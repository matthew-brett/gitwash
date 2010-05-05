================
 Making a patch
================

You've discovered a bug or something else you want to change in nipy_ - excellent!

You've worked out a way to fix it - even better!

You want to tell us about it - best of all!

Here's how.

If you don't already have one, clone a copy of the nipy_ repository::

      git clone git://github.com/nipy/nipy.git

For a very simple change
========================

#. Edit the code in your new ``nipy`` directory.
#. When your edits are good, make a patch::

   git diff > my_bug_fix.patch

#. Send ``my_bug_fix.patch`` to the `nipy mailing list`_.

For a less simple change
========================

This is a change which might need a bit of thought, and revision.  In this case you can use git_ to keep track of your changes as you go.

#. Make a 'feature branch'::

      git branch the-fix-im-thinking-of
      git checkout the-fix-im-thinking-of

#. Do some edits, and commit them as you go::

      # hack, hack
      git commit -am 'BF - added tests for Funny bug'
      # hack hack
      git commit -am 'BF - added fix for Funny bug'

#. When you have finished, check you have committed all your changes::

      git stat

#. Finally, make your commits into patches::

      git format-patch -M -C

   You will now have several files named like::

      0001-BF-added-tests-for-Funny-bug.patch
      0002-BF-added-fix-for-Funny-bug.patch

   Send these files to the `nipy mailing list`_.

.. include:: links_names.txt
