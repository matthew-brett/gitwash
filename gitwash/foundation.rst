.. _git-foundation:

===============
Git foundations
===============

"Foundations" is a little joke on a religous theme; our page borrows heavily
from the `git parable`_ - so - why not a foundation myth?

In the beginning was the working tree
=====================================

The *working tree* has all the files in my project.  The project I am working on
is a modest history and explanation of everything, with provisional title "the
book".  It has a table of contents ``contents.txt`` and a single book chapter::

    .
    ├── chapter1.txt
    └── contents.txt

On the first day - the repository and the working tree
======================================================

I decide that I want to keep track of my changes.  Because I currently lack any
shame about body issues, I will call my new versioning system ``ahole`` [1]_ .

I decide that what I need to do is store the state of my book at the end of each
day.  To do this, I make a new directory in my working tree, called ``.ahole``,
to store previous states of my book.  

At the end of the day, I make an archive containing all the files in the working
tree, and save it in my new ``.ahole``.  In fact, what I will do is, make a new
subdirectory in ``.ahole`` named for today's date, then store a copy of the
book files in there.  On unix, that might look like this::

    mkdir .ahole/year0-jan-01
    mkdir .ahole/year0-jan-01/files
    cp * .ahole/year0-jan-01/files 

So now, I've got my book in the working tree, and copy of the files that is a
snapshot of the book as of today::

    .
    ├── .ahole
    │   └── year0-jan-01
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt
    ├── chapter1.txt
    └── contents.txt
    
I decide to use the name *repository* for the contents of the ``.ahole``
directory.

On the second day - adding, staging, commits
============================================

Today I do some more work on the book.   I start work on chapter 3, and, while
I'm thinking about things, I decide to write some notes to myself about this
character "Eve" that I have seen wandering around.  I call those notes
``something_about_eve.txt``.  When I get to the end of the day, I start thinking
about storing my work.  At the moment, my directory looks like this::

    .
    ├── .ahole
    │   └── year0-jan-01
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt
    ├── something_about_eve.txt
    ├── chapter2.txt
    ├── chapter1.txt
    └── contents.txt

Two thoughts come to me.  The first is, that for some reason I can't put my
finger on, I don't want to put ``something_about_eve.txt`` into the repository
at the moment.  The other thought was that this book could get very big and
take a very long time to write.  If I have to copy the whole working
directory into the repository every day, the repository could get very large.
I wonder if I should just store the things that are different from yesterday.

I think about this for a while.  In the end I come up with an idea.  I'll make a
directory in ``.ahole`` called ``index``.  When I get to the end of the day,
I'll first go into the ``index`` directory, and make links to all the files fron
yesterday, like this::

    ├── .ahole
    │   ├─── index
    │   │    ├── chapter1.txt (link to ../year0-jan-01/files/chapter1.txt)
    │   │    └── contents.txt (link to ../year0-jan-01/files/contents.txt)
    │   └── year0-jan-01
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt


Of course, because these are links, they don't take up extra space on the disk.

Then, I decide what I want to back up.   Maybe I have changed chapter 1, so I
delete the link to ``chapter1.txt`` in ``index``, and copy ``chapter1.txt`` from
the working directory to ``index``.  I'll call that *add*-ing the file to the
index.  I'll also 'add' the new ``chapter2.txt`` file to the index.  I'm not
going to 'add' ``something_about_eve.txt`` at the moment.

