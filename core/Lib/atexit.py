# Portions Copyright (c) 2005 Nokia Corporation 
"""
atexit.py - allow programmer to define multiple exit functions to be executed
upon normal program termination.

One public function, register, is defined.
"""

__all__ = ["register"]

_exithandlers = []
def _run_exitfuncs():
    while _exithandlers:
        func, targs, kargs = _exithandlers.pop()
        apply(func, targs, kargs)

def register(func, *targs, **kargs):
    _exithandlers.append((func, targs, kargs))

import sys
if hasattr(sys, "exitfunc"):
    # Assume it's another registered exit function - append it to our list
    register(sys.exitfunc)
sys.exitfunc = _run_exitfuncs

del sys

if __name__ == "__main__":
    def x1():
        print "running x1"
    def x2(n):
        print "running x2(%s)" % `n`
    def x3(n, kwd=None):
        print "running x3(%s, kwd=%s)" % (`n`, `kwd`)

    register(x1)
    register(x2, 12)
    register(x3, 5, "bar")
    register(x3, "no kwd args")
