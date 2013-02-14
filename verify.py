#!/usr/bin/python

import os
import random
import shutil
import time
import gpgme
import StringIO



pub_key_buff = StringIO.StringIO()
pub_key_buff.write('''
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.11 (GNU/Linux)

mI0EUR2HBwEEALs/mXmvmdB7/CKd0YfEDd0bKqtSLPM3FCSmCaCO3rhZ9eHsFETj
nKb5ERdCZRvJ/dhrVUBFXX9ojSx+LW/UCM/l004AusNLkf+ftgw0Xlbacqz+MIQI
MqVhQ4mHlga3/vy9wBnoIMjxrFyxEvNwtIDTTIImWJIVMbUnGpwImIhPABEBAAG0
HUJvYmJ5IE1jQm9iIDxibWJAZXhhbXBsZS5jb20+iL4EEwECACgFAlEdhwcCGwMF
CQANLwAGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEE89YXufLzd5IuMEALka
VqCCrRHf7HXIEQG3asBkAecmb7Pa/D51zCtzHAft2p9XZvdTczu+OoNgdqhjHUPx
Yi+bfj/TVUDTiyrn9/cbvRIX2XbKTgXPBru7E1LGHsO+jfyVgzcHa9vYvB8fWVtl
Um4crD9L9emoXxw5AKd/djuuQS/L2rhGbf0M2mRwuI0EUR2HBwEEAKL08MOujedI
vbxPBgjkLXgeGmL6ilzEwQ2/EyniBIM5iJ3yGSAKweBhgumGqleWLhJNgm2dep2o
Htaojkmk+GsNjjjGj3FKqLxeHAGvYJdkddJGfvRGlNm+dm/clsCGeueUz59bGHtV
WgOtj4mjAGfrP+t5MC3cstM8qSznN6tXABEBAAGIpQQYAQIADwUCUR2HBwIbDAUJ
AA0vAAAKCRBPPWF7ny83eYv4BACLDmsDYA+sc1sIxiM5t9Ha24JJuOw6B28oY5cU
yB7cLEYCtVL8JhAmTe7zXIhpf67+DPPlXuZlQA6oM9UnS9EyBYutNrK2yTDadHC4
7L4EdK9ccdqcLBZ3rlXR54Qc4FSEDx/HAuOXfFvVfNOFUf5wcAo6+GZEL3MdM71p
OUYn1A==
=ppdo
-----END PGP PUBLIC KEY BLOCK-----
''')
pub_key_buff.seek(0)

