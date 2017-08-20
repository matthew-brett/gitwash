.. highlight:: bash

.. _development-workflow:

####################
Development workflow
####################

You already have your own forked copy of the `PROJECTNAME`_ repository, by
following :ref:`forking`. You have :ref:`set-up-fork`. You have configured
git by following :ref:`configure-git`.  Now you are ready for some real work.

Workflow summary
================

In what follows we'll refer to the upstream PROJECTNAME ``master`` branch, as
"trunk".

* Don't use your ``master`` branch for anything.  Consider deleting it.
* When you are starting a new set of changes, fetch any changes from trunk,
  and start a new *feature branch* from that.
* Make a new branch for each separable set of changes |emdash| "one task, one
  branch" (`ipython git workflow`_).
* Name your branch for the purpose of the changes - e.g.
  ``bugfix-for-issue-14`` or ``refactor-database-code``.
* If you can possibly avoid it, avoid merging trunk or any other branches into
  your feature branch while you are working.
* If you do find yourself merging from trunk, consider :ref:`rebase-on-trunk`
* Ask on the `PROJECTNAME mailing list`_ if you get stuck.
* Ask for code review!

This way of working helps to keep work well organized, with readable history.
This in turn makes it easier for project maintainers (that might be you) to see
what you've done, and why you did it.

See `linux git workflow`_ and `ipython git workflow`_ for some explanation.

Consider deleting your master branch
====================================

It may sound strange, but deleting your own ``master`` branch can help reduce
confusion about which branch you are on.  See `deleting master on github`_ for
details.

.. _update-mirror-trunk:

Update the mirror of trunk
==========================

First make sure you have done :ref:`linking-to-upstream`.

From time to time you should fetch the upstream (trunk) changes from github::

   git fetch upstream

This will pull down any commits you don't have, and set the remote branches to
point to the right commit.  For example, 'trunk' is the branch referred to by
(remote/branchname) ``upstream/master`` - and if there have been commits since
you last checked, ``upstream/master`` will change after you do the fetch.

.. _make-feature-branch:

Make a new feature branch
=========================

When you are ready to make some changes to the code, you should start a new
branch.  Branches that are for a collection of related edits are often called
'feature branches'.

Making an new branch for each set of related changes will make it easier for
someone reviewing your branch to see what you are doing.

Choose an informative name for the branch to remind yourself and the rest of us
what the changes in the branch are for.  For example ``add-ability-to-fly``, or
``buxfix-for-issue-42``.

::

    # Update the mirror of trunk
    git fetch upstream
    # Make new feature branch starting at current trunk
    git branch my-new-feature upstream/master
    git checkout my-new-feature

Generally, you will want to keep your feature branches on your public github_
fork of `PROJECTNAME`_.  To do this, you `git push`_ this new branch up to your
github repo.  Generally (if you followed the instructions in these pages, and by
default), git will have a link to your github repo, called ``origin``.  You push
up to your own repo on github with::

   git push origin my-new-feature

In git >= 1.7 you can ensure that the link is correctly set by using the
``--set-upstream`` option::

   git push --set-upstream origin my-new-feature

From now on git will know that ``my-new-feature`` is related to the
``my-new-feature`` branch in the github repo.

.. _edit-flow:

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
   You'll see a listing like this one:

   .. code-block:: none

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
   push`` (see `git push`_).

Ask for your changes to be reviewed or merged
=============================================

When you are ready to ask for someone to review your code and consider a merge:

#. Go to the URL of your forked repo, say
   ``https://github.com/your-user-name/REPONAME``.
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

.. _rebase-on-trunk:


Rebasing a Pull Request (PR)
============================

When working on a PR, changes may occur in the parent branch (usually master).
This can lead to conflict with changes in your branch. The conflicts can be
trivial: for example both the parent branch and your branch add an entry to
the top of `CHANGELOG`.  Git can not unambiguously tell what to do with both
changes (should one go above the other? if so, which order? should it try to
merge them?) so it declares the branches can not be merged
cleanly. GitHub can only automatically merge PR without conflicts, so you will
need to manually 'rebase'. This is the process of updating your branch with
upstream changes, and resolving conflicts.


To start your work you :ref:`update-mirror-trunk` and
:ref:`make-feature-branch` called ``cool-feature``. At this stage
trunk is at some commit, let's call it E. Now you make some new
commits on your ``cool-feature`` branch, let's call them A, B,
C.  Maybe your changes take a while, or you come back to them after a while.  In
the meantime, trunk has progressed from commit E to commit (say) G:

.. code-block:: none

          A---B---C cool-feature
         /
    D---E---F---G trunk

At this stage you consider merging trunk into your feature branch, and you
remember that this here page sternly advises you not to do that, because the
history will get messy. Most of the time you can just ask for a review, and not
worry that trunk has got a little ahead.  But sometimes, the changes in trunk
might affect your changes, and you need to harmonize them.  In this situation
you may prefer to do a rebase.

