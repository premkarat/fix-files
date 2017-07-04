#!/usr/bin/python
# Author: Prem Karat
# MIT license
# rename files names NOT directories
#   1. from uppercase to lowercase
#   2. replace spaces with -
#   3. replace _ to -
# There is no WARRANTY of any kind, please refer to MIT Licnese.

import os
import sys
from commands import getstatusoutput


def main():
    dir = None
    if len(sys.argv) > 1:
        dir = sys.argv[1]
    if not dir:
        dir = './'

    modified = False
    for root, _, files in os.walk(dir):
        for fname in files:
            fnameModified = False
            orgfname = os.path.join(root, fname)
            if ' ' in fname:
                fname = '-'.join(fname.split())
                fnameModified = True
            if '_' in fname:
                fname = fname.replace('_', '-')
                fnameModified = True
            if any(x.isupper() for x in fname):
                fname = fname.lower()
                fnameModified = True
            if fnameModified:
                newfname = os.path.join(root, fname)
                stat, _ = getstatusoutput("mv '%s' %s" % (orgfname, newfname))
                if stat != 0:
                    print "Failed to rename %s to %s" % (orgfname, newfname)
                else:
                    modified = True

    if not modified:
        print "no files modified"

                
if __name__ == '__main__':
    main()