sec_key_buff = StringIO.StringIO()
sec_key_buff.write('''
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: GnuPG v1.4.11 (GNU/Linux)

lQH+BFEdhwcBBAC7P5l5r5nQe/windGHxA3dGyqrUizzNxQkpgmgjt64WfXh7BRE
45ym+REXQmUbyf3Ya1VARV1/aI0sfi1v1AjP5dNOALrDS5H/n7YMNF5W2nKs/jCE
CDKlYUOJh5YGt/78vcAZ6CDI8axcsRLzcLSA00yCJliSFTG1JxqcCJiITwARAQAB
/gMDAphUqPM6n7vXYH3G3erG1+VW8U1oOtxtCDUI6Nanzg47thf67uh3Tt1JSTwd
22jirfyGEswNfi6msbpmTmJNLjgp4dSLRsoYfp8fbo0+FcYFP2ifcfToFiJV/6il
sWi/620i255UsYiz458Q3HmIouqXrM+VGnH3o0v51aYhDAF63HE2LqVuTpd9Th7d
DzCznBbfbdhoyEP7GEtNguNCk/ZFV0mYeXfVVRg90D2vuxBbycGYl7zF4NgG4yhe
SD2XVUj3WJj/OW9Le8GgqbIyXKzgcNyBWvJUaugYRwoYbGRR69QHTZb7DMpre42P
TYHuCF0vPyRyE1RhO3J2ExjZJIYKkdE88F3Ug4hqqKH98CykwP20oP3CcBqk4BPz
yV4ZYU9PwamrwgsRiomRy11qoIJxZS2bBsq/A1S8wMrwaJ5z3fwQy9Dfg+E6SO0N
iuE1iiZ73Lj7eu5X91OCNNG/IR5LlNPfh0+/D9k5yiwVtB1Cb2JieSBNY0JvYiA8
Ym1iQGV4YW1wbGUuY29tPoi+BBMBAgAoBQJRHYcHAhsDBQkADS8ABgsJCAcDAgYV
CAIJCgsEFgIDAQIeAQIXgAAKCRBPPWF7ny83eSLjBAC5Glaggq0R3+x1yBEBt2rA
ZAHnJm+z2vw+dcwrcxwH7dqfV2b3U3M7vjqDYHaoYx1D8WIvm34/01VA04sq5/f3
G70SF9l2yk4Fzwa7uxNSxh7Dvo38lYM3B2vb2LwfH1lbZVJuHKw/S/XpqF8cOQCn
f3Y7rkEvy9q4Rm39DNpkcJ0B/QRRHYcHAQQAovTww66N50i9vE8GCOQteB4aYvqK
XMTBDb8TKeIEgzmInfIZIArB4GGC6YaqV5YuEk2CbZ16nage1qiOSaT4aw2OOMaP
cUqovF4cAa9gl2R10kZ+9EaU2b52b9yWwIZ655TPn1sYe1VaA62PiaMAZ+s/63kw
Ldyy0zypLOc3q1cAEQEAAf4DAwKYVKjzOp+712CaWpO5l7kqOXXN3KpcCDMjpYNA
Q7U4qE/cav3g8UibZpqyjZQyJ4r72uHPqyAH9F5jOD57vu1AGFNveHCcHA42lTvi
dRGLYX4AOpxo+3kbqXWWeNRneK1xQ9noT40Wi2hmDf1377PUKG4qxbEl0M9Y/Bur
vQMa44N4OO0GPEcF8evjwDspze3mkX/ep/Xlr9eUgKO5RpodUcvVwEeEnSiI+J4l
M1DVmQPs+r+kJoOpnPgYlS6OwQ1en8xDnTrkU4ci3Rd3qnOczkwFpdcdQqK/PVEO
u6Zxtfwj2jvnoLfdbRbUct7iienGaMJaSgYEsEshJqBpVPaa6XDpkHIzytOJ/HCZ
H0AlkhlrAucO3dNeZXJGZmrhJzOtrQkyIEQx0mQ0sZYhHLhfUF3y5WJAW6yVzToz
Z8R4lt3BguLIwni+oH04ZVh2Q5fc7WlMGmAN+ZkhBIY3oR9wtQBQMxQjjyFkBs2R
iKUEGAECAA8FAlEdhwcCGwwFCQANLwAACgkQTz1he58vN3mL+AQAiw5rA2APrHNb
CMYjObfR2tuCSbjsOgdvKGOXFMge3CxGArVS/CYQJk3u81yIaX+u/gzz5V7mZUAO
qDPVJ0vRMgWLrTaytskw2nRwuOy+BHSvXHHanCwWd65V0eeEHOBUhA8fxwLjl3xb
1XzThVH+cHAKOvhmRC9zHTO9aTlGJ9Q=
=Z11m
-----END PGP PRIVATE KEY BLOCK-----
''')
sec_key_buff.seek(0)


# Create environment
random_suffix = "%04x" % random.randrange(1 << 16)
gpg_home = '/tmp/gpghome_%s' % random_suffix
os.mkdir(gpg_home)
conf_file = open(os.path.join(gpg_home, 'gpg.conf'), 'w')
conf_file.close()
os.environ['GNUPGHOME'] = gpg_home
context = gpgme.Context()

context.import_(pub_key_buff)
context.import_(sec_key_buff)
k = list(context.keylist())[0]



def passphrase_callback(uid_hint, passphrase_info, prev_was_bad, fd):
    

plaintext = StringIO.StringIO()
plaintext.write("hello world")
plaintext.seek(0)
signature = StringIO.StringIO()
print context.sign(plaintext, signature, gpgme.SIG_MODE_CLEAR)
signature.seek(0)
print signature.read()


# Tear down environment
shutil.rmtree(gpg_home)
