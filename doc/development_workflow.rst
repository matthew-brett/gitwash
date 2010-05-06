.. _development-workflow:

====================
Fevelopment workflow
====================

You already have your own forked copy of the nipy_ repository, by
following :ref:`forking`, :ref:`set-up-fork`, and you have configured
git_ by following :ref:`configure-git`.

We recommend strongly that you start a new 'feature branch' each time to
start a new set of edits.  It really helps when you ask for code review
or merges later on.  It also helps keep work organized.

Making a new feature branch
===========================

::

   git branch my-new-feature
   git checkout my-new-feature

Generally, you will want to keep this also on your public github_ fork
of nipy_.  To do this, you ``push`` this new branch up to your github_
repo.  Generally (if you followed the instructions in these pages, and
by default), git will have a link to your github_ repo, called
``origin``.  You push up to github_ with::

   git push origin my-new-feature

From now on git_ will know that ``my-new-feature`` is related to the
``my-new-feature`` branch in the gitub_ repo.

The editing workflow
====================

Overview
--------

::

   # hack hack
   git add my_new_file
   git commit -am 'NF - some message'
   git push

In more detail
--------------

#. Make some changes
#. See which files have changed with ``git status``.  You'll see a
   listing like this one::

     # On branch ny-new-feature
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
#. To push the changes up to your forked repo on github_, do a ``git push``.  

Asking for merge
================

When you are ready to ask for the merge of your code:

#. Goto the URL of your forked repo, say ``http://github.com/your-user-name/nipy.git``. 
#. Click on the 'Pull request' button:

   .. image:: pull_button.png

   Enter a message; we suggest you select only ``nipy`` as the
   recipient, but feel free to add others from the list as you like.

Merging from trunk
==================

This updates your code from the mainline `nipy github`_  repo. 

Overview
--------

::

   # go to your master branch
   git checkout master
   # pull changes from github
   git fetch mainline
   # merge from mainline
   git merge mainline master

In detail
---------

We suggest that you do this only for your ``master`` branch, and leave
your 'feature' branches unmerged, to keep their history as clean as
possible.  This makes code review easier::

   git checkout master

Make sure you have done :ref:`linking-to-mainline`.

Merge the mainline code into your current development by first pulling
the mainline repo to a copy on your local machine::

   git fetch mainline

then merging into your current branch::

   git merge mainline/master

Deleting a branch on github_
============================

::

   git checkout master
   # delete branch locally
   git branch -D my-unwanted-branch
   # delete branch on github
   git push origin :my-unwanted-branch

(Note the colon ``:`` before ``test-branch``.  See also:
http://github.com/guides/remove-a-remote-branch

.. include:: links_names.txt
