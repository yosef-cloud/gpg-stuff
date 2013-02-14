#!/usr/bin/python
'''
create_environment.py 

Create a temporary environment for pygpgme.

Based on
/usr/lib/python2.7/dist-packages/gpgme/tests/util.py
'''

import os
import random
import shutil
import time


# Create environment
random_suffix = "%04x" % random.randrange(1 << 16)
gpg_home = '/tmp/gpghome_%s' % random_suffix
os.mkdir(gpg_home)
conf_file = open(os.path.join(gpg_home, 'gpg.conf'), 'w')
conf_file.close()
os.environ['GNUPGHOME'] = gpg_home

time.sleep(30)
# Tear down environment
shutil.rmtree(gpg_home)
