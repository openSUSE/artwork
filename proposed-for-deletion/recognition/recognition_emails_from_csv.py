#!/usr/bin/env python3
import csv
import sys
import subprocess
import smtplib
import time

from optparse import OptionParser
from email.mime.text import MIMEText
import email.utils

from retry import retry

DEFAULT_DELIMITER = ","


# map of default config entries
config = {
    'relay': 'relay.suse.de',
}

@retry(tries=10,delay=5,jitter=1)
def send_email(relay, user, to, from_addr, subject, body):

    # Create the container (outer) email message.
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to
    msg['Message-ID'] = email.utils.make_msgid()
    msg['Date'] = email.utils.formatdate(localtime=1)

    print ("Sending email from: %s to: %s (%s)" % (from_addr, to, user))
    time.sleep(0.5) # let's not flood server
    relay.sendmail(from_addr, to, msg.as_string())
    print ("Email sent.")

def get_userinfo(username):
    """
    args:
        username - OBS username, or a "Name Surname <user@domain>
                   in case of no OBS account"
    Returns:
        None or ("name surname", "user@email")
    """
    username = username.strip()
    result = []
    print ("Checking user info for: %s" % username)
    if "@" in username:
        result = email.utils.parseaddr(username)
    else:
        out = str(subprocess.check_output(["osc", "whois", username]))
        if "not found" in str(out):
            return None

        result = email.utils.parseaddr(out)

    return (username, result[0], result[1])


def get_personalised_template(template, userdata, text):
    result = template.replace("__USER__", userdata[1])
    result = result.replace("__TEXT__", text)
    return result

def main():
    parser = OptionParser(usage="%prog --csv example_recognition_input.csv recognition_leap_15.2_retro_example_individual.htm")
    parser.add_option("--csv", help="Data with recipients")
    parser.add_option("--delimiter", help="csv delimiter [%s]" % DEFAULT_DELIMITER, default=DEFAULT_DELIMITER)
    parser.add_option("--subject", help="Subject of the e-thank you")
    parser.add_option("--from", dest="from_addr", help="Email sender", default="marketing@lists.opensuse.org")

    opts, args = parser.parse_args()

    if len(args) != 1:
        parser.error("Expected one argument which is the HTML template for recognition email")

    if not opts.csv:
        parser.error("You need to specify input csv with columns Team, OBS Username, Text")

    if not opts.subject:
        parser.error("Please specify subject of the recognition email.")

    if not opts.from_addr:
        parser.error("Please specify sender of the recognition email.")

    email_template = None
    with open(args[0]) as reader:
        email_template = reader.read()

    personalised_emails = {} # email: body
    not_found = []
    failed = {}
    with open(opts.csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=opts.delimiter, quotechar='"')
        for row in csvreader:
            if len(row) < 3: # Team, OBS Login, Text:
                sys.stderr.write("Expected at least three columns and got %d, did you check the delimiter?.\nExpected columns: Team, OBS Login, Recognition Text\n" % len(row))
                sys.exit(2)
            if row[0][0] == "#":
                continue # skip comments

            username, to, text = row[1], None, None
            userdata = get_userinfo(username)
            if not userdata:
                not_found.append(username)
            else:
                to = userdata[2]
                text = get_personalised_template(email_template, userdata, row[2])

                personalised_emails[username] = (to, text)

    if not_found:
        sys.stderr.write("Error: These OBS accounts were not found: %s\n" % ", ".join(not_found))
        sys.exit(1)

    print("All email addresses look okay. Hit enter to proceed with sending emails. Ctrl+C to cancel.")
    input()
    relay = smtplib.SMTP(config['relay'])
    for username in personalised_emails:
        try:
            send_email(relay, username, personalised_emails[username][0], opts.from_addr, opts.subject, body=personalised_emails[username][1])
        except:
            sys.stderr.write("ERROR: Sending failed for user %s. Skipping\n" % username)
            failed[username] = personalised_emails[username]
            relay.quit() # try to re-establish connection to SMTP
            relay = smtplib.SMTP(config['relay'])
            # continue
    relay.quit()
    if failed:
        sys.stderr.write("Failed to send email to following accounts: %s\n" % ", ".join(failed.keys()))

if __name__ == "__main__":
    main()
