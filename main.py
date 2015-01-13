#!/usr/bin/env python

import os
import subprocess
import sys

def execute(args):
    return subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]

def get_from_plist(key, plist):
    return execute(['/usr/libexec/PlistBuddy', '-c', 'Print %s' % key, '%s' % plist])

def escape_newline(string):
    return string.replace('\n', '')

src_root = os.environ['SRCROOT']
plist = src_root + '/' + os.environ['INFOPLIST_FILE']
build_version = escape_newline(get_from_plist('CFBundleVersion', plist))
short_build_version = escape_newline(get_from_plist('CFBundleShortVersionString', plist))

if build_version.startswith(short_build_version):
    sys.exit(0)
else:
    print("\nBuild (%s) should starts with Version (%s)\n" % (build_version, short_build_version))
    sys.exit(1)


