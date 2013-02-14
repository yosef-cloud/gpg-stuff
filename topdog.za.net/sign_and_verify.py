#!/usr/bin/pytyhon

import os
import gpgme
from StringIO import StringIO

gpghome = os.path.expanduser('~/.gnupg')
os.environ['GNUPGHOME'] = gpghome
assert 'GPG_AGENT_INFO' not in os.environ

def passphrase_cb(uid_hint, passphrase_info, prev_was_bad, fd):
    os.write(fd, 'whatever\n')


ctx = gpgme.Context()
ctx.armor = True
print list(ctx.keylist())
[key] = ctx.keylist()
ctx.signers = [key]
ctx.passphrase_cb = passphrase_cb

plaintext = StringIO('hello world\n')
signature = StringIO()
signed = ctx.sign(plaintext, signature, gpgme.SIG_MODE_DETACH)

print 'signed =', signed

plaintext.seek(0)
signature.seek(0)

sigs = ctx.verify(signature, plaintext, None)
print sigs[0].fpr
