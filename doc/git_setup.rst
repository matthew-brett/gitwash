=========
GIT setup
=========

Before you get going with git_, you'll need to install it, and configure it.

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

Configure GIT on each computer
==============================

Configure git_ by identifying yourself, and adding some aliases to
common commands.  We'll use these aliases later.  You only need to do
this once for each computer on which you will use git::

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

In fact, these commands will write to your user's git configuration file
``~/.gitconfig``.  Specifically this file will become::

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

To set up on another computer, run the commands again, or just copy your
``.gitconfig`` file to the home directory on your new computer.

Set up and configure a github_ account
======================================

If you don't have a github_ account, go to the github_ page, and make one. 

You then need to configure your account to allow write access - see the
``Generating SSH keys`` help on `github help`_.


.. include:: links_names.txt


