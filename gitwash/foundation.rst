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

I decide that I want to keep track of my changes.  Because I currently lack any
shame about body issues, I will call my new versioning system ``ahole``.

I decide that what I need to do is store the state of my code at the end of each
day.  Do do this, I make a new directory in my working tree, called ``.ahole``,
to store the previous state of my code.  

At the end of the day, I make an archive containing all the files in the working
tree, and save it in ``.ahole``.  In fact, what I will do is, make a new
subdirectory in ``.ahole`` named for today's date, then store an archive of the
code in there.  On unix, that might look like this::

    mkdir .ahole/year0-jan-01
    zip -r .ahole/year0-jan-01/files.zip *

So now, I've got my code in the working tree, and an archive that is a snapshot
of the code as of today::

    .
    ├── .ahole
    │   └── year0-jan-01
    │       └── files.zip
    ├── README
    ├── setup.py
    └── tinyproject
        ├── __init__.py
        └── tinymodule.py
    
I decide to use the name *repository* for the contents of the ``.ahole``
directory.

On the second day - commits
===========================

I do some more work.   I save it into the repository, at the end of the day::

    .
    ├── .ahole
    │   ├── year0-jan-02
    │   │   └── files.zip
    │   └── year0-jan-01
    │       └── files.zip
    ├── README
    ├── setup.py
    └── tinyproject
        ├── __init__.py
        └── tinymodule.py

I decide that I'll use the name *commit* for each of the archive directories.  The action
of making the archive, I will call *commiting*. 

On the third day - history
==========================

I have a new friend, Eve.  She wants to help out.  Of course Eve has her own
computer, and I send her my ``.ahole`` directory.  She checks out my
code (reconstructs my working tree) with something like::

    unzip .ahole/year0-jan-02/files.zip

and now she's got the same working tree as me.  She does some fine work.  At
the end of the day, she commits her changes the same way I do::

    mkdir .ahole/year0-jan-03
    zip -r .ahole/year0-jan-03/files.zip *

but Eve is smart, and she immediately realizes that both of us will have a
commit directory ``.ahole/year0-jan-03`` - but they will have different
contents.   If she later wants to share work with me, that could get confusing.

The two of us are a little tired after all our work, and we meet for a beer.  We
talk about it for a while.  At first we think we can just add the time to the
date, because that's likely to be unique for each of us.  Then we realize that
that's going to get messy too, because, if Eve does a commit on her computer,
then I do a commit on mine, and she does another one on hers, the times will say
that these are all in one sequence, but in fact there are two sequences, mine,
and Eves.  We need some other way to keep track of the sequence of commits, that
will work even if two of us are working independently.   

In the end we decide that we are going to give the commits some unique identifer
string instead of the date.   We'll store the contents of the working tree in
the same way, as ``files.zip``, but we'll add a new file to each commit, called
``info.txt`` that will tell us who did the commit, and when, and, most
importantly, what the previous commit was.  We'll call the previous commit the
*parent*.  

Before our conversation, my directory looked like this::

    .
    ├── .ahole
    │   ├── year0-jan-03
    │   │   └── files.zip
    │   ├── year0-jan-02
    │   │   └── files.zip
    │   └── year0-jan-01
    │       └── files.zip
    ├── setup.py
    ├── README
    └── tinyproject
        ├── __init__.py
        └── tinymodule.py

but now we've worked out the new way, it looks like this::

    .
    ├── .ahole
    │   ├── 5d89f8
    │   │   ├── info.txt
    │   │   └── files.zip
    │   ├── 7ef41f
    │   │   ├── info.txt
    │   │   └── files.zip
    │   └── 6438a4
    │       ├── info.txt
    │       └── files.zip
    ├── setup.py
    ├── README
    └── tinyproject
        ├── __init__.py
        └── tinymodule.py

and ``.ahole/5d89f8/info.txt`` looks like this::

    committer = Adam
    date = year0-jan-03
    parent = 7ef41f
    message = Third day