rebase takes your changes (A, B, C) and replays them as if they had been made to
the current state of ``trunk``.  In other words, in this case, it takes the
changes represented by A, B, C and replays them on top of G. After the rebase,
your history will look like this:

.. code-block:: none

                  A'--B'--C' cool-feature
                 /
    D---E---F---G trunk


In git, rebasing is a mild form of re-writing history: it effectively
forwards all your commits to the updated upstream commit. For a much
more detailed explanation (with pictures!) see `this nice write up
<https://git-scm.com/book/en/Git-Branching-Rebasing>` or See `rebase
without tears`_.  In general, re-writing history, particularly
published history, is considered bad practice, but in this case it is
very useful.

The following example assumes that the remote of _your_ GitHub
repository is called ``origin`` and the remote of the official
repository is called ``upstream``.

The first step is to make sure that your local copy of the upstream repository is
up-to-date::

     git fetch upstream

This updates your local copy of the repository, but does not change any files
in your working copy.  Next, switch to the branch that you want to update and make
a backup (just to be safe!).::

     git checkout cool-feature
     git branch tmp cool-feature

You are now ready to start the rebase of your branch onto the target
parent branch, in this case `matplotlib/master` ::

     git rebase upstream/master

If there are no conflicts git will print something like::

  First, rewinding head to replay your work on top of it...
  Applying: Allow tuples of 4 floats as color rcparams.
  Applying: Add a proper test for validate_color

and return without error.  In this case you can jump straight to :ref:`force_push`.

.. _handle_rebase_conflicts:

Handling rebase conflicts
-------------------------

If things can not be merged cleanly,  git will give a bunch of feed back::

     First, rewinding head to replay your work on top of it...
     Applying: first steps to extract FigureManager* and friends from pyplot
     Applying: split backend_qt4 into two parts, with and without Gcf
     ...
     Applying: pep8 clean up on backend_gtk3.py
     Using index info to reconstruct a base tree...
     M       lib/matplotlib/backends/backend_gtk3.py
     Falling back to patching base and 3-way merge...
     Auto-merging lib/matplotlib/backends/backend_gtk3.py
     CONFLICT (content): Merge conflict in lib/matplotlib/backends/backend_gtk3.py
     Failed to merge in the changes.
     Patch failed at 0013 pep8 clean up on backend_gtk3.py
     The copy of the patch that failed is found in:
        /home/tcaswell/other_source/matplotlib/.git/rebase-apply/patch

     When you have resolved this problem, run "git rebase --continue".
     If you prefer to skip this patch, run "git rebase --skip" instead.
     To check out the original branch and stop rebasing, run "git rebase --abort".

We see that a few commits could be cleanly applied to the tip of
``upstream/master``.  However, git  eventually hit a commit that
had conflicts: in the example above, this happens in the file
`lib/matplotlib/backends/backend_gtk3.py`).  For more verbose
information run ::

     git status

which should print something like ::

     You are currently rebasing branch 'backend_plt_refactor' on 'e6f8993'.
       (fix conflicts and then run "git rebase --continue")
       (use "git rebase --skip" to skip this patch)
       (use "git rebase --abort" to check out the original branch)

     Unmerged paths:
       (use "git reset HEAD <file>..." to unstage)
       (use "git add <file>..." to mark resolution)

             both modified:      lib/matplotlib/backends/backend_gtk3.py

     no changes added to commit (use "git add" and/or "git commit -a")

This tells you exactly where the conflict (caused by the target branch
and your commits modifying the same lines of code) is and provides
some advice on how to proceed.  Opening up the file in question, you
will see blocks that look something like this::

     <<<<<<< HEAD
     =======
             self.__dict__.clear()   # Is this needed? Other backends don't have it.
     >>>>>>> pep8 clean up on backend_gtk3.py

The block of code between `<<<<<<<` and `=======` is the code on the
target branch (in this case nothing) and the code between `=======`
and `>>>>>>>` is the code in the commit you are trying to rebase.  The
rest of the code is either the same or the diff can be unambiguously
applied.  You need to determine how to resolve the conflict (in this
case, the code on HEAD is correct).  Once you have resolved all the
conflicts, `add` the file to the index::

     git add lib/matplotlib/backends/backend_gtk3.py

Repeat this for all of the files that have conflicts.  When you are done with
that you can check the status::

     git status

which should print something like ::

     rebase in progress; onto e6f8993
     You are currently rebasing branch 'backend_plt_refactor' on 'e6f8993'.
       (all conflicts fixed: run "git rebase --continue")

     Changes to be committed:
       (use "git reset HEAD <file>..." to unstage)

             modified:   lib/matplotlib/backends/backend_gtk3.py

which shows us that we have resolved all of the conflicts with this
commit and can continue::

     git rebase --continue

You now iterate the until you have made it through all of the commits
which have conflicts.  Once you have successfully rebased your branch,
be sure to re-run the tests to make sure everything is still working
properly.

.. _recovering-from-mess-up:

Recovering from mess-ups
------------------------

Sometimes, you mess up merges or rebases. Luckily, in git it is
relatively straightforward to recover from such mistakes.

