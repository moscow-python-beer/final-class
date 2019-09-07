# -*- coding: utf-8 -*-


def _init_subclass(cls, *args, **kwargs) -> None:
    raise TypeError('Subclassing final classes is restricted')


def final(cls):
    """Marks class as `final`, so it won't have any subclasses."""
    setattr(  # noqa: B010
        cls, '__init_subclass__', classmethod(_init_subclass),
    )
    return cls
