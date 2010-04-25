===========================
git setup for each computer
===========================

Install
=======

See the git_ page for the most recent information.

Have a look at the github_ install help pages available from `github help`_

There are good instructions here: http://book.git-scm.com/2_installing_git.html

At the time of writing, these should work for some standard platforms:

================ =============
Debian / ubuntu  ``sudo apt-get install git-core``
Fedora           ``sudo yum install git-core``
Windows          Download and install msysGit_
OS X             Use the git-osx-installer_
================ =============

.. _git-config:

Configure
=========

Configure git_ by identifying yourself, and adding some aliases to
common commands.  We'll use these aliases later.  You only need to do
this once for each computer on which you will use git.  The easiest way
to do this, is to create a ``.gitconfig`` file in your home directory,
with contents like this::

  [core]
          editor = emacs
  [user]
          email = you@yourdomain.example.com
          name = Your Name Comes Here
  [alias]
          ca = commit -a
          st = status
          stat = status
          co = checkout
  [color]
          diff = auto
          status = true

(of course you'll need to set your email and name, and may want to set
your editor).  If you prefer, you can do the same thing from the command
line::

  # optional - configure your default text editor for git
  git config --global core.editor emacs
  # give your name and email address to label your commits
  git config --global user.email you@yourdomain.example.com
  git config --global user.name "Your Name Comes Here"
  # add some useful aliases
  git config --global alias.ca "commit -a" # git ca -> git commit -a 
  git config --global alias.st status
  git config --global alias.stat status
  git config --global alias.co checkout
  # add some nice colors to diff printouts and status output
  git config --global color.diff auto
  git config --global color.status true

These commands will write to your user's git configuration file
``~/.gitconfig``. 

To set up on another computer, you can copy your ``~/.gitconfig`` file,
or run the commands above.

You may want to start just by following the latest source
(:ref:`following-latest`) - or you may want to jump straight in as a
developer (:ref:`start-as-developer`).

.. include:: links_names.txt


