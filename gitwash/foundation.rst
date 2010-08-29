.. _git-foundation:

===============
Git foundations
===============

"Foundations" is a little joke on a religous theme; our page borrows heavily
from the `git parable`_ - so - why not a foundation myth?

In the beginning was the working tree
=====================================

The *working tree* has all the files in my project.  If this was a tiny python
project, it might look a little like this::

    .
    ├── README
    ├── setup.py
    └── tinyproject
        ├── __init__.py
        └── tinymodule.py

On the first day - the repository and the working tree
======================================================

I decide that I want to keep track of my changes.  So, at the end of the day,
I make an archive containing all the files in the working tree, and save it
somewhere.  To make things nice and neat, I'll save it in a subdirectory called
``.versions``.  On unix, this might look something like::

    tar cvf .versions/2010-08-28.tar.gz *

So now, I've got my code in the working tree, and an archive that is a snapshot
of the code as of today::

    .
    ├── .versions
    │   └── 2010-08-28.tar.gz
    ├── README
    ├── setup.py
    └── tinyproject
        ├── __init__.py
        └── tinymodule.py

I decide to use the name *repository* for the contents of the ``.version``
directory.

On the second day - commits
===========================

I do some more work.   I save it into the repository, at the end of the day::

    .
    ├── .versions
    │   ├── 2010-08-28.tar.gz
    │   └── 2010-08-29.tar.gz
    ├── README
    ├── setup.py
    └── tinyproject
        ├── __init__.py
        └── tinymodule.py

I decide that I'll use the name *commit* for each of the archives.  The action
of making the archive, I will call *commiting*. 

On the third day - history
==========================

I have a new friend, Eve.  She wants to help out.  Of course Eve has her own
computer, and I send her the ``.versions`` directory.  She checks out my
code (reconstructs my working tree) with something like::

   tar zxf .versions/2010-08-29.tar.gz

and now she's got the same working tree as me.  She does some fine work.  At
the end of the day, she backs up the same way I do::

    tar cvf .versions/2010-08-30.tar.gz *

but Eve is smart, and she immediately realizes that both of us will have a
commit file ``.versions/2010-08-30.tar.gz`` - but they will be different.   The
two of us are a little tired after all our work, and we meet for a beer.
After talking it through, we decide to change the way we name our commits,
from using the date, to using some unique random number.  So now, my
repository will look like this::

    ├── .versions
    │   ├── 37445.tar.gz
    │   ├── 44586.tar.gz
    │   └── 66374.tar.gz

and Eve's will look like this::

    ├── .versions
    │   ├── 37445.tar.gz
    │   ├── 44586.tar.gz
    │   └── 79272.tar.gz

where ``66374.tar.gz`` was my working tree as of today, and ``79272.tar.gz`` is
Eve's.  We immediately realize that we're going to run into trouble though,
because previously, we had the date to tell us the order of the commits. Now,
we've just got a random number, so we need some way to store the commit
sequence.  We decide to modify the nature of the stored commit.   What we will
do is make the commit be the combination of 1) the files in the working
directory and also 2) some information about the commit, like the date, who did
it, and what the previous commit was.  The information about the previous commit
will tell us the commit sequence. So, when we make a commit, it's going to look
a little bit like this::

   tar cvf files.tar.gz *
   
then we make a text file called ``info.txt`` that looks like this::

   Committer = 'Adam'
   Date = '2010-08-30'
   Parent = '22586'
   Message = 'Some useful work I did on the third day'

and we make a new unique random number - let's say it turns out to be '66374'.
Then we make the commit like this::

   tar cvf .version/66374.tar.gz files.tar.gz info.txt

After a little thought, Eve and I realize that, when we make our new commit, we
are going to have to know what the current commit is, so we can use that as the
parent of the new commit.  So, when we make a new commit, we store the commit
number in a file.  We'll call this file ``.versions/HEAD``, so, after the commit
above, the file ``.versions/HEAD`` will have the contents ``66374``. So,
``.versions/HEAD`` identifies the last (current) commit.  And of course, when we
make a new commit, we can get the parent of the new commit, from the current
commit in ``.versions/HEAD``. And then, when we want to go back to an earlier
state of the code, we can do a *checkout*, by::

   tar zxf .versions/44586.tar.gz
   tar zxf files.tar.gz 
   rm files.tar.gz

and then we just put '44586' into ``.versions/HEAD``. 

In our excitement, we immediately realize that it's really easy to see the
history of the code now.  We can easily fetch out ``info.txt`` from the current
commit, print it, then find its parent, and fetch ``info.txt`` from the parent,
print it, and so on.