Meanwhile, Eve's directory looks like this::

    .
    ├── .ahole
    │   ├── 0a01a0
    │   │   ├── info.txt
    │   │   └── files.zip
    │   ├── 7ef41f
    │   │   ├── info.txt
    │   │   └── files.zip
    │   └── 6438a4
    │       ├── info.txt
    │       └── files.zip
    ├── README
    ├── setup.py
    └── tinyproject
        ├── __init__.py
        └── tinymodule.py

and Eve's ``.ahole/0a01a0/info.txt`` looks like this::

    committer = Eve
    date = year0-jan-03
    parent = 7ef41f
    message = Eve day 3

After a little thought, Eve and I realize that, when we make our new commit, we
are going to have to know what the current commit is, so we can use that as the
parent of the new commit.  So, when we make a new commit, we store the commit
identifier in a file.  We'll call this file ``.ahole/HEAD``, so, after my last commit
above, the file ``.ahole/HEAD`` will have the contents ``5d89f8``. So,
``.ahole/HEAD`` identifies the last (current) commit.  And of course, when we
make a new commit, we can get the parent of the new commit, from the current
commit in ``.ahole/HEAD``. 

So now, we have a new procedure for our commit.  In outline it looks like this::

   def ahole_commit(message):
       # make unique identifier for this commit => UID
       # Make a directory with name UID in '.ahole' => .ahole/$UID
       # Make an archive of the current working tree in .ahole/$UID/files.zip
       # Get previous (parent) commit id from .ahole/HEAD => HEAD
       # Make .ahole/$UID/info.txt with parent set to HEAD
       # Set .ahole/HEAD to contain UID

And then, when we want to go back to an earlier state of the code, we can do a
*checkout*, with something like::

   def ahole_checkout(commit_id):
      # clear the current working tree
      # unpack .ahole/$commit_id/files.zip into working tree
      # make .ahole/HEAD contain $commit_id

