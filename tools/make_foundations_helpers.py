from os import mkdir, rename, rmdir, chdir
from os.path import sep
from glob import glob
from hashlib import sha1
from time import sleep

AHOLE_DIR = '.ahole' + sep

def rewrite_dates(committers, messages=None):
    if messages is None:
        messages = [''] * len(committers)
    date_dirs = sorted(glob(AHOLE_DIR + 'year*'))
    parent = ''
    for date_dir, committer, message in zip(date_dirs, committers, messages):
        date = date_dir.replace(AHOLE_DIR, '')
        info = '''committer = %s
date = %s
parent = %s
message = %s
''' % (committer, date, parent, message)
        files_fname = date_dir + sep + 'files.zip'
        files = open(files_fname,  'rb').read()
        hashval = sha1(files + info).hexdigest()[:6]
        hash_dir = AHOLE_DIR + hashval
        sleep(5) # to allow modification dates to differ
        mkdir(hash_dir)
        rename(files_fname, hash_dir + sep + 'files.zip')
        open(hash_dir + sep + 'info.txt', 'wt').write(info)
        parent = hashval
        rmdir(date_dir)


chdir('ourproject')
rewrite_dates(['Adam', 'Adam', 'Adam'], ['First day', 'Second day', 'Third day'])
chdir('..')
chdir('evesproject')
rewrite_dates(['Adam', 'Adam', 'Eve'], ['First day', 'Second day', 'Eve day 3'])
