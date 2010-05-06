================
 Making a patch
================

You've discovered a bug or something else you want to change in nipy_ - excellent!

You've worked out a way to fix it - even better!

You want to tell us about it - best of all!

Here's how.

If you don't already have one, clone a copy of the nipy_ repository::

      git clone git://github.com/nipy/nipy.git

#. Make a 'feature branch'.  This will be where you work on your bug
   fix.  It's nice and safe and leaves you with access to an unmodified
   copy of the code in the main branch::

      git branch the-fix-im-thinking-of
      git checkout the-fix-im-thinking-of

#. Do some edits, and commit them as you go::

      # hack, hack, hack
      # Tell git about any new files you've made
      git add somewhere/tests/test_my_bug.py
      # commit work in progress as you go
      git commit -am 'BF - added tests for Funny bug'
      # hack hack, hack
      git commit -am 'BF - added fix for Funny bug'

#. When you have finished, check you have committed all your changes::

      git status

#. Finally, make your commits into patches::

      git format-patch -M -C

   You will now have several files named for the commits::

      0001-BF-added-tests-for-Funny-bug.patch
      0002-BF-added-fix-for-Funny-bug.patch

   Send these files to the `nipy mailing list`_.

When you are done, to switch back to the main copy of the code, just
return to the ``master`` branch::

   git checkout master

.. include:: links_names.txt
