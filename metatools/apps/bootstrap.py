#!/usr/bin/env python

# This file was automatically generated by
# METATOOLS_SELF
# at METATOOLS_TIME.

import os
import site
import sys
import time

argv_emulation = METATOOLS_ARGV_EMULATION
command = METATOOLS_COMMAND
entrypoint = METATOOLS_ENTRYPOINT
execfile_ = METATOOLS_EXECFILE
on_open_url = METATOOLS_ON_OPEN_URL
on_open_document = METATOOLS_ON_OPEN_DOCUMENT


if argv_emulation or on_open_url or on_open_document:

    sys.path.insert(0, os.path.dirname(sys.executable))
    import bootstrap_ae

    if argv_emulation:
        print 'argv_emulation'
        handler = bootstrap_ae.AppleEventHandler()
        handler.emulate_argv()
        print 'done'


if command:
    # We loaded python just to do this?
    os.execvp(command, [command] + sys.argv[1:])
    exit(1) # Never reached.

if execfile_:
    globals_ = {'__name__': '__main__'}
    execfile(execfile_, globals_, globals_)
    exit(0)

if entrypoint:
    entrypoint = entrypoint.split(':')
    module = __import__(entrypoint[0], fromlist=['.'])
    if len(entrypoint) > 1:
        attrs = entrypoint[1].split('.')
        head = module
        for attr in attrs:
            head = getattr(head, attr, None)
            if head is None:
                print >> sys.stderr, entrypoint, 'does not exist'
                exit(2)
        head()
    exit(0)

print >> sys.stderr, 'metatools.app: unknown bootstrapping type'
exit(3)


