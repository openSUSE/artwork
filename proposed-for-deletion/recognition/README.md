This tool and data is for a current effort to recognize contributors to the project that received possitive feedback
as part of openSUSE Leap release retro.

Script is substituing __USER__ and __TEXT__ in supplied email template with text and OBS account info from the .csv
This is then send to the email gathered by osc whois $user

* The actual retrospective https://en.opensuse.org/Portal:15.2/Retrospective
* Action item shttps://progress.opensuse.org/projects/leap152retro/issues
 

Example usage:

./generate_emails_from_csv.py --csv example_recognition_input.csv recognition_leap_15.2_retro_example_individual.htm

First column in the csv is not really used by the script, but is extremely helpful for putting together the recognition text.
Leap 15.2 recognitions were sent to about 150 accounts. Altought there is a retry implemented.
In some cases the SMTP and script needs to be re-executed.

My recommendation is to wait for the end output which says for which accounts has the delivery failed and then grep the file for the misisng ones,
or simply comment lines in csv with '#' for every entry that was already processed which is identified by "Email sent." confirmation on the stdout.
