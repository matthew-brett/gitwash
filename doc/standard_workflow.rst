=======================
 Standard git workflow
=======================

Merging from trunk
==================

Make sure you have done the :ref:`linking-to-mainline`.

Merge the mainline code into your current development by first pulling
the mainline repo to a copy on your local machine::

   git fetch mainline

then merging into your current branch::

   git merge mainline/master


.. include:: links_names.txt