Now we are tired, but happy, and we rest.

On the fourth day - references
==============================

We wake with a strange excitement.  The idea, of keeping a reference to the
current commit in ``.versions/HEAD``, seems that it could be more general.  I
talk to Eve over breakfast (she stayed in her own place of course, but she came
over for work).  Together we work out the concept of *references*. A reference
is:

Reference
    Something that points to a commit

So, ``.versions/HEAD`` is a reference - the current commit.  But what if I
decide that I want to do a release of some code?  Let's say I want to release
the code in ``.versions/44586.tar.gz`` as 'release-0.1'.   I'm going to send
this out to all my friends (to be honest, I don't have many friends just yet,
but still).  I want to be able to remember what version of the code I sent out.
I can make a *reference* to this commit.  I'll call this a *tag*.   I make a new
directory in ``.versions`` called ``refs``, and another directory in ``refs``,
called ``tags``, and then, in ``.versions/refs/tags/release-0.1`` I just put
'44586' - a reference to the release commit.   That way, if I ever need to go
back to the code I released, I just have to read the ``release-0.1`` file to
find the commit, and then checkout that commit. 

Wait, but, there's a problem.  If I checkout the commit in ``release-0.1``, I
will overwrite ``.versions/HEAD``, and I will lose track of what commit I was
working on before.

Let's store that in another reference.  Let's use the name 'master' for my main
line of development.  I store where this is, by making a new file
``.versions/refs/heads/master`` that is a reference to the last commit.  It just
contains the text '66374'.  So that I know that I am working on 'master', I make
``.versions/HEAD`` have the text ``ref: refs/heads/master``.  Now, when I make a
new commit, I check ``.versions/HEAD``, see that I'm working on 'master', then I
make a new commit in the usual way.  Specifically, I make a new random number -
say '41607' and make the ``info.txt`` file, and then::

   tar cvf files.tar.gz *
   tar cvf .version/41607.tar.gz files.tar.gz info.txt

Finally, I update ``.versions/refs/heads/master`` to contain ``41607``.  That
way, we keep track of which commit we are on, by constantly updating 'master'.

Ok - now let's return to me checking out the release code.  I first get the
contents of ``.versions/refs/tags/release-0.1`` - it's '66374'.  Then I checkout
the working tree for that code::

   tar zxf .versions/66374.tar.gz
   tar zxf files.tar.gz 
   rm files.tar.gz

Then I make ``.versions/HEAD`` contain the text ``66374``.  

