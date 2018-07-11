# -*- coding: utf-8 -*-

from typing import Type, TypeVar

T = TypeVar('T')


def _init_subclass(cls: Type[T], *args, **kwargs) -> None:
    raise TypeError('Subclassing final classes is restricted')


def final(cls: Type[T]) -> Type[T]:
    """Marks class as `final`, so it won't have any subclasses."""
    setattr(cls, '__init_subclass__', classmethod(_init_subclass))
    return cls
