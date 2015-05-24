import inspect
from graph_tools import topsort
from utils import result
from functools import wraps


def get_deps(fn, namespace):
    deps = {}
    q = [fn]
    ns = result(namespace)
    while len(q) > 0:
        fn = q.pop()
        args = inspect.getargspec(fn).args
        deps[fn.func_name] = args
        for func_name in args:
            if func_name not in deps:
                q.append(ns[func_name])
    return deps


def execute_with_deps(fn, namespace):
    env = {}
    deps = get_deps(fn, namespace=namespace)
    l = result(namespace)
    for n in reversed(list(topsort(deps))):
        kwargs = {func_name: env[func_name] for func_name in deps[n]}
        env[n] = l[n](**kwargs)
    return env[fn.func_name]


def injected(fn, namespace=lambda: globals()):
    @wraps(fn)
    def wrapped():
        return execute_with_deps(fn, namespace)
    return wrapped
