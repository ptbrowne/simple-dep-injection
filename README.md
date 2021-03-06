# Simple dependency injection

Proof of concept of doing dependency injection using functions.

- [API](#api)
    - [call](#call)
    - [injected](#injected)

Dependency injection
====================

Dependency injection is a form of Inversion of Control where
the user a service does not instantiate/call the service but where
the service is instantiated/called by the dependency injection
framework.

Here, services are approximated as functions. If a functions depends
on the result of another function to properly execute, it specifies the
function to be called in its arguments. To execute a function, the
dependency injection framework, here `call`, will gather the dependencies
of the functions, gather the dependencies of the dependencies, all the way
down and will find the right execution order with a `topsort`. It will then
call each dependency in order, passing the results to the functions that
need it.

DI's primary goal is decoupling and minimal knowledge of the dependencies.
Indeed, the user of a service does not need to know how to instantiate this
service as it is the dependency framework that will sort out how to instantiate
it (along with its dependencies). It also allows for easier testing as the
dependencies of a module under test can be mocked.


## API

- [call](#call)
- [injected](#injected)


### call

Execute a function with dependency injection.

The namespace is the container of all the dependencies.

```python
>>> def a(b): return b*2
>>> def b(): return 1
>>> def c(): return 4
>>> call(a, {'a': a, 'b': b})
2
>>> call(a, {'a': a, 'b': c}) # mocking !
8
```


### injected

Returns a function that can be called without using call.


```python
>>> def a(b): return b*2
>>> def b(): return 1
>>> def c(): return 4
>>> ns = {'a': a, 'b': b, 'c': c}
>>> a = injected(a, namespace=ns)
>>> a()
2
```
