.. _start-as-developer:

======================================
 Starting from scratch as a developer
======================================

These are the instructions for the situation where you know that you
want to edit the code and make your changes available to the rest of us.

First you follow the instructions for :ref:`forking`. Now:

Clone your fork
===============

#. Clone your fork to the local computer with |repoclone-rw|
#. Investigate.  Change directory to your new repo: |repo-cd|. Then
   ``git branch -a`` to show you all branches.  You'll get something
   like::

      * master
      remotes/origin/master

   This tells you that you are currently on the ``master`` branch, and
   that you also have a ``remote`` connection to ``origin/master``.
   What remote repository is ``remote/origin``? Try ``git remote -v`` to
   see the URLs for the remote.  They will point to your github_ fork.

   Now you want to connect to the mainline |repourl| repository, so you
   can merge in changes from trunk.

.. _linking-to-mainline:

Linking your repository to the mainline repo
============================================

#. |repo-cd| if you haven't done this already
#. |repo-add-remote|

   Note that we've used ``git://`` for the URL rather than ``git@``.  The
   ``git://`` URL is read only.  This means we that we can't
   accidentally (or deliberately) write to the mainline repo, and we are
   only going to use it to merge into our own code.

You are now ready to follow the :ref:`development-workflow`.

.. include:: links_names.txt
.. include:: substitutions.txt

