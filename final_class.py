# -*- coding: utf-8 -*-

from typing import Type, TypeVar

_ClassDef = TypeVar('_ClassDef', bound=Type)


def _init_subclass(cls: _ClassDef, *args, **kwargs) -> None:
    raise TypeError('Subclassing final classes is restricted')


def final(cls: _ClassDef) -> _ClassDef:
    """Marks class as `final`, so it won't have any subclasses."""
    setattr(  # noqa: B010
        cls, '__init_subclass__', classmethod(_init_subclass),
    )
    return cls
