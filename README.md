openSUSE Artwork Repository
###########################
This is the repository of the (artwork team)[https://en.opensuse.org/openSUSE:Art_team].
While a version control system such as git may seem daunting, it is by far the
best option for collaborative authoring. GitHub is also relatively easy to use.


License
-------
All content in is licensed under (CC-BY-SA 3.0)[http://creativecommons.org/licenses/by-sa/3.0/] unless
otherwise stated.

Contribute
----------
Contents

  • 1 Initial setup
  • 2 Workflow
      □ 2.1 Getting the latest changes
      □ 2.2 Adding new files or directories
      □ 2.3 Committing changes
      □ 2.4 Pushing changes
      □ 2.5 Status
      □ 2.6 Removing files
      □ 2.7 Renaming or moving files or directories
      □ 2.8 History
  • 3 TODO

Initial setup

If you would like to modify or add material to our repository, you need to do
the following things first:

 1. register an account on GitHub, if you don't already have one
 2. install git (as root or use sudo, zypper install git), if you don't have it
    already
 3. See the GitHub help to set up your account and get an SSH key in there.
 4. ask admin@opensuse.org to add your user account to the team on github,
    which will give you write access to the repo.
 5. run the following commands in your ordinary user shell:
     1. git config --global user.email "my.email@address" (obviously with your
        real email address ;))
     2. git config --global user.name "John Doe" (again, with your real name)
 6. pick some directory where you'll want the files to reside, e.g. ~/Documents
    and go there in your shell, e.g. cd ~/Documents
 7. retrieve the repository with the following command as user: git clone
    git@github.com:openSUSE/artwork.git (which will create a subdirectory
    "artwork")

Workflow

Getting the latest changes

In order to pull the latest changes that have been stored in the repository,
use the following command:

git pull

That will download the latest version of everything that is in the repository
on github, and store it on your disk.

Of course, that command needs to be ran from a shell while being in your local
artwork directory (e.g. ~/Documents/artwork)

Adding new files or directories

When you create a new file or directory, you have to tell git that you would
like to add it to the repository first, using the following command:

git add filename

(where you replace filename with the actual name of the file or directory you
want to add).

Note that adding a file does not upload it to the repository yet, it merely
instructs git that you want to put it under version control.

Committing changes

When you change files and you would like to store their state in the repository
(e.g. when you think it's good enough to be used by others), use the following
command:

git commit -m "some comment about the change I just made" filename

Please use meaningful comments (what's after -m) as that will help everyone to
keep track of the changes that were made. Also, make sure to put the comment
into quotes (between "") or the shell will interpret it as several parameters
for the git command, which it isn't.

You can also commit changes of several files at once, which is the preferred
approach when the changes do apply to several files (e.g. you just changed the
color palette on a dozen Inkscape files): that way, your changes will show up
as one "action" in the history of the repository.

To do so, just pass several filenames to the git commit command, like this:

git commit -m "changed palette to the right colors" filename1 filename2
filename3

You can also commit all the changes to all the files in your local copy of the
repository, by using the -a switch, like this:

git commit -m "changed palette to Bento colors" -a

Pushing changes

When you commit changes, git will only store them in your local repository on
your hard disk, and not to the artwork repository on github, which means that
no one else will be able to see your changes.

git works that way because you may choose to make changes locally, on your hard
disk, and keep track of those changes to be able to revert to a previous
version, without necessarily pushing those changes to all the other people who
work on the repository just yet.

Once you want to share your changes with everyone else, you must "push" those
changes to the repository, with the following command:

git push

Note that the very first time you will do a git push, you will have to use this
command: git push origin master

From then on, you will only need to use git push

Furthermore, when you want to push your changes to gitorious, it is possible
that someone else already pushed other changes there. git will tell you see
when that happened, and you will just need to make a git pull before the git
push

Note Dolphin, KDE's file manager, has git support. The actions described above
can be done quite easily from there. Configure Dolphin and under Services you
can enable Git support. It will then automatically detect git folders and let
you add files you changed, make commits and push and pull changes.

Status

With the command git status, you can see whether you have files on your hard
disk that have changes (or new files, or deleted files) that have not been
committed yet.

Example:

git status

would output something like this:

# On branch master
# Changed but not updated:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#       modified:   git-mini-howto.txt
#
no changes added to commit (use "git add" and/or "git commit -a")

The output above means that the file git-mini-howto.txt is locally modified:
you have made changes to that file, but those changes are not committed (yet).

Removing files

If you want to delete a file from the repository, use git rm instead of
removing it as you would normally do (using rm filename or your favourite file
browser), like this:

git rm filename

Removing a file is just yet another change for git and, hence, to commit the
change: git commit -m "removed that file, it's obsolete now" filename (or the
other commit commands as explained above, such as git commit -a -m "...")

To push that change to gitorious, for everyone: git push

Renaming or moving files or directories

When you want to rename a file or directory, or move it elsewhere, do not use
the regular command-line or file manager options to do so. If you do that, git
will consider the renamed/moved file to be a new one and hence will lose the
history of changes.

The proper way of doing so is by using git mv, like this:

git mv old_filename new_filename

As usual, you will need to commit and push for that change to be visible for
everyone.

History

One of the most obvious advantages of version control systems such as git is
the ability to see the history of a file, which is a log of the modifications
that have been made, with the commit messages (see the -m option for git
commit), when changes were made and by whom.

To see the history of a file, use the following command:

git log filename

That will display something like this:

commit bbcf4e3a848d65fc28d1fb6d20d0ce7add040a33
Author: Pascal Bleser <pascal.bleser@opensuse.org>
Date:   Tue Feb 15 23:46:11 2011 +0100

    add LICENSE

There is only one change on the file above, but it shows

  • whom made the change: Pascal Bleser
  • when that change was made: Tue Feb 15
  • what was changed (the commit message): "add LICENSE"

You can also see the all the changes, of the whole repository (and not just of
a single file), by using

git log

(without passing a file name)

Please note that git log commands automatically put the output into a pager
(normally that is /usr/bin/less), which gives you the ability to navigate the
output (with expected keys, such as arrow up, arrow down, page up, page down,
...). To leave the pager and return to the shell, simply press the key "q"
(mnemonics: "q" as in "quit").

git log has quite a few more options, which you can read about by typing git
log --help (also opens in the pager, press "q" to quit.)

TODO

  • document how to retrieve previous revisions of a file (git checkout)
  • document how to reset your working environment to the state of the
    repository, to remove all your local changes (git reset --hard)
  • mention graphical user interfaces (gitk, qgit, ...)
  • link to other howtos, cheat sheets, etc, such as http://
    cheat.errtheblog.com/s/git


Mirrors
-------
http://geeko.ioda.net/git/artwork/
rsync://geeko.ioda.net/git/artwork

The mirror is refreshed every 10 minutes
