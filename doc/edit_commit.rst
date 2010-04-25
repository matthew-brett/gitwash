.. _edit-commit:

=======================
 Editing and commiting
=======================

#. |repo-cd|
#. Make some changes
#. See which files have changed with ``git status``.  If you have done
   :ref:`git-config` then you could use the configured alias for
   ``status`` - as in ``git stat``.  You'll see a listing like this one::

     # On branch master
     # Changed but not updated:
     #   (use "git add <file>..." to update what will be committed)
     #   (use "git checkout -- <file>..." to discard changes in working directory)
     #
     #	modified:   README
     #
     # Untracked files:
     #   (use "git add <file>..." to include in what will be committed)
     #
     #	INSTALL
     no changes added to commit (use "git add" and/or "git commit -a")

#. Check what the actual changes are with ``git diff``
#. Add any new files to version control ``git add new_file_name``
#. To commit all modified files, do ``git commit -am 'A commit
   message'``.  Note the ``-a`` flag to ``git commit``.  This commits
   *to your local machine*.

.. include:: links_names.txt
.. include:: substitutions.txt
