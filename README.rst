.. -*- rest -*-
.. vim:syntax=rst

=========
 Gitwash
=========

A set of documents and an example repository to describe starting with
github and a git workflow.

Our idea is that many projects may have the same workflow, more or less.
Each project needs docs that have exact project-specific command lines
for use with git and github.

It seems a shame to type all this out for every project, when a lot of
it is the same.

Gitwash is one way of solving this problem.

* You can build the gitwash documents directly to review your workflow.
* The documents designed for re-use in different projects are in the
  ``gitwash`` subdirectory.
* In these documents, we've encoded the various strings you will want to
  replace with strings in ALL CAPS.  The ``PROJECTNAME`` is the name of
  the project as it appears in text - for example ``IPython``.
  ``REPONAME`` is the name of the repository (e.g ``ipython``), and
  ``MAIN_GH_USER`` is the main github user (the user for the central
  github repository - or the name of the github "organization").  This
  results in links to your project repository of the form
  ``github.com/MAIN_GH_USER/REPONAME.git``.
* The script ``gitwash_dumper.py`` will checkout the gitwash repository,
  do a search and replace on these strings and replace them with the
  ones you want, and then output these into your own docs in a place
  that you choose. You might want a copy of this tool somewhere in your
  repository.  You can refresh it from time time with::

    curl -O https://raw.github.com/matthew-brett/gitwash/master/gitwash_dumper.py

  For IPython, ``PROJECTNAME`` is 'IPython', ``REPONAME`` is 'ipython', and the
  ``MAIN_GH_USER`` is also 'ipython'.  An example command for *ipython* might
  then be::

     gitwash_dumper.py doc/devel IPython --repo-name=ipython --github-user=ipython \
        --project-url=http://ipython.scipy.org \
        --project-ml-url=http://mail.scipy.org/mailman/listinfo/IPython-dev

  to dump the search / replaced docs into the ``doc/devel/gitwash``
  directory.
* In the command above you'll notice that you also have to add your project main
  URL with the ``--project-url`` option, and the mailing list URL with the
  ``--project-ml-url`` option.  That is the standard way to add your own links
  into the documentation.
* You might want to have a Makefile target to update gitwash
  automatically from the sources.  For example, in the *nipy* docs
  Makefile, we have::

     gitwash-update:
        python ../tools/gitwash_dumper.py devel/guidelines nipy \
            --project-url=http://nipy.org \
            --project-ml-url=http://mail.scipy.org/mailman/listinfo/nipy-devel

There's an example build of gitwash at
http://matthew-brett.github.com/pydagogue/gitwash_build.html

