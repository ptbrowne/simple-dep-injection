# Simple dependency injection

Proof of concept of doing dependency injection using functions.

- [API](#api)
    - [call](#call)
    - [injected](#injected)

It is not meant to be used anywhere, this work's sole
purpose was to better understand the concept and how
to implement it. To keep it simple, I used functions
and argument names to specify dependencies.


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
