#!/usr/bin/env python

import os
import subprocess

def execute(command):
    return subprocess.Popen(command, stdout=PIPE).stdout.read()

def get_from_plist(key, plist):
    return execute('/usr/libexec/PlistBuddy -c "Print %s" "%s"' % (key, plist))

plist = os.environ['INFOPLIST_FILE']
build_version = get_from_plist('CFBundleVersion', plist)
short_build_version = get_from_plist('CFBundleShortVersion', plist)

if build_version.startswith(short_build_version):
    sys.exit(0)
else:
    sys.exit(1)