Now I've done that, all the stuff I want to store in the backup is ready.  I
just need to put it into its own backup archive directory.   To do that, I just
do something like (Unix again)::

    mkdir .ahole/year0-jan-02
    mkdir .ahole/year0-jan-02/files
    # ``cp -a`` below copies links as new links rather than fresh copies of
    # the linked file
    cp -a .ahole/index/* .ahole/year0-jan-02/files 
    rm .ahole/index/*

I end up with a directory that looks like this::

    .
    ├── .ahole
    │   ├── year0-jan-02
    │   │   └── files
    │   │       ├── chapter2.txt
    │   │       ├── chapter1.txt
    │   │       └── contents.txt
    │   └── year0-jan-01
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt
    ├── something_about_eve.txt
    ├── chapter2.txt
    ├── chapter1.txt
    └── contents.txt

I decide that I'll use the name *commit* for each of the archive directories
(``year0-jan-01`` and ``year0-jan-02``).  The action of adding files to the
index, I will call *staging* files for the 'commit'.  I will use the term
*committing* for the action of making the archive directory, and copying the
files from the index to archive directory.

On the third day - history
==========================

As a result of certain events yesterday evening, I have a new friend, Eve.  She
wants to help out.  Of course Eve has her own computer, and I send her my
``.ahole`` directory.  I thank myself for my wisdom in not adding
``something_about_eve.txt`` to the repository.

Eve checks out our book (reconstructs my working tree) with something like::

    cp .ahole/year0-jan-02/files/* .

(where the ``cp`` command copies links as fresh new copies of the files).  Now
she's got the same working tree as me (apart from the file I didn't want her to
see).  She does some fine work on ``chapter1.txt``.  At the end of the day, she
commits her changes the same way I do.  She first makes fresh links my last set
of files in her own ``index``::

    ├── .ahole
    │   ├─── index
    │   │    ├── chapter2.txt (link to ../year0-jan-02/files/chapter1.txt)
    │   │    ├── chapter1.txt (link to ../year0-jan-02/files/chapter1.txt)
    │   │    └── contents.txt (link to ../year0-jan-02/files/contents.txt)

then she copies her own new ``chapter1.txt`` over the link to ``chapter1.txt``
in the index::

    ├── .ahole
    │   ├─── index
    │   │    ├── chapter1.txt (fresh copy from Eve's working tree)
    │   │    ├── chapter2.txt (link to ../year0-jan-02/files/chapter1.txt)
    │   │    └── contents.txt (link to ../year0-jan-02/files/contents.txt)

and does a commit::

    mkdir .ahole/year0-jan-03
    mkdir .ahole/year0-jan-03/files
    # ``cp -a`` below copies links as new links rather than fresh copies of
    # the linked file
    cp -a .ahole/index/* .ahole/year0-jan-03/files
    rm .ahole/index/*

At least, that is what Eve was going to do, but Eve is smart, and she
immediately realizes that there is a problem.  After she has done her commit,
both of us will likely have a commit directory ``.ahole/year0-jan-03`` - but
they will have different contents.   If she later wants to share work with me,
that could get confusing.

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
the same way, in the ``files`` subdirectory, but we'll add a new file to each
commit, called ``info.txt`` that will tell us who did the commit, and when, and,
most importantly, what the previous commit was.  We'll call the previous commit
the *parent*.  

Eve was right to predict that I had made my own commit today.  So, before our
conversation, my directory looked like this::

    .
    ├── .ahole
    │   ├── year0-jan-03
    │   │   └── files
    │   │       ├── chapter2.txt
    │   │       ├── chapter1.txt
    │   │       └── contents.txt
    │   ├── year0-jan-02
    │   │   └── files
    │   │       ├── chapter2.txt
    │   │       ├── chapter1.txt
    │   │       └── contents.txt
    │   └── year0-jan-01
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt
    ├── something_about_eve.txt
    ├── chapter2.txt
    ├── chapter1.txt
    └── contents.txt

but now we've worked out the new way, it looks like this::

    .
    ├── .ahole
    │   ├── 5d89f8
    │   │   ├── info.txt
    │   │   └── files
    │   │       ├── chapter2.txt
    │   │       ├── chapter1.txt
    │   │       └── contents.txt
    │   ├── 7ef41f
    │   │   ├── info.txt
    │   │   └── files
    │   │       ├── chapter2.txt
    │   │       ├── chapter1.txt
    │   │       └── contents.txt
    │   └── 6438a4
    │       ├── info.txt
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt
    ├── something_about_eve.txt
    ├── chapter2.txt
    ├── chapter1.txt
    └── contents.txt

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
    │   │   └── files
    │   │       ├── chapter2.txt
    │   │       ├── chapter1.txt
    │   │       └── contents.txt
    │   ├── 7ef41f
    │   │   ├── info.txt
    │   │   └── files
    │   │       ├── chapter2.txt
    │   │       ├── chapter1.txt
    │   │       └── contents.txt
    │   └── 6438a4
    │       ├── info.txt
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt
    ├── chapter2.txt
    ├── chapter1.txt
    └── contents.txt

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
       # Make an archive of the current working tree in .ahole/$UID/files
       # Get previous (parent) commit id from .ahole/HEAD => HEAD
       # Make .ahole/$UID/info.txt with parent set to HEAD
       # Set .ahole/HEAD to contain UID

And then, when we want to go back to an earlier state of the book, we can do a
*checkout*, with something like::

   def ahole_checkout(commit_id):
      # clear the current working tree
      # unpack .ahole/$commit_id/files into working tree
      # make .ahole/HEAD contain $commit_id

So, when we run ``ahole_checkout('7ef41f`)`` we will get the copy of the working
tree corresponging to ``7ef41f``, and ``.ahole/HEAD`` will just contain the
string ``7ef41f``. 

In our excitement, we immediately realize that it's really easy to see the
history of the book now.  We can easily fetch out ``info.txt`` from the current
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

So, ``.ahole/HEAD`` is a reference - the current commit.  But what if I decide
that I want to give out some preliminary version of our book.  Let's say I want
to release the book stored in ``.ahole/7ef41f/files`` as 'release-0.1'.   I'm going
to send this out to all my friends (to be honest, I don't have many friends just
yet, but still).  I want to be able to remember what version of the book I sent
out.  I can make a *reference* to this commit.  I'll call this a *tag*.   I make
a new directory in ``.ahole`` called ``refs``, and another directory in
``refs``, called ``tags``, and then, in ``.ahole/refs/tags/release-0.1`` I just
put '7ef41f' - a reference to the release commit.   That way, if I ever need to
go back to the version of the book I released, I just have to read the ``release-0.1`` file to
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
       # Make an archive of the current working tree in .ahole/$UID/files
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

Ok - now let's return to me checking out the released version of the book.  I
first get the contents of ``.ahole/refs/tags/release-0.1`` - it's '5d89f8'.
Then I checkout the working tree for that version, using my nice
``ahole_checkout`` procedure::

    ahole_checkout('5d89f8')

The checkout procedure will make ``.ahole/HEAD`` contain the text ``5d89f8``.  

Now I want to go back to working on my current version of the book.  That's the
set of files pointed to by ``.ahole/refs/heads/master``.  Of course, I can I
check the contents of ``.ahole/refs/heads/master`` - it is ``dfbeda``.  Then I
get the book texbook tex normal checkout procedure::

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
      # unpack .ahole/$UID/filesinto working tree
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
there's a serious conceptual error in the version of the book that I released -
``release-0.1``?  What if I want to go back and fix it - that is - do another
commit on top of the *released* book, instead of the version of the book that
I'm currently working on?  I can just make a new *head*.  I'll do it like this::

   cp .ahole/refs/tags/release-0.1 .ahole/refs/heads/working-on-0.1

Then, I look at what commit ``working-on-0.1`` contains - of course it's
``7ef41f``.  I get that state of the book with my new checkout procedure::

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
her changes, and whether I'll include them in my version of the book.  Unwisely
I end up suggesting that women don't contribute to books, and ask her why her
head isn't covered with an as-yet not-invented headscarf.  In the end we patch
it up, and I agree to go back and try and put in her changes. 

Luckily, despite the lack of basics like clothing, there is an excellent local
network, so I can see the contents of her version of the book at
``/eves_computer/our_project/.ahole``.  She wants me to look at her 'master'
branch.  Just because the network might fail, I need to fetch what I need from
her computer to mine.  So, to keep track of things, I'll make a new directory,
called ``.ahole/refs/remotes/eve``, and I'll copy all her *heads* - in this case
just ``master`` - to that directory.   So now, I've got
``.ahole/refs/remotes/eve/master``, and in fact, it points to the commit that
she did on the third day - and this was commit '0a01a0'.  I don't have this
commit in my ``.ahole`` directory, so I'll copy that from
``/eves_computer/our_project/.ahole/0a01a0``.  I look in the ``info.txt`` file
for that commit, and check what the parent is.  It is '7ef41f'.  I check if I
have that, and yes, I have, so I can stop copying stuff from Eve's directory.

So, what I just did was:

* Copy Eve's *head* references from
  ``/eves_computer/our_project/.ahole/refs/heads`` to my
  ``.ahole/refs/remotes/eve``. 
* For each of the references in ``.ahole/refs/remotes/eve``, I check whether
  I have the referenced commit, and the parents of that commit, and, if not, I
  copy them to ``.ahole``.

We decide to call that two-step sequence - a *fetch*. 

Now I want to look at her version of the book.  I can just check it out of
course.  I first get the commit identifier from
``.ahole/refs/remotes/eve/master`` - '0a01a0'.  Then::

    ahole_checkout('0a01a0')

This will put '0a01a0' into ``.ahole/HEAD``.  I can look at her version of the
book, and decide if I like it.  If I do, then I can do a *merge*.  What's a
merge?  It's the join of two commits.  First I work out where Eve's tree
diverged from mine, by going back in her history, following the parents of the
commits.  In this case it's easy, because the parent commit ('7ef41f') of this
commit ('0a01a0') is one that is also in my history (the history for my 'master'
branch).  Then I work out the difference between the last shared commit
('7ef41f') and this commit ('0a01a0') - let's call that ``eves_diff``.  

I go back to my own 'master' - which turns out to be
(``.ahole/refs/heads/master``) - 'dfbeda'::

    ahole_checkout('master')
   
This will change ``.ahole/HEAD`` to be ``ref: refs/heads/master`` - and I will
have just got the working tree from ``.ahole/dfbeda/files``.  Then I take
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

.. rubric

.. _[1] ``ahole`` might seem a bit rude to you, but I was born in the UK, and,
        where I come from, 'ahole' is roughly as rude as 'git'. 
