"""
Proof of concept of doing dependency injection using
functions.

It is not meant to be used anywhere, this work's sole
purpose was to better understand the concept and how
to implement it. To keep it simple, I used functions
and argument names to specify dependencies.

def a(b): return b*2
def b(): return 1
def c(): return 4

call(a, {'b': b})
call(a, {'b': c}) # mocking !

injected_a = injected(a, {'b': b})

# here you can call injected_a "normally"
injected_a()
"""

import inspect
from graph_tools import topsort
from utils import result
from functools import wraps


def get_deps(fn, namespace):
    deps = {}
    q = [fn]
    ns = result(namespace)
    # function -> name
    # we do not rely on fn.func_name since dependencies
    # can be mocked
    rv_ns = {v: k for k, v in namespace.iteritems()}
    while len(q) > 0:
        fn = q.pop()
        args = inspect.getargspec(fn).args
        deps[rv_ns[fn]] = args
        for func_name in args:
            if func_name not in deps:
                q.append(ns[func_name])
    return deps


def call(fn, namespace):
    """
    Execute a function with dependency injection. The namespace
    is the container of all the dependencies

    >>> def a(b): return b*2
    >>> def b(): return 1
    >>> def c(): return 4
    >>> call(a, {'a': a, 'b': b})
    2
    >>> call(a, {'a': a, 'b': c}) # mocking !
    8
    """
    env = {}
    deps = get_deps(fn, namespace=namespace)
    l = result(namespace)
    for n in reversed(list(topsort(deps))):
        kwargs = {func_name: env[func_name] for func_name in deps[n]}
        env[n] = l[n](**kwargs)
    return env[fn.func_name]


def injected(fn, namespace=lambda: globals()):
    """
    Make a closure with dependency already solved so that you can
    call the function normally without using call

    >>> def a(b): return b*2
    >>> def b(): return 1
    >>> def c(): return 4
    >>> ns = {'a': a, 'b': b, 'c': c}
    >>> a = injected(a, namespace=ns)
    >>> a()
    2
    """
    @wraps(fn)
    def wrapped():
        return call(fn, namespace)
    return wrapped
