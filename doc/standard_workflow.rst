=======================
 Standard git workflow
=======================

If you haven't already, :ref:`forking`, and :ref:`cloning`, and |repo-cd|

Then:

#. Make some changes
#. Check what has changed with ``git status``.  If you have done
   :ref:`git-config` then you could use the configured alias for
   ``status`` - as it ``git stat``.  You'll see a listing like this one::




Merging from trunk
==================

Make sure you have done the :ref:`linking-to-mainline`.

Merge the mainline code into your current development by first pulling
the mainline repo to a copy on your local machine::

   git fetch mainline

then merging into your current branch::

   git merge mainline/master


.. include:: links_names.txt
.. include:: substitutions.txt
