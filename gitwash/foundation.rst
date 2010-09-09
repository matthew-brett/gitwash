.. _git-foundation:

===============
Git foundations
===============

"Foundations" is a little joke on a religous theme; our page borrows heavily
from the `git parable`_ - so - why not a foundation myth?

On the first day - the repository and the working tree
======================================================

I'm young and the world is fresh and I have lots of time.

I have so much time, that I decide that I want to write a book.  The project I
am working on is a modest history and explanation of everything, with
provisional title "The Book".  It has a table of contents ``contents.txt`` and a
single book chapter::

    .
    ├── chapter1.txt
    └── contents.txt

As I start to write, I begin to think I should keep track of my changes.  I need
some sort of version control system.  How hard can it be?

I start with some names.  I'm going to call this set of files that I'm working
on, the *working tree*. Because I currently lack any shame about body issues, I
will call my new versioning system ``ahole`` [#ahole_git]_ .

I decide that what I need to do is store the state of The Book at the end of each
day.  To do this, I make a new directory in my working tree, called ``.ahole``.
This directory will store The Book as it evolves into a world-wide best-seller.
I will use the name *repository* for the contents of ``.ahole``. 

At the end of the day, I make a copy of all the files in the working tree, and
save it in my new ``.ahole`` repository.  In fact, what I will do is, make a new
subdirectory in ``.ahole`` named for today's date, then store a copy of the book
files in there.  On unix, that might look like this::

    mkdir .ahole/year0-jan-01
    mkdir .ahole/year0-jan-01/files
    cp * .ahole/year0-jan-01/files 

So I've still got the contents of The Book in the working tree, but now, in the
repository, I have a copy of the files that is a snapshot of The Book as of
today::

    .
    ├── .ahole
    │   └── year0-jan-01
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt
    ├── chapter1.txt
    └── contents.txt

On the second day - staging and commits
=======================================

Today I do some more work on the book.   I start work on chapter 2, and, while
I'm thinking about things, At the same time I find that I am writing some notes
to myself about this character "Eve" that I have seen wandering around.  I save
those notes in a file called ``something_about_eve.txt``.  When I get to the end
of the day, I start thinking about storing my work.  At the moment, my directory
looks like this::

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

For some reason I can't put my finger on, I don't want to put
``something_about_eve.txt`` into the repository at the moment.  In fact, in
general, I want to choose which changes I back up into the repository, and which
changes I leave for another day.  In the end I come up with an idea.  I'll make
a directory in ``.ahole`` called ``staging_area``.  When I start work at the
beginning of the day, I copy the previous backed-up version of my files from the
repository, into ``staging_area``. These files are now ready for storing in the
next snapshot::

    cp .ahole/year0-jan-01/* .ahole/staging_area

I now have::

    ├── .ahole
    │   ├─── staging_area
    │   │    ├── chapter1.txt 
    │   │    └── contents.txt
    │   └── year0-jan-01
    │       └── files
    │           ├── chapter1.txt
    │           └── contents.txt


As I work, I decide what I'm going to put into tonight's snapshot.  For example,
maybe I changed ``chapter1.txt`` and I think it's ready to back up. I copy my
modified version of ``chapter1.txt`` from the working tree to ``staging_area``.
I'll call that *stage*-ing the file.  I'll also 'stage' the new ``chapter2.txt``
file (copy it to the staging area).  I'm not going to stage
``something_about_eve.txt`` at the moment.

Now I've done that, all the stuff I want to store in the backup is ready.  I
just need to put it into its own backup snapshot directory.   To do that, I just
do something like (Unix again)::

    mkdir .ahole/year0-jan-02
    mkdir .ahole/year0-jan-02/files
    cp .ahole/staging_area/* .ahole/year0-jan-02/files 
    rm .ahole/staging_area/*

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

I decide that I'll use the name *commit* for each of the daily snapshot
directories (``year0-jan-01`` and ``year0-jan-02``).  The action of adding files
to the staging area, I will call *staging* files for the 'commit'.  I will use
the term *committing* for the action of making the snapshot directory, and
copying the files from the staging area to the snapshot directory.

On the third day - history
==========================

As a result of certain events yesterday evening, I have a new friend, Eve.  She
wants to help out.  Of course Eve has her own computer, and I send her my
``.ahole`` directory.  I thank myself for my wisdom in not adding
``something_about_eve.txt`` to the repository.

Eve checks out our book (reconstructs my working tree) with something like::

    cp .ahole/year0-jan-02/files/* .

Now she's got the book files as I committed them last night.  She also copies
the last commit files into the staging area, as I did:: 

    ├── .ahole
    │   ├─── staging_area
    │   │    ├── chapter2.txt 
    │   │    ├── chapter1.txt
    │   │    └── contents.txt

She does some fine work on ``chapter1.txt``. Around the middle of the day, she
thinks that chapter 1 is ready to back up, so she copies it to
``.ahole/staging_area``. 

and does a commit::

    mkdir .ahole/year0-jan-03
    mkdir .ahole/year0-jan-03/files
    cp -a .ahole/staging_area/* .ahole/year0-jan-03/files

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
commit, called ``info.txt``, that will tell us who did the commit, and when, and,
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
    message = Third day
    date = year0-jan-03
    parent = 7ef41f

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
    message = Eve day 3
    date = year0-jan-03
    parent = 7ef41f

After a little thought, Eve and I realize that, when we make our new commit, we
are going to have to know what the current commit is, so we can use that as the
parent.  When we make a new commit, we store the commit identifier in a file.
We'll call this file ``.ahole/HEAD``, so, after my last commit above, the file
``.ahole/HEAD`` will have the contents ``5d89f8``. We use the contents of
``.ahole/HEAD`` to identify the last (current) commit.  And of course, when we
make a new commit, we can get the parent of the new commit, from the current
commit in ``.ahole/HEAD``. 

So now, we have a new procedure for our commit.  In outline it looks like this
(now in python_ syntax) [#commit_imports]_ ::

   def ahole_commit(committer, message):
       # Make a unique identifier for this commit somehow
       new_id = make_unique_id()
       # Make a new directory in ahole with the new unique name 
       commit_dir = '.ahole/' + new_id
       mkdir(commit_dir)
       mkdir(commit_dir + '/files')
       # Copy the files from the staging area to the new directory
       # command example: 'cp .ahole/staging_area/* .ahole/7ef41f/files'
       system_call('cp .ahole/staging_area/* ' + commit_dir + '/files')
       # Get previous (parent) commit id from .ahole/HEAD 
       head_id = file('.ahole/HEAD').read()
       # Make info.txt with parent set to HEAD
       info_file = file(commit_dir + '/info.txt', 'w')
       info_file.write('committer = ' + committer + '\n')
       info_file.write('message = ' + message + '\n')
       info_file.write('date = ' + date.today() + '\n')
       info_file.write('parent = ' + head_id + '\n')
       info_file.close()
       # Set .ahole/HEAD to contain new commit id
       file('.ahole/HEAD', 'w').write(new_id)

When we want to go back to an earlier state of the book, we can do a
*checkout*, with something like:: 

   def ahole_checkout(commit_id):
      commit_dir = '.ahole/' + commit_id
      # copy .ahole/$commit_id/files into working tree
      # command example: 'cp .ahole/7ef41f/files .'
      system_call('cp ' + commit_dir + '/files/* .')
      # make .ahole/HEAD contain commit_id
      file('.ahole/HEAD', 'w').write(commit_id)

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

So, ``.ahole/HEAD`` is a reference - to the current commit.  But what if I decide
that I want to give out some preliminary version of our book.  Let's say I want
to release the book stored in ``.ahole/7ef41f/files`` as 'release-0.1'.   I'm
going to send this out to all my friends (to be honest, I don't have many
friends just yet, but still).  I want to be able to remember what version of the
book I sent out.  I can make a *reference* to this commit.  I'll call this a
*tag*.   I make a new directory in ``.ahole`` called ``refs``, and another
directory in ``refs``, called ``tags``, and then, in
``.ahole/refs/tags/release-0.1`` I just put '7ef41f' - a reference to the
release commit.   That way, if I ever need to go back to the version of the book
I released, I just have to read the ``release-0.1`` file to find the commit, and
then checkout that commit. 

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
When I've saved the new commit, I set ``.ahole/refs/heads/master`` to have the
new commit id.  So, I need to modify my commit procedure slightly::

   def ahole_commit(committer, message):
       # *** this stuff down to the next *** line is new
       # Get previous (parent) commit id from .ahole/HEAD
       head_contents = file('.ahole/HEAD').read()
       # Check if this is a reference, de-reference if so
       # Also, get file into which to write the new commit id
       if head_contents.startswith('ref: '):
           head_ref = head_contents.replace('ref: ', '')
           head_ref_file = '.ahole/' + head_ref
           head_id = file(head_ref_file).read()
       else:
           head_ref_file = '.ahole/HEAD'
           head_id = head_contents
       # *** the stuff below you've seen before (until *** again)
       # Make a unique identifier for this commit somehow
       new_id = make_unique_id()
       # Make a new directory in ahole with the new unique name 
       commit_dir = '.ahole/' + new_id
       mkdir(commit_dir)
       mkdir(commit_dir + '/files')
       # Copy the files from the staging area to the new directory
       # command example: 'cp .ahole/staging_area/* .ahole/7ef41f/files'
       system_call('cp .ahole/staging_area/* ' + commit_dir + '/files')
       # Make info.txt with parent set to HEAD
       info_file = file(commit_dir + '/info.txt', 'w')
       info_file.write('committer = ' + committer + '\n')
       info_file.write('message = ' + message + '\n')
       info_file.write('date = ' + date.today() + '\n')
       info_file.write('parent = ' + head_id + '\n')
       info_file.close()
       # Set the file that points to the current commit, to point to our commit
       # *** a little new, in that we might be writing to .ahole/HEAD, or
       # something like .ahole/refs/heads/master, depending on what .ahole/HEAD
       # contained at the top of this routine
       file(head_ref_file, 'w').write(new_id)

So, let's say that I'm currently on commit '5d89f8'.  ``.ahole/HEAD`` contains
``ref: refs/heads/master``.  ``.ahole/refs/heads/master`` contains ``5d89f8``.
I run my commit procedure::

   ahole_commit('Adam', 'Night follows day')

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
set of files pointed to by ``.ahole/refs/heads/master``.  I can
check the contents of ``.ahole/refs/heads/master`` - it is ``dfbeda``.  Then I
get the current version with the normal checkout procedure::

    ahole_checkout('dfbeda')

Finally, I'll have to set ``.ahole/HEAD`` to be ``ref: refs/heads/master``.  All
good.

Of course, I could automate this, by modifying my checkout procedure slightly
[#add_listdir]_ ::

   def ahole_checkout(commit_reference):
      # If this is a reference, dereference
      if commit_reference in listdir('.ahole/refs/heads'): 
          # it's a head reference, maybe 'master'
          head_reference = True
          fname = '.ahole/refs/heads/' + commit_reference
          commit_id = file(fname).read()
      elif commit_reference in listdir('.ahole/refs/tags'):
          # it's a tag reference
          head_reference = False
          fname = '.ahole/refs/tags/' + commit_reference
          commit_id = file(fname).read()
      else: # Just a standard commit id
          head_reference = False
          commit_id = commit_reference
      commit_dir = '.ahole/' + commit_id
      # copy .ahole/$commit_id/files into working tree
      # command example: 'cp .ahole/7ef41f/files .'
      system_call('cp ' + commit_dir + '/files/* .')
      # make ahole/HEAD point to commit id
      if head_reference:
          # Point HEAD at head reference
          file('.ahole/HEAD').write('ref: refs/heads/' + commit_reference)
          # Write commit id into head reference file
          file('.ahole/refs/heads/' + commit_reference, 'w').write(commit_id)
      else:
          file('.ahole/HEAD', 'w').write(commit_id)

What then, is the difference, between a *tag* - like our release - and the
moving target like 'master'?  The 'tag' is a *static* reference - it does not
change when we do a commit and always points to the same commit.  'master' is a
dynamic reference - in particular, it's a *head* reference:

Head
    A head is a reference that updates when we do a commit

My head is hurting a little, after Eve explains all this, but after a little
while and a nice apple pie, I'm feeling positive about ``ahole``.

On the fifth day - branches, merges and remotes
===============================================

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
of commits, which can grow.  All I need, to make a new branch, is make a
new head reference to a commit.  For example, if I want to make new branch
starting at the current position of 'master', all I need is::

   cp .ahole/refs/tags/master .ahole/refs/heads/my-new-branch

If I want to work on this branch, I need to check it out, with::

    ahole_checkout('my-new-branch')

That will get the commit identifier in ``.ahole/refs/heads/my-new-branch``, unpack
the commit tree into the working tree, and set ``.ahole/HEAD`` to contain the
text ``ref: refs/heads/my-new-branch``

I've got my branches, but Eve will have her own branches, and this will help us
know where each of us is working.  

That's good, because Eve is now asking me if I can have a look at her changes,
and whether I'll include them in my version of the book.  Unwisely I end up
suggesting that women don't contribute to books, and ask her why her hair isn't
covered with an as-yet not-invented headscarf.  In the end we patch it up, and I
agree to go back and try and put in her changes. 

Luckily, despite the lack of basics like clothing, there is an excellent local
network, so I can see the contents of her version of the book at
``/eves_computer/our_book/.ahole``.  She wants me to look at her 'master'
branch.  Just because the network might fail, I need to fetch what I need from
her computer to mine.  So, to keep track of things, I'll make a new directory,
called ``.ahole/refs/remotes/eve``, and I'll copy all her *heads* - in this case
just ``master`` - to that directory.   So now, I've got
``.ahole/refs/remotes/eve/master``, and in fact, it points to the commit that
she did on the third day; this was commit '0a01a0'.  I don't have this
commit in my ``.ahole`` directory, so I'll copy that from
``/eves_computer/our_book/.ahole/0a01a0``.  I look in the ``info.txt`` file
for that commit, and check what the parent is.  It is '7ef41f'.  I check if I
have that, and yes, I have, so I can stop copying stuff from Eve's directory.

So, what I just did was:

* Copy Eve's *head* references from
  ``/eves_computer/our_book/.ahole/refs/heads`` to my
  ``.ahole/refs/remotes/eve``. 
* For each of the references in ``.ahole/refs/remotes/eve``, I check whether
  I have the referenced commit, and the parents of that commit, and, if not, I
  copy them to ``.ahole``.

We decide to call that two-step sequence - a *fetch*. 

Now I want to look at her version of the book.  I have her head references and
the commits they point to, so I can checkout her latest version. I first get the
commit identifier from ``.ahole/refs/remotes/eve/master`` - '0a01a0'.  Then::

    ahole_checkout('0a01a0')

This will put '0a01a0' into ``.ahole/HEAD``.  I can look at her version of the
book, and decide if I like it.  If I do, then I can do a *merge*.  

What is a merge?  It's the join of two commits.  First I work out where Eve's
tree diverged from mine, by going back in her history, following the parents of
the commits.  In this case it's easy, because the parent commit ('7ef41f') of
this commit ('0a01a0') is one that is also in my history (the history for my
'master' branch).  This most recent shared commit I will call the *common
ancestor*.  Then I work out the difference between the common ancestor commit
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

On the sixth day - saving time and space with objects
=====================================================

I am now very happy with ``ahole``, but Eve clearly doesn't think we've got it
right yet.

As she's thinking, she decides to make a couple of illustrations for The Book,
so she adds some photos to her working tree::

    .
    ├── .ahole
    │   ...
    ├── images
    │   ├── adam_with_apple.jpg
    │   └── lion_with_lamb.jpg
    ├── chapter3.txt
    ├── chapter2.txt
    ├── chapter1.txt
    └── contents.txt

As soon as she does this, she realizes what's wrong with ``ahole``.  The photos
are large files.  At the moment, every time we make a commit, we're copying all
the files into the commit ``files`` directory to make the snapshot.  With big
files, this is going to lead to many identical copies and lots of wasted space. 

Eve realizes that what we need is to be able to do, is make the commit use
*references* to files, rather than the files themselves.  That way, when the
commit has files that have not changed, it can just point to the unchanged
file, rather than carrying a wasteful copy of the file.  

If the commits just store references, we need a way to store the contents of the
files, so they can be referenced.  Maybe we could store the files for our
snapshots in a directory, and use some sort of unique filename so that the
commits can reference that filename?  For example, maybe we could make a
directory in ``.ahole`` like this::

   mkdir .ahole/objects

and use this directory to store the contents of the files for our snapshots.
Then we could store the commits as something like a table, where the entries
would tell us how to get the matching files from the ``.ahole/objects``
directory. 

We could have some structure for the commits like this::

    ├── .ahole
    │   ├── 5d89f8
    │   │   ├── info.txt
    │   │   └── file_list
    
    
where ``.ahole/5d89f8/file_list`` would be a list of references to files in the
``.ahole/objects`` directory, along with the filename that the contents has when
reconstructed back into the snapshot.  For example, maybe ``file_list`` would
look like this::

    contents_version1 contents.txt 
    chapter1_version1 chapter1.txt 
    chapter2_version2 chapter2.txt 
    chapter3_version1 chapter3.txt 

These references in the first column could match filenames in the
``.ahole/objects`` directory::

    │   ├── objects
    │   │   ├── chapter1_version1
    │   │   ├── chapter2_version2
    │   │   ├── chapter2_version2
    │   │   ├── chapter3_version1
    │   │   └── contents_version1

I suppose you could think of the ``.ahole/objects`` directory as a very simple
form of database, where the keys are the filenames, and the file contents are
the values.

We think about this for a while and realize that it's going to be annoying
trying to find unique names to use as filenames in ``.ahole/objects``, because
there will be many versions of many files.  For example ``chapter1_version2``,
``chapter1_version3`` and so on is clearly not going to work, because when Eve
and I work independently, at some point we're both going to have something like
a ``chapter1_version3`` in our respective ``.ahole/objects`` directories, but
they will be different, and that will be confusing. 

At this stage, Eve reveals that she has some training in computer science.  Of
course I have no idea what that is, or who did the training, but she's in too
much of a rush to explain that now.   She proposes that we make the filenames
(database keys) by doing *hashes* of the file contents.  It turns out that
hashing algorithms can take a stream of bytes such as the contents of a file,
and create a string that is near-enough unique to that stream of bytes. That's
really good, because it means that, if Eve and I have an object with the same
filename (hash) that means it almost certainly contains the exact same contents.

Eve recommends the 'SHA1' hashing algorithm, and I'm in no position to disgree
with her.  Now we've got a unique string to use as a key for each file.  For
example, we run the SHA1 algorithm over the current book files and we get
these::

    chapter1.txt 9e398c7cf8d56e960aa7769839cc0c38b8e12f11
    chapter2.txt 65735b3705284cdf4a66c2e4812ca13cbaa7cd5d
    chapter3.txt 3c2e09cc43568f13444c075c84b047957f7995a5
    contents.txt f31bfa1225f9e0eb6741a0ab1122f8cd2cbedc04

If we change the file at all, then the hash changes, and we have a new unique
string and therefore we have a new unique filename with which to store the new
contents. For example, the original version of chapter 2 was a bit shorter, and
had a hash of '1cf01a1dfbe135b6132362fa8e17eaefcaf00a7f'. 

Now we have got a nice way of making the references that will go into
``.ahole/5d89f8/file_list``.  First we store the file versions in our
``.ahole/objects`` directory, using their hash values as filenames::

    │   ├── objects
    │   │   ├── 9e398c7cf8d56e960aa7769839cc0c38b8e12f11 (chapter1 version 1)
    │   │   ├── 1cf01a1dfbe135b6132362fa8e17eaefcaf00a7f (chapter2 version 1)
    │   │   ├── 65735b3705284cdf4a66c2e4812ca13cbaa7cd5d (chapter2 version 2)
    │   │   ├── 3c2e09cc43568f13444c075c84b047957f7995a5 (chapter3 version 1)
    │   │   └── f31bfa1225f9e0eb6741a0ab1122f8cd2cbedc04 (contents version 1)

Next we create ``.ahole/5d89f8/file_list`` with one row per file in our
directory.  Each row contains first - the hash value (and therefore filename in
``.ahole/objects``) which allows me to get the file contents, then the type of
thing this is - here a file - and lastly, the filename as it was in the
snapshot::

    9e398c7cf8d56e960aa7769839cc0c38b8e12f11 file chapter1.txt 
    65735b3705284cdf4a66c2e4812ca13cbaa7cd5d file chapter2.txt 
    3c2e09cc43568f13444c075c84b047957f7995a5 file chapter3.txt 
    f31bfa1225f9e0eb6741a0ab1122f8cd2cbedc04 file contents.txt 

Now, what about Eve's new working tree with the photos in it?  The photos are in
the ``images`` subdirectory, and we don't have a way of storing subdirectories
yet.  Aha - why not store directories in the object database too?  Directories
can just be *tree* files like ``file_list``.  *tree* files are lists, one entry
per row, where each row contains the hash reference for the file contents, the
type of thing it is (tree or file), and the filename as it was in the snapshot.
So, for Eve's new commit, we'd first store the contents of the two photo files
in the ``.ahole/objects`` directory::

    │   ├── objects
    │   │   ├── 82e6792faa893070dcd6fe3e614b6f147be1a0a9 (adam_with_apple.jpg)
    │   │   ├── e8b23357995db47e70906d4c7a08114c0c0ba376 (lion_with_lamb.jpg)
    │   │   ├── 9e398c7cf8d56e960aa7769839cc0c38b8e12f11 (chapter1 version 1)

etc.  Then we make a new *tree* file called - say - 'images_listing' like this::

    82e6792faa893070dcd6fe3e614b6f147be1a0a9 file adam_with_apple.jpg 
    e8b23357995db47e70906d4c7a08114c0c0ba376 file lion_with_lamb.jpg  

and we make a hash for that tree file too, and put that into
``.ahole/objects``::

    │   ├── objects
    │   │   ├── be242dba385bc0689be16454e959f4b64c87abce (images_listing)
    │   │   ├── 82e6792faa893070dcd6fe3e614b6f147be1a0a9 (adam_with_apple.jpg)
    │   │   ├── e8b23357995db47e70906d4c7a08114c0c0ba376 (lion_with_lamb.jpg)
    │   │   ├── 9e398c7cf8d56e960aa7769839cc0c38b8e12f11 (chapter1 version 1)

etc.  Now maybe our whole commit listing can include files and directories for
the root directory of our project, something like::

    9e398c7cf8d56e960aa7769839cc0c38b8e12f11 file chapter1.txt
    65735b3705284cdf4a66c2e4812ca13cbaa7cd5d file chapter2.txt
    3c2e09cc43568f13444c075c84b047957f7995a5 file chapter3.txt
    f31bfa1225f9e0eb6741a0ab1122f8cd2cbedc04 file contents.txt
    be242dba385bc0689be16454e959f4b64c87abce tree images      

Oh - but wait - that's just a tree listing too, let's make a hash for that, and
put it into the ``.ahole/objects`` directory::

    │   ├── objects
    │   │   ├── e52dc9dbe358c549df65307652ff2709322812b3 (root listing)  
    │   │   ├── be242dba385bc0689be16454e959f4b64c87abce (images_listing)
    │   │   ├── 82e6792faa893070dcd6fe3e614b6f147be1a0a9 (adam_with_apple.jpg)

Right - so now our whole commit boils down to our ``info.txt`` file, and the
hash for the root tree (the one starting 'e52dc' above). We can get rid of the
old ``files`` subdirectory in the commit, and add the hash for the root tree
instead - something like::

    committer = Eve
    message = Adding funny pictures
    date = year0-jan-06
    root_tree = e52dc9dbe358c549df65307652ff2709322812b3 
    parent = 0a01a0

Now we can solve the annoying problem of finding an unique commit id for each
commit.   We just make a hash for the ``info.txt`` file, and put that into the
``.ahole/objects`` directory too, as a *commit* file::

    │   ├── objects
    │   │   ├── 7e0cda8c145b300b519ed28998a31f801b6d626f (latest commit)
    │   │   ├── e52dc9dbe358c549df65307652ff2709322812b3 (root listing)  
    │   │   ├── be242dba385bc0689be16454e959f4b64c87abce (images_listing)

The unique id for the commit is the hash for its contents. In this case the
commit id is '7e0cda8c145b300b519ed28998a31f801b6d626f'.  Don't forget that the
hash is more or less unique to the contents, so this commit will have an id that
is unique to the combination of the committer, message, date, root tree hash and
commit parent.  The root tree hash is unique to the contents of the root tree
listing, and the root tree listing contains file hashes, which are in turn
unique to the file contents, so the root tree hash will be unique to the file
contents of the commit.  Thus, the commit id is unique to all the things that go
into the commit, including the contents.  It's clever isn't it?

We can now have three types of files in the ``.ahole/objects`` directory -
files, trees, and commits.  

OK - so things are now a little more complicated than our previous setup with
file copies, but lots of things have just got much easier.   For example, we can
now get rid of the ``staging_area`` directory.  The staging area can just be a
single file containing the root tree listing of the snapshot.  Let's call that
file ``.ahole/index``.  Now Eve has done her new commit, that file can just be
the root directory listing of the previous commit (the commit we have just
done)::

    9e398c7cf8d56e960aa7769839cc0c38b8e12f11 file chapter1.txt
    65735b3705284cdf4a66c2e4812ca13cbaa7cd5d file chapter2.txt
    3c2e09cc43568f13444c075c84b047957f7995a5 file chapter3.txt
    f31bfa1225f9e0eb6741a0ab1122f8cd2cbedc04 file contents.txt
    be242dba385bc0689be16454e959f4b64c87abce tree images      

When Eve makes an edit to ``chapter1.txt``, instead of copying the file to the
``staging_area`` directory, she makes a hash for the new ``chapter1.txt``
contents, she stores the new ``chapter1.txt`` contents in the ``.ahole/objects``
directory using the hash as a filename, and then she edits the ``.ahole/index``
file to point to her new chapter 1 contents instead of the old.  She might
automate this with a small command like ``ahole_stage`` [#need_hashlib]_ ::

    def ahole_stage(fname):
        # Get the hash for the file contents
        file_contents = file(fname).read()
        file_hash = sha1_hash(file_contents)
        # (assuming that the new file is going in the root directory)
        new_root_entry = file_hash + ' file ' + fname
        root_listing = file('.ahole/index').read()
        if new_root_entry in root_listing:
            # This exact file contents and filename already present
            return
        # Make an entry for these file contents in the objects database
        database_fname = '.ahole/objects/' + file_hash
        file(database_fname, 'w').write(file_contents)
        # Write index listing with new entry
        root_listing = root_listing + new_root_entry + '\n'
        file('.ahole/index', 'w').write(root_listing)

Making a new commit involves taking the contents of ``.ahole/index`` and using
it to make a new commit file in ``.ahole/objects``.  Using the structure of our
previous ``ahole_commit`` routine, that might look like::

   def ahole_commit(committer, message):
       # *** this stuff is the same as before ***
       # Get previous (parent) commit id from .ahole/HEAD
       head_contents = file('.ahole/HEAD').read()
       # Check if this is a reference, de-reference if so
       # Also, get file into which to write the new commit id
       if head_contents.startswith('ref: '):
           head_ref = head_contents.replace('ref: ', '')
           head_ref_file = '.ahole/' + head_ref
           head_id = file(head_ref_file).read()
       else:
           head_ref_file = '.ahole/HEAD'
           head_id = head_contents
       # *** the stuff below is different ***
       # Make root tree entry in objects database from .ahole/index
       index_contents = file('.ahole/index').read()
       index_hash = sha1_hash(index_contents)
       file('.ahole/objects/' + index_hash, 'w').write(index_contents)
       # Make commit information with parent set to HEAD
       info_str = 'committer = ' + committer + '\n'
       info_str += 'message = ' + message + '\n'
       info_str += 'date = ' + date.today() + '\n'
       info_str += 'root_tree = ' + index_hash + '\n' 
       info_str += 'parent = ' + head_id + '\n'
       # Write commit file into objects database, with hash
       commit_hash = sha1_hash(info_str)
       file('.ahole/objects/' + commit_hash, 'w').write(info_str)
       # Set the current commit file to contain new id
       file(head_ref_file, 'w').write(commit_hash)

How about doing a merge?  Remember that, in the bad old days, we had to compare
lots of files between the branches, and the common ancestor?  No more.  Now we
are using the hash file references, all we need to do, is look at the tree
listing.  If the tree listing has the same entry (filename and hash) that means
that the file is indentical between the two trees, and we don't have to load the
contents to check.   That makes it very fast to do comparisons between trees
that haven't changed much.

Eve was right of course.  Now, if we make a new commit, when one file is
changed, all we store is the contents of the file that has changed and a new
tree listing with the updated hash for the changed file.  That makes the storage
for lots and lots of similar trees very efficient.

Someone ought to write this up and give it to the world.  Wait, that's just us.

On the seventh day - there was git
==================================

The seventh day is for resting.   You are all done now, and the hard stuff is
over.  In a state of deep inner peace, you can think about all that you've
discovered in ahole:

* A commit refers to a snapshot of the complete set of files for your project
* The staging area (index) defines what will change between your upcoming commit
  and the previous commit
* A branch is just a pointer to a commit, that moves when you do another commit.
* Version control is very easy to understand

You remind yourself that life is very good, because you don't have to use a
version control system called *ahole*, you can use a very similar system called
git_.

If you use git_, you'll notice that you have lots of *ahole* friends.  You'll
see git has a ``.git`` directory that contains the repository.  You'll recognize
the ``.git/objects`` directory containing filenames with SHA1 hashes.  You'll
see that commits have SHA1 hashes.  You'll recognize the ``.git/HEAD`` file and
``.git/refs/heads`` and ``.git/refs/tags`` and ``.git/refs/heads/master``. There
is a ``.git/index`` file, and it is the staging area. ``.git/index`` is a little
more complicated than ``.ahole/index`` because it's adapted to helping with
difficult merges, but it's the same idea. 

You now live in the garden of Eden of version control.  Remember to stay away
from that apple tree.

.. include:: git_links.inc

.. rubric:: Footnotes

.. [#ahole_git] ``ahole`` might seem a bit rude to you, but I was born in the UK, and,
     where I come from, 'ahole' is roughly as rude as 'git'. 

.. [#commit_imports] In case you are interested, for the commit code to actually
    run, you would need the prior python commands::

      from os import mkdir
      from datetime import date
      import subprocess
       
      def system_call(cmd):
          subprocess.call(cmd, shell=True)
 
    as well as some definition of ``make_unique_id()``.

.. [#add_listdir] You'll notice we added the python ``listdir`` command, from::

      from os import listdir

    .

.. [#need_hashlib] Now you need to add::

       import hashlib

       def sha1_hash(contents):
           return hashlib.sha1_hash(contents)

    .
