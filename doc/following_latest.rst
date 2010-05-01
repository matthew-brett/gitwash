.. _following-latest:

=============================
 Following the latest source
=============================

These are the instructions if you just want to follow the latest
*nipy* source, but you don't need to do any development for now.

The steps are:

* install git_
* get local copy of the git repository from github_
* update local copy from time to time

.. include:: install.txt

Get the local copy of the code
==============================

From the command line::

   git clone git://github.com/nipy/nipy.git

You now have a copy of the code tree in the new ``nipy``x directory.

Updating the code
=================

From time to time you may want to pull down the latest code.  Do this with::

   cd nipy
   git pull

The tree in ``nipy`` will now have the latest changes from the initial
repository.

At some stage you might consider editing the code; in that case, see
:ref:`follower-to-developer`.