Why don't I put ``ref: refs/tags/release-0.1`` into ``.versions/HEAD``?
Because, if I do a commit, I don't want to update ``refs/tags/release-0.1``.
``release-0.1`` contains the exact commit I released - I need to know it was
that one, even if I do more development on top of it.  So, to prevent the tag
getting changed, I just make ``.versions/HEAD`` have a commit number [#detached]_ .

Now I want to go back to working on my current code.   I check the contents of
``.versions/refs/heads/master`` - it is ``41607``.  Then I get the code::

   tar zxf .versions/41607.tar.gz
   tar zxf files.tar.gz 
   rm files.tar.gz

Then I set ``.versions/HEAD`` to be ``ref: refs/heads/master``.   Off I go.

What then, is the difference, between a *tag* - like our release - and the
moving target like 'master'?  The 'tag' is a *static* reference - it does not
change when we do a commit and always points to the same commit.  'master' is a
dynamic reference - in particular, it's a *head* reference:

Head
    A head is a reference that updates when we do a commit

My head is hurting a little, after Eve explains all this, but after a little
while and a nice apple pie, I'm feeling positive about this ``version`` we're
making.

On the fifth day - branches
===========================

Yesterday was a little exhausting, so today there was some time for reflection.

As Eve and I relax with the other animals, who are all getting on very well with
each other, we begin to realize that this *head* thing could be very useful.

For example, what if one of my very small number of friends tells me that
there's a problem with the code I released - ``release-0.1``?  What if I want to
go back and fix it - that is - do another commit on top of the *released* code,
instead of the code I'm currently working on?  I can just make a new *head*.
I'll do it like this::

   cp .versions/refs/tags/release-0.1 .versions/refs/heads/working-on-0.1

Then, I look at what commit ``working-on-0.1`` contains - of course it's
``44586``.  I get the code::

   tar zxf .versions/44586.tar.gz
   tar zxf files.tar.gz 
   rm files.tar.gz

and I set ``.versions/HEAD`` to be ``ref: refs/heads/working-on-0.1``.  Now,
when I do a commit, I'll update the file ``.versions/refs/heads/working-on-0.1``
to have the new commit number.  And off I go.

As we think about this, we come to think of 'master' and 'working-on-0.1' as
*branches* - because they can each be thought of as identifying a tree or graph
of commits, which can grow.  All I need to do, to make a new branch, is make a
new head reference to a commit.  For example, if I want to make new branch
starting at the current position of 'master', all I need to do is::

   cp .versions/refs/tags/master .versions/refs/heads/my-new-branch

Of course, then, if I want to work on this branch, I need to check it out, by
getting the commit number in ``.versions/refs/heads/my-new-branch``, unpacking
the commit tree into the working tree, and setting ``.versions/HEAD`` to contain the text ``ref:
refs/heads/my-new-branch``


On the sixth day - remotes
==========================

Eve and I are getting on well, but now she's asking me if I can have a look at
her changes, and whether I'll include them in my version of the code.  Luckily,
despite the lack of basics like clothing, there is an excellent local network,
so I can see the contents of her version of the code at
``/eves_computer/our_project/.versions``.  She wants me to look at her 'master'
branch.  Just because the network might fail, I need to fetch what I need from
her computer to mine.  So, to keep track of things, I'll make a new directory,
called ``.versions/refs/remotes/eve``, and I'll copy all her *heads* - in this
case just ``master`` - to that directory.   So now, I've got
``.versions/refs/remotes/eve/master``, and in fact, it points to the commit that
she did on the third day - and this was commit '79272'.  I don't have this
commit in my ``.versions`` directory, so I'll copy that from
``/eves_computer/our_project/.versions/79272.tar.gz``.  I look in the
``info.txt`` file for that commit, and check what the parent is.  It is '44586'.
I check if I have that, and yes, I have, so I can stop copying stuff from Eve's
directory.

So, what I just did was:

* Copy Eve's *head* references from
  ``/eves_computer/our_project/.versions/refs/heads`` to my
  ``.versions/refs/remotes/eve``. 
* For each of the references in ``.versions/refs/remotes/eve``, I check whether
  I have the referenced commit, and the parents of that commit, and, if not, I
  copy them to ``.versions``.

We decide to call that two-step sequence - a *fetch*. 

Now I want to look at her code.  I can just check it out of course.  I first get
the commit number from ``.versions/refs/remotes/eve/master`` - '79272'.  Then::

   tar zxf .versions/79272.tar.gz
   tar zxf files.tar.gz 
   rm files.tar.gz

and I put '79272' into ``.versions/HEAD``.  I can look at her code, and decide
if I like it.  If I do, then I can do a *merge*.  What's a merge?  It's the join
of two commits.  First I work out where Eve's tree diverged from mine, by going
back in her history, following the parents of the commits.  In this case it's
easy, because the parent commit ('44586') of this commit ('79272') is one that
is also in my history (the history for my 'master' branch).  Then I work out the
difference between the last shared commit ('44586') and this commit ('79272') -
let's call that ``eves_diff``.  

I go back to my own 'master' - which turns out to be
(``.versions/refs/heads/master``) - '41607'::

   tar zxf .versions/41607.tar.gz
   tar zxf files.tar.gz 
   rm files.tar.gz
   
and change ``.versions/HEAD`` to be ``ref: refs/heads/master``.  Then I take
``eves_diff`` and apply it to my current working tree.  If there were any
conflicts, I resolve them, but in my world, there are no conflicts.  I have a
feeling there may be some later.   That apple pie is making me feel a little
funny.  

Finally, I make a new commit, with a new random number - '64128', with the
merged working tree.  But, there's a trick: here the new commit '64128' - has
*two* parents, first - '41607' - the previous commit in my 'master', and second
'79272' - the last commit in Eve's master.  Now, the next time I look at Eve's
tree, I will be able to see that I've got her '79272' commit in my own history,
and won't need to apply it again.

On the seventh day - there was git
==================================

OK - so you knew it all the time.  We were talking about git_.  In git_, it's a
little more complicated, but not much.  The *repository* is stored in the
``.git`` directory, rather than the ``.versions`` directory.  To save space, and
because it makes diffs easier, the commits are not archives of whole working
trees, but differences between the previous working tree and the new working
tree.

But basically - you can imagine, that if you wrapped up our crude checkout into
something nice like::

    git checkout master

Then that could go and find out what commit is in ``refs/heads/master``, and
reconstruct that into the working tree.

And as for the rest - well - maybe it's obvious!  Or maybe I need to write a
little more, before the flaming sword starts to wave over the entrance to my
little plot of land.


.. include:: git_links.inc

.. rubric:: Footnotes

.. [#detached] In git, this is a 'detached HEAD'

