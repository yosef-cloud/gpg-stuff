#!/usr/bin/python
'''
import_key.py 

Create a temporary environment then import a key from a string.

Based on
/usr/lib/python2.7/dist-packages/gpgme/tests/util.py
/usr/lib/python2.7/dist-packages/gpgme/tests/util.py
'''

import os
import random
import shutil
import time
import gpgme
import StringIO


# Create environment
random_suffix = "%04x" % random.randrange(1 << 16)
gpg_home = '/tmp/gpghome_%s' % random_suffix
os.mkdir(gpg_home)
conf_file = open(os.path.join(gpg_home, 'gpg.conf'), 'w')
conf_file.close()
os.environ['GNUPGHOME'] = gpg_home

ctx = gpgme.Context()

ctx.import_(open('pubkey.asc'))

for key in ctx.keylist():
    print key

# Tear down environment
shutil.rmtree(gpg_home)
