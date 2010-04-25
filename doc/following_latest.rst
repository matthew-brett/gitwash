.. _following-latest:

=============================
 Following the latest source
=============================

These are the instructions if you just want to follow the latest
|reponame| source, but you don't need to do any development for now.

Get the read-only source
========================

Run |repoclone-ro|

You now have a copy of the code tree in the |reponame| directory.

Updating the code
=================

After you've done the initial clone, you can get the latest changes with:

#. |repo-cd|
#. ``git pull``

The tree in |reponame| will now have the latest changes from the initial
repository.

Editing the code
================

You may find yourself wanting to make a few changes to the code, maybe
for a fix or changing a small feature.  If you do, then you can do this
in your repository, by following the usual :ref:`edit-commit` cycle.
You can still do ``git pull`` from time to time to merge the upstream
code back into your local repository.

If you find you'd like to give your changes back, then just follow the
instructions in :ref:`follower-to-developer`.

.. include:: substitutions.txt