So, when we run ``ahole_checkout('7ef41f`)`` we will get the copy of the working
tree corresponging to ``7ef41f``, and ``.ahole/HEAD`` will just contain the
string ``7ef41f``. 

In our excitement, we immediately realize that it's really easy to see the
history of the code now.  We can easily fetch out ``info.txt`` from the current
commit, print it, then find its parent, and fetch ``info.txt`` from the parent,
print it, and so on.

Now we are tired, but happy, and we rest.

On the fourth day - references
==============================

We wake with a strange excitement.  The idea, of keeping a reference to the
current commit in ``.ahole/HEAD``, seems that it could be more general.  I
talk to Eve over breakfast (she stayed in her own place of course, but she came
over for work).  Together we work out the concept of *references*. A reference
is:

Reference
    Something that points to a commit

So, ``.ahole/HEAD`` is a reference - the current commit.  But what if I
decide that I want to do a release of some code?  Let's say I want to release
the code in ``.ahole/7ef41f/files.zip`` as 'release-0.1'.   I'm going to send
this out to all my friends (to be honest, I don't have many friends just yet,
but still).  I want to be able to remember what version of the code I sent out.
I can make a *reference* to this commit.  I'll call this a *tag*.   I make a new
directory in ``.ahole`` called ``refs``, and another directory in ``refs``,
called ``tags``, and then, in ``.ahole/refs/tags/release-0.1`` I just put
'7ef41f' - a reference to the release commit.   That way, if I ever need to go
back to the code I released, I just have to read the ``release-0.1`` file to
find the commit, and then checkout that commit. 

Wait, but, there's a problem.  If I checkout the commit in ``release-0.1``, I
will overwrite ``.ahole/HEAD``, and I will lose track of what commit I was
working on before.

Let's store that in another reference.  Let's use the name 'master' for my main
line of development.  I store where this is, by making a new file
``.ahole/refs/heads/master`` that is a reference to the last commit.  It just
contains the text '5d89f8'.  So that I know that I am working on 'master', I
make ``.ahole/HEAD`` have the text ``ref: refs/heads/master``.  Now, when I make
a new commit, I first check ``.ahole/HEAD``; if I see ``ref:
refs/heads/master``, then first, I get the commit id in
``.ahole/refs/heads/master`` - and I use that as the parent id for the commit.
When I've save the new commit, I set ``.ahole/refs/heads/master`` to have the
new commit id.  So, I need to modify my commit procedure slightly::

   def ahole_commit(message):
       # make unique identifier for this commit => UID
       # Make a directory with name UID in '.ahole' => .ahole/$UID
       # Make an archive of the current working tree in .ahole/$UID/files.zip
       # Check if .ahole/HEAD begins with 'ref: refs/head'
       # If Yes: read parent ID from file pointed to by .ahole/HEAD -> HEAD_ID 
       #    Make .ahole/$UID/info.txt with parent set to HEAD_ID
       #    Replace text in reference file with UID
       # If No: Get previous (parent) commit id from .ahole/HEAD => HEAD_ID
       #    Make .ahole/$UID/info.txt with parent set to HEAD_ID
       #    Set .ahole/HEAD to contain UID

So, let's say that I'm currently on commit '5d89f8'.  ``.ahole/HEAD`` contains
``ref: refs/heads/master``.  ``.ahole/refs/heads/master`` contains ``5d89f8``.
I run my commit procedure::

   ahole_commit('Night follows day')

The commit prodedure has made a new commit 'dfbeda'; ``.ahole/HEAD`` continues
to have text ``ref: refs/heads/master``, but now ``.ahole/refs/heads/master``
contains ``dfbeda``.  In this way, we keep track of which commit we are on, by
constantly updating 'master'.

Ok - now let's return to me checking out the release code.  I first get the
contents of ``.ahole/refs/tags/release-0.1`` - it's '5d89f8'.  Then I checkout
the working tree for that code, using my nice ``ahole_checkout`` procedure::

    ahole_checkout('5d89f8')

The checkout procedure will make ``.ahole/HEAD`` contain the text ``5d89f8``.  

Now I want to go back to working on my current code.  That's the code pointed to
by ``.ahole/refs/heads/master``.  Of course, I can I check the contents of
``.ahole/refs/heads/master`` - it is ``dfbeda``.  Then I get the code with my
normal checkout procedure::

    ahole_checkout('dfbeda')

Finally, I'll have to set ``.ahole/HEAD`` to be ``ref: refs/heads/master``.  All
good.

Of course, I could automate this, by modifying my checkout procedure slightly::

   def ahole_checkout(refspec):
      # If $refspec is a file in .ahole/refs/heads then:
      #    # This is a reference
      #    Get commit ID from .ahole/refs/heads/$refspec -> UID
      # Else
      #    # This is a bare ID string
      #    Set $refspec -> UID 
      # clear the current working tree
      # unpack .ahole/$UID/files.zip into working tree
      # If $refspec was a reference:
      #    write ``ref: refs/heads/$refspec`` into .ahole/HEAD
      # else: # just a bare ID passed   
      #    make .ahole/HEAD contain $commit_id

What then, is the difference, between a *tag* - like our release - and the
moving target like 'master'?  The 'tag' is a *static* reference - it does not
change when we do a commit and always points to the same commit.  'master' is a
dynamic reference - in particular, it's a *head* reference:

Head
    A head is a reference that updates when we do a commit

My head is hurting a little, after Eve explains all this, but after a little
while and a nice apple pie, I'm feeling positive about ``ahole``.

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

   cp .ahole/refs/tags/release-0.1 .ahole/refs/heads/working-on-0.1

Then, I look at what commit ``working-on-0.1`` contains - of course it's
``7ef41f``.  I get the code with my new checkout procedure::

    ahole_checkout('working-on-0.1')

This changes ``.ahole/HEAD`` to be ``ref: refs/heads/working-on-0.1``.  Now,
when I do a commit with ``ahole_commit``,  that will update the file
``.ahole/refs/heads/working-on-0.1`` to have the new commit identifier.  Despite the
apple pie being a bit bitter last night, we're feeling good.

As we think about this, we come to think of 'master' and 'working-on-0.1' as
*branches* - because they can each be thought of as identifying a tree or graph
of commits, which can grow.  All I need to do, to make a new branch, is make a
new head reference to a commit.  For example, if I want to make new branch
starting at the current position of 'master', all I need to do is::

   cp .ahole/refs/tags/master .ahole/refs/heads/my-new-branch

Of course, then, if I want to work on this branch, I need to check it out,
with::

    ahole_checkout('my-new-branch')

That will get the commit identifier in ``.ahole/refs/heads/my-new-branch``, unpack
the commit tree into the working tree, and set ``.ahole/HEAD`` to contain the
text ``ref: refs/heads/my-new-branch``


On the sixth day - remotes
==========================

Eve and I are getting on well, but now she's asking me if I can have a look at
her changes, and whether I'll include them in my version of the code.  Luckily,
despite the lack of basics like clothing, there is an excellent local network,
so I can see the contents of her version of the code at
``/eves_computer/our_project/.ahole``.  She wants me to look at her 'master'
branch.  Just because the network might fail, I need to fetch what I need from
her computer to mine.  So, to keep track of things, I'll make a new directory,
called ``.ahole/refs/remotes/eve``, and I'll copy all her *heads* - in this
case just ``master`` - to that directory.   So now, I've got
``.ahole/refs/remotes/eve/master``, and in fact, it points to the commit that
she did on the third day - and this was commit '0a01a0'.  I don't have this
commit in my ``.ahole`` directory, so I'll copy that from
``/eves_computer/our_project/.ahole/0a01a0``.  I look in the
``info.txt`` file for that commit, and check what the parent is.  It is '7ef41f'.
I check if I have that, and yes, I have, so I can stop copying stuff from Eve's
directory.

So, what I just did was:

* Copy Eve's *head* references from
  ``/eves_computer/our_project/.ahole/refs/heads`` to my
  ``.ahole/refs/remotes/eve``. 
* For each of the references in ``.ahole/refs/remotes/eve``, I check whether
  I have the referenced commit, and the parents of that commit, and, if not, I
  copy them to ``.ahole``.

We decide to call that two-step sequence - a *fetch*. 

Now I want to look at her code.  I can just check it out of course.  I first get
the commit identifier from ``.ahole/refs/remotes/eve/master`` - '0a01a0'.
Then::

    ahole_checkout('0a01a0')

This will put '0a01a0' into ``.ahole/HEAD``.  I can look at her code, and decide
if I like it.  If I do, then I can do a *merge*.  What's a merge?  It's the join
of two commits.  First I work out where Eve's tree diverged from mine, by going
back in her history, following the parents of the commits.  In this case it's
easy, because the parent commit ('7ef41f') of this commit ('0a01a0') is one that
is also in my history (the history for my 'master' branch).  Then I work out the
difference between the last shared commit ('7ef41f') and this commit ('0a01a0')
- let's call that ``eves_diff``.  

I go back to my own 'master' - which turns out to be
(``.ahole/refs/heads/master``) - 'dfbeda'::

    ahole_checkout('master')
   
This will change ``.ahole/HEAD`` to be ``ref: refs/heads/master`` - and I will
have just got the working tree from ``.ahole/dfbeda/files.zip``.  Then I take
``eves_diff`` and apply it to my current working tree.  If there were any
conflicts, I resolve them, but in my world, there are no conflicts.  I have a
feeling there may be some later.   That apple pie is making me feel a little
funny.  

Finally, I make a new commit, with a new unique ID - say '80cc85', with the
merged working tree.  But, there's a trick: here the new commit '80cc85' - has
*two* parents, first - 'dfbeda' - the previous commit in my 'master', and second
'0a01a0' - the last commit in Eve's master.  Now, the next time I look at Eve's
tree, I will be able to see that I've got her '0a01a0' commit in my own history,
and won't need to apply it again.

On the seventh day - there was git
==================================

OK - so you knew it all the time.  We were talking about git_.  In git_, it's a
little more complicated, but not much.  The *repository* is stored in the
``.git`` directory, rather than the ``.ahole`` directory.  To save space, and
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
