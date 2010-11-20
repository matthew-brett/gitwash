""" Testing gitwash dumper
"""

from os.path import join as pjoin, dirname, split as psplit
import shutil
from tempfile import mkdtemp
from subprocess import call

from nose.tools import assert_true, assert_equal, assert_raises


def test_dumper():
    downpath, _ = psplit(dirname(__file__))
    exe_pth = pjoin(downpath, 'gitwash_dumper.py')
    tmpdir = mkdtemp()
    try:
        call([exe_pth,
              tmpdir,
              'my_project'])
    finally:
        shutil.rmtree(tmpdir)

