.. _development-workflow:

====================
Development workflow
====================

You already have your own forked copy of the PROJECTNAME_ repository, by
following :ref:`forking`, :ref:`set-up-fork`, and you have configured
git by following :ref:`configure-git`.

Workflow summary
================

* Make a ``main-master`` branch to keep track of the changes in the upstream
  master branch. We'll call the upstream master branch "trunk" in the rest of
  this page.
* Don't use your ``master`` branch for anything.  Consider deleting it.
* When you are starting a new set of changes, update the ``main-master`` branch,
  and start a new *feature branch* from that.
* Make a new branch for each separable set of changes.
* If you can possibly avoid it, try not to merge other branches into your
  feature branch while you are working.
* If you do find yourself merging from another branch, consider ``git rebase``
* Ask for review!

This way of working really helps to keep work well organized, and in
keeping history as clear as possible.

See |emdash| for example |emdash| `linux git workflow`_.

Make a branch to keep track of trunk
====================================

Here we make a branch to keep track of the upstream `PROJECTNAME github`_  repo.

Overview
--------

Once per repository clone::

    # make a tracking branch to track upstream
    git branch main-master --track upstream/master

From time to time, to pull down the latest changes::

   # go to your main-master tracking branch
   git checkout main-master
   # get upstream changes from github
   git fetch upstream
   # merge from upstream
   git merge upstream/master

We've used the name ``main-master`` to remind ourselves that this is
the upstream branch.

In detail
---------

We suggest that you only merge the upstream changes into your ``main-master``
branch, and leave your 'feature' branches unmerged.  This keeps your code
history clean and makes code review easier.

First make sure you have done :ref:`linking-to-upstream`.

Next make the upstream tracking branch.  You need to do this once for each clone
you have made::

    git branch main-master --track upstream/master

This ``main-master`` branch will only contain the state of the upstream code.
That is, please be careful not to make your own changes in this branch, as
things will start to get confusing.

To update your ``main-master`` branch with the latest upstream changes::

    git checkout main-master
    git fetch upstream
    git merge upstream/master

Consider deleting your master branch
====================================

It may sound strange, but deleting your own ``master`` branch can help reduce
confusion about which branch you are on.  See `deleting master on github`_ for
details.

Make a new feature branch
=========================

When you are ready to make some changes to the code, you should start a new
branch.  Branches that are for a collection of related edits are often called
'feature branches'.

::

    # Make new feature branch starting at current trunk
    git branch my-new-feature main-master
    git checkout my-new-feature

Generally, you will want to keep your feature branches on your public github_
fork of PROJECTNAME_.  To do this, you `git push`_ this new branch up to your
github repo.  Generally (if you followed the instructions in these pages, and by
default), git will have a link to your github repo, called ``origin``.  You push
up to your own repo on github with::

   git push origin my-new-feature

In git > 1.7 you can ensure that the link is correctly set by using the
``--set-upstream`` option::

   git push --set-upstream origin my-new-feature

From now on git will know that ``my-new-feature`` is related to the
``my-new-feature`` branch in the github repo.

The editing workflow
====================

Overview
--------

::

   # hack hack
   git add my_new_file
   git commit -am 'NF - some message'
   git push

In more detail
--------------

#. Make some changes
#. See which files have changed with ``git status`` (see `git status`_).
   You'll see a listing like this one::

     # On branch ny-new-feature
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

#. Check what the actual changes are with ``git diff`` (`git diff`_).
#. Add any new files to version control ``git add new_file_name`` (see
   `git add`_).
#. To commit all modified files into the local copy of your repo,, do
   ``git commit -am 'A commit message'``.  Note the ``-am`` options to
   ``commit``. The ``m`` flag just signals that you're going to type a
   message on the command line.  The ``a`` flag |emdash| you can just take on
   faith |emdash| or see `why the -a flag?`_ |emdash| and the helpful use-case
   description in the `tangled working copy problem`_. The `git commit`_ manual
   page might also be useful.
#. To push the changes up to your forked repo on github, do a ``git
   push`` (see `git push`).

Ask for your changes to be reviewed or merged
=============================================

When you are ready to ask for someone to review your code and consider a merge:

#. Go to the URL of your forked repo, say
   ``http://github.com/your-user-name/REPONAME``.
#. Use the 'Switch Branches' dropdown menu near the top left of the page to
   select the branch with your changes:

   .. image:: branch_dropdown.png

#. Click on the 'Pull request' button:

   .. image:: pull_button.png

   Enter a title for the set of changes, and some explanation of what you've
   done.  Say if there is anything you'd like particular attention for - like a
   complicated change or some code you are not happy with.

   If you don't think your request is ready to be merged, just say so in your
   pull request message.  This is still a good way of getting some preliminary
   code review.

Deleting a branch on github
===========================

::

   git checkout master
   # delete branch locally
   git branch -D my-unwanted-branch
   # delete branch on github
   git push origin :my-unwanted-branch

(Note the colon ``:`` before ``test-branch``.  See also:
http://github.com/guides/remove-a-remote-branch

Several people sharing a single repository
==========================================

If you want to work on some stuff with other people, where you are all
committing into the same repository, or even the same branch, then just
share it via github.

First fork PROJECTNAME into your account, as from :ref:`forking`.

Then, go to your forked repository github page, say
``http://github.com/your-user-name/REPONAME``

Click on the 'Admin' button, and add anyone else to the repo as a
collaborator:

   .. image:: pull_button.png

Now all those people can do::

    git clone git@githhub.com:your-user-name/REPONAME.git

Remember that links starting with ``git@`` use the ssh protocol and are
read-write; links starting with ``git://`` are read-only.

Your collaborators can then commit directly into that repo with the
usual::

     git commit -am 'ENH - much better code'
     git push origin master # pushes directly into your repo

Explore your repository
=======================

To see a graphical representation of the repository branches and
commits::

   gitk --all

To see a linear list of commits for this branch::

   git log

You can also look at the `network graph visualizer`_ for your github
repo.

.. include:: links.inc
