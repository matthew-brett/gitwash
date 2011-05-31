.. _maintainer-workflow:

###################
Maintainer workflow
###################

This page is for maintainers |emdash| those of us who merge our own or other
peoples changes into the upstream repository.

Being as how you're a maintainer, you are completely on top of the basic stuff
in :ref:`development-workflow`.

The instructions in :ref:`linking-to-upstream` add a remote that has read-only
access to the upstream repo.  Being a maintainer, you've got read-write access.

It can help to remind you of this, if you add a remote link, for read-write,
with a scary name, like this::

    git remote add upstream-rw git@github.com:MAIN_GH_USER/REPONAME.git
    git fetch upstream-rw

*******************
Integrating changes
*******************

Let's say you have some changes that need to go into trunk
(``upstream-rw/master``).

The changes are in some branch that you are currently on.  For example, you are
looking at someone's changes like this::

    git remote add someone git://github.com/someone/REPONAME.git
    git fetch someone
    git branch cool-feature --track someone/cool-feature
    git checkout cool-feature

Specifically, you are on the branch with the changes you want to push upstream.

If there are only a few commits, consider rebasing to upstream::

    # Fetch upstream changes
    git fetch upstream-rw
    # rebase
    git rebase upstream-rw/master

Remember that, if you do a rebase, and push that, you'll have to close any
github pull requests manually, because github will not be able to detect the
changes have already been merged.

If there are a longer series of related commits, consider a merge instead::

    git fetch upstream-rw
    git merge --no-ff upstream-rw/master

The merge will be detected by github, and should close any related pull requests
automatically.

Note the ``--no-ff`` above.  This forces git to make a merge commit, rather than
doing a fast-forward, so that these set of commits stay in their own series of
commits, and then join the main history with a merge, rather than appearing to
have been made directly on top of the trunk.

Now, in either case::

    # Recheck that what is there is sensible
    git log --oneline --graph
    git log -p upstream-rw/master..

Finally, push branch to trunk::

    git push upstream-rw my-new-feature:master

.. include:: links.inc
