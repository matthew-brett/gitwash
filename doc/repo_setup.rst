=============================
 Initial setup of repository
=============================

You need to do this only once.  The instructions here are very similar
to the instructions at http://help.github.com/forking/ - please see that
page for more detail.  We're repeating most of it here just to give the
specifics for the |reponame| project, and to suggest some default names.

Create your own repository fork
===============================

#. Log into your github_ account.
#. Go to the |reponame| github home at |repourl|. 
#. Click on the *fork* button:

   .. image:: forking_button.png

   Now, after a short pause and some 'Hardcore forking action', you
   should find yourself at the home page for your own forked copy of |reponame|

.. _linking-to-mainline:

Linking the repository to the original repository
=================================================

#. Clone your fork to the local computer with |repoclone|
#. Investigate.  Change directory to your new repo: |repo-cd| . Then
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

#. Add the connection to |repourl| by |repo-cd| if you haven't done this
   already, then run |repo-add-remote|

   Note that we've used ``git://`` for the URL rather than ``git@``.  The
   ``git://`` URL is read only.  This means we that we can't
   accidentally (or deliberately) write to the mainline repo, and we are
   only going to use it to merge into our own code.


.. include:: links_names.txt
.. include:: substitutions.txt

