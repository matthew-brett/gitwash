""" Testing gitwash dumper
"""

import os
from os.path import join as pjoin, dirname, split as psplit
import sys
import shutil
from tempfile import mkdtemp
from subprocess import call

from nose.tools import assert_true, assert_false, assert_equal, assert_raises

_downpath, _ = psplit(dirname(__file__))
ROOT_DIR = os.path.abspath(_downpath)
sys.path.append(ROOT_DIR)

import gitwash_dumper as gwd

EXE_PTH = pjoin(ROOT_DIR, 'gitwash_dumper.py')
DOC_DIR = pjoin(_downpath, 'gitwash')
TMPDIR = None

def setup():
    global TMPDIR
    TMPDIR = mkdtemp()


def teardown():
    shutil.rmtree(TMPDIR)


def test_link_checks():
    test_fname = pjoin(TMPDIR, 'test.inc')
    # Check case where we have links
    gwd.make_link_targets(
        'nipy',
        'nipy',
        'nipy',
        pjoin(DOC_DIR, 'known_projects.inc'),
        test_fname,
        None,
        None)
    assert_false(os.path.isfile(test_fname))
    # Add explicit links, and file gets written
    gwd.make_link_targets(
        'nipy',
        'nipy',
        'nipy',
        pjoin(DOC_DIR, 'known_projects.inc'),
        test_fname,
        'http://nowhere.org',
        None)
    assert_equal(open(test_fname, 'rt').read(),
                 """.. nipy
.. _nipy: http://nowhere.org
""")


def test_dumper():
    call([EXE_PTH,
          TMPDIR,
          'marsbar',
          '--gitwash-url=%s' % ROOT_DIR])
    gitwdir = pjoin(TMPDIR, 'gitwash')
    assert_true(os.path.isdir(gitwdir))
    for dirpath, dirnames, filenames in os.walk(gitwdir):
        if not dirpath.endswith('gitwash'):
            raise RuntimeError('I only know about the gitwash directory')
        for filename in filenames:
            old_fname = pjoin(DOC_DIR, filename)
            new_fname = pjoin(dirpath, filename)
            old_contents = file(old_fname, 'rt').readlines()
            new_contents = file(new_fname, 'rt').readlines()
            for old, new in zip(old_contents, new_contents):
                if 'PROJECT' in old and not filename.endswith('.inc'):
                    assert_false('PROJECT' in new)
                    assert_true('my_project' in new)
    shutil.rmtree(gitwdir)


def test_building():
    call([EXE_PTH,
          TMPDIR,
          'marsbar',
          '--gitwash-url=%s' % ROOT_DIR])
    cwd = os.getcwd()
    shutil.copy(pjoin(ROOT_DIR, 'conf.py'), TMPDIR)
    try:
        os.chdir(TMPDIR)
        open('index.rst', 'wt').write('\n')
        call('sphinx-build -b html -d _build/doctrees   . _build/html',
             shell=True)
        call('sphinx-build -b linkcheck -d _build/doctrees   . _build/linkcheck',
             shell=True)
    finally:
        os.chdir(cwd)
