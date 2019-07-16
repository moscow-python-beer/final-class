# final_class

[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) [![Build Status](https://travis-ci.org/moscow-python-beer/final-class.svg?branch=master)](https://travis-ci.org/moscow-python-beer/final-class) [![Coverage Status](https://coveralls.io/repos/github/moscow-python-beer/final-class/badge.svg?branch=master)](https://coveralls.io/github/moscow-python-beer/final-class?branch=master) [![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Final classes for `python3.6+`.


## Features

- No metaclass conflicts
- No runtime overhead
- No dependencies
- Type hints included
- Designed to be as simple as possible


## Why?

In languages like `java` we have a nice way
to restrict subclassing any class by making it `final`:

```java
public final class SomeClass {
  // ...
}
```

In `python` we don't have such feature out of the box.
That's where `final_class` library comes in!


## Installation

```bash
pip install final_class
```


## Usage

```python
from final_class import final


@final
class Example(object):  # You won't be able to subclass it!
    ...


class Error(Example):  # Raises `TypeError`
    ...
```


## License

MIT.
