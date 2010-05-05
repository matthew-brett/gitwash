.. _development-workflow:

========================
git development workflow
========================

You already have your own copy of the |reponame| repository, either from
:ref:`start-as-developer` or :ref:`follower-to-developer`.

You now might want to do some cycles of :ref:`edit-commit`.

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
