.. highlight:: bash

.. _following-latest:

=============================
 Following the latest source
=============================

These are the instructions if you just want to follow the latest
*PROJECTNAME* source, but you don't need to do any development for now.

The steps are:

* :ref:`install-git`
* get local copy of the `PROJECTNAME github`_ git repository
* update local copy from time to time

Get the local copy of the code
==============================

From the command line::

   git clone https://github.com/MAIN_GH_USER/REPONAME.git

You now have a copy of the code tree in the new ``REPONAME`` directory.

Updating the code
=================

From time to time you may want to pull down the latest code.  Do this with::

   cd REPONAME
   git pull

The tree in ``REPONAME`` will now have the latest changes from the initial
repository.

.. include:: links.inc
