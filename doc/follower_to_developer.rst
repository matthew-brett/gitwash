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

   # remove read-only pointer to upstream repository
   git remote rm origin
   # add pointer to your own fork
   git remote add origin git@github.com:you-user-name/nipy.git
   # add back renamed read-only pointer to upstream
   git remote add mainline git://github.com/gitwash/nipy.git
   # push your branch to github
   git checkout my-edits
   git push origin my-edits

Details
-------

Make a github_ account
~~~~~~~~~~~~~~~~~~~~~~

.. include:: make_account.txt

Tell git_ who you are
~~~~~~~~~~~~~~~~~~~~~

.. include:: set_user.txt

Make a forked copy of nipy
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: make_fork.txt





Making a patch
==============

Overview
--------

some text


.. include:: links_names.txt



