.. _follower-to-developer:

==================================================
 Changing from following the code, to development
==================================================

This is to deal with the situation where you started just
:ref:`following-latest` but then found that you would like to publish
some changes that you've made, therefore making your |reponame| friends
happy.

First, make your own github_ copy of the repository to work in, by :ref:`forking`. 

Next, you want to do a final update on your local repository:

#. |repo-cd|
#. ``git pull``

Now, you want to point your local repository at your new forked
repository, as well as maintaining the link with the mainline |reponame|
repository.   To do this:

#. ``git remote rm origin`` - remove the link to the mainline repository
#. |repo-add-fork| - add read-write link to your forked copy
#. |repo-add-remote| - add back read-only link to the mainline |repourl| repository

Now you can follow the workflow in :ref:`development-workflow`.

.. include:: links_names.txt
.. include:: substitutions.txt



