=======================
 Standard git workflow
=======================

Editing and commiting
======================

If you haven't already, :ref:`forking`, and :ref:`cloning`, and |repo-cd|

Then:

#. Make some changes
#. See which files have changed with ``git status``.  If you have done
   :ref:`git-config` then you could use the configured alias for
   ``status`` - as it ``git stat``.  You'll see a listing like this one::

   # On branch master
   # Changed but not updated:
   #   (use "git add <file>..." to update what will be committed)
   #   (use "git checkout -- <file>..." to discard changes in working directory)
   #
   #	modified:   README
   #
   # Untracked files:
   #   (use "git add <file>..." to include in what will be committed)
   #
   #	INSTALL
   no changes added to commit (use "git add" and/or "git commit -a")

#. Check what the actual changes are with ``git diff``
#. Add any new files to version control ``git add new_file_name``
#. To commit all modified files, do ``git commit -am 'A commit
   message'``.  Note the ``-a`` flag to ``git commit``.  This commits
   *to your local machine*.

Pushing up to your github_ repo
===============================

``git push origin master``

Asking for merge
================

#. Goto |repourl|
#. Click on the 'Pull request' button:

   .. image:: pull_button.png

   Enter a message; select only the repository owner as the recipient.    

Merging from trunk
==================

This updates your code from the mainline |repourl| repo. 

Make sure you have done :ref:`linking-to-mainline`.

Merge the mainline code into your current development by first pulling
the mainline repo to a copy on your local machine::

   git fetch mainline

then merging into your current branch::

   git merge mainline/master

Making a new local and remote branch
====================================

#. ``git co -b new_branch`` - create the new branch locally and check it out
#. ``git push origin new_branch`` - push the new branch back to github_

If you want to delete a remote branch for some reason, see:
http://github.com/guides/remove-a-remote-branch


.. include:: links_names.txt
.. include:: substitutions.txt