If you mess up during a rebase::

   git rebase --abort

If you notice you messed up after the rebase::

   # reset branch back to the saved point
   git reset --hard tmp

If you forgot to make a backup branch::

   # look at the reflog of the branch
   git reflog show cool-feature

   8630830 cool-feature@{0}: commit: BUG: io: close file handles immediately
   278dd2a cool-feature@{1}: rebase finished: refs/heads/my-feature-branch onto 11ee694744f2552d
   26aa21a cool-feature@{2}: commit: BUG: lib: make seek_gzip_factory not leak gzip obj
   ...

   # reset the branch to where it was before the botched rebase
   git reset --hard cool-feature@{2}


.. _force_push:

Force Push
----------

Your branch is now rebased, however, because of the way git
determines the hash of each commit, it now shares no commits with your
old branch published on GitHub so you can not push to that branch as
you would when simply adding commits.  In order to publish your newly
rebased (and tested!) branch you need to use the ``--force`` flag::

    git push --force origin

which will _replace_ all of the commits under your branch on GitHub
with the new versions of the commit.

Congratulations, you have rebased your branch!

You can now safely delete your backup branch::

   git branch -D tmp



Some other things you might want to do
======================================

Delete a branch on github
-------------------------

::

   git checkout master
   # delete branch locally
   git branch -D my-unwanted-branch
   # delete branch on GitHub
   git push origin :my-unwanted-branch

Note the colon ``:`` before ``my-unwanted-branch``.  See also:
https://help.github.com/articles/pushing-to-a-remote/#deleting-a-remote-branch-or-tag

Several people sharing a single repository
------------------------------------------

If you want to work on some stuff with other people, where you are all
committing into the same repository, or even the same branch, then just
share it via github.

First fork PROJECTNAME into your account, as from :ref:`forking`.

Then, go to your forked repository github page, say
``https://github.com/your-user-name/REPONAME``

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
-----------------------

To see a graphical representation of the repository branches and
commits::

   gitk --all

To see a linear list of commits for this branch::

   git log

You can also look at the `network graph visualizer`_ for your github
repo.

Finally the :ref:`fancy-log` ``lg`` alias will give you a reasonable text-based
graph of the repository.


.. _rewriting-commit-history:

Rewriting commit history
------------------------

.. note::

   Do this only for your own feature branches.

There's an embarrassing typo in a commit you made? Or perhaps the you
made several false starts you would like the posterity not to see.

This can be done via *interactive rebasing*.

Suppose that the commit history looks like this::

    git log --oneline
    eadc391 Fix some remaining bugs
    a815645 Modify it so that it works
    2dec1ac Fix a few bugs + disable
    13d7934 First implementation
    6ad92e5 * masked is now an instance of a new object, MaskedConstant
    29001ed Add pre-nep for a copule of structured_array_extensions.
    ...

and ``6ad92e5`` is the last commit in the ``cool-feature`` branch. Suppose we
want to make the following changes:

* Rewrite the commit message for ``13d7934`` to something more sensible.
* Combine the commits ``2dec1ac``, ``a815645``, ``eadc391`` into a single one.

We do as follows::

    # make a backup of the current state
    git branch tmp HEAD
    # interactive rebase
    git rebase -i 6ad92e5

This will open an editor with the following text in it::

    pick 13d7934 First implementation
    pick 2dec1ac Fix a few bugs + disable
    pick a815645 Modify it so that it works
    pick eadc391 Fix some remaining bugs

    # Rebase 6ad92e5..eadc391 onto 6ad92e5
    #
    # Commands:
    #  p, pick = use commit
    #  r, reword = use commit, but edit the commit message
    #  e, edit = use commit, but stop for amending
    #  s, squash = use commit, but meld into previous commit
    #  f, fixup = like "squash", but discard this commit's log message
    #
    # If you remove a line here THAT COMMIT WILL BE LOST.
    # However, if you remove everything, the rebase will be aborted.
    #

To achieve what we want, we will make the following changes to it::

    r 13d7934 First implementation
    pick 2dec1ac Fix a few bugs + disable
    f a815645 Modify it so that it works
    f eadc391 Fix some remaining bugs

This means that (i) we want to edit the commit message for
``13d7934``, and (ii) collapse the last three commits into one. Now we
save and quit the editor.

Git will then immediately bring up an editor for editing the commit
message. After revising it, we get the output::

    [detached HEAD 721fc64] FOO: First implementation
     2 files changed, 199 insertions(+), 66 deletions(-)
    [detached HEAD 0f22701] Fix a few bugs + disable
     1 files changed, 79 insertions(+), 61 deletions(-)
    Successfully rebased and updated refs/heads/my-feature-branch.

and the history looks now like this::

     0f22701 Fix a few bugs + disable
     721fc64 ENH: Sophisticated feature
     6ad92e5 * masked is now an instance of a new object, MaskedConstant

If it went wrong, recovery is again possible as explained :ref:`above
<recovering-from-mess-up>`.

.. include:: links.inc
