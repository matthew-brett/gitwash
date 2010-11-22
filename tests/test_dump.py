""" Testing gitwash dumper
"""

from os.path import join as pjoin, dirname, split as psplit
import shutil
from tempfile import mkdtemp
from subprocess import call

from nose.tools import assert_true, assert_equal, assert_raises

_downpath, _ = psplit(dirname(__file__))
EXE_PTH = pjoin(_downpath, 'gitwash_dumper.py')
TMPDIR = None

def setup():
    global TMPDIR
    TMPDIR = mkdtemp()


def teardown():
    shutil.rmtree(TMPDIR)


def test_dumper():
    call([EXE_PTH,
          TMPDIR,
          'my_project'])

