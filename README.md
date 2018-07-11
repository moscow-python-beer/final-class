# final_class

[![wemake.services](https://img.shields.io/badge/style-wemake.services-green.svg?label=&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](http://wemake.services) [![Build Status](https://travis-ci.org/wemake-services/final_class.svg?branch=master)](https://travis-ci.org/wemake-services/final_class)

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
