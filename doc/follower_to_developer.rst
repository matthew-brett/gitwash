.. _follower-to-developer:

==================================================
 Changing from following the code, to development
==================================================

Private edits, keeping track of upstream development
====================================================

Overview
--------

::
       
   # make new branch
   git branch my-edits
   git checkout my-edits
   # hack hack
   git commit -am 'My edits in my branch'
   # update your branch from upstream
   git pull origin/master

Keeping a github_ copy of your private edits
============================================

Overview
--------

#. make a github_ account
#. tell git_ who you are
#. fork *nipy* repository using github_ interface

Then::

   git remote rm origin
   git remote add origin git@github.com:your-user-name/nipy.git
   git remote add mainline git://github.com/gitwash/nipy.git
   git push origin my-edits

Details
-------

Make a github_ account
~~~~~~~~~~~~~~~~~~~~~~

.. include:: make_account.txt

Tell git_ who you are
~~~~~~~~~~~~~~~~~~~~~

Make a forked copy of nipy
~~~~~~~~~~~~~~~~~~~~~~~~~~


Link your local branch to github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git uses the ``origin`` name to point to the main home of this
repository.  You want to set this to be your forked copy.

First, delete the current ``origin`` link, because that points to the
main *nipy* repository::

   git remote rm origin

Next make ``origin`` point to your new forked copy::

   git remote add origin git@github.com:your-user-name/nipy.git

Add back the reference to the main *nipy* repository, but with another
name::

   git remote add mainline git://github.com/gitwash/nipy.git

Next push your own branch into your own github copy of *nipy*::

   git push origin my-edits


Making a patch
==============

Overview
--------

some text


.. include:: links_names.txt



