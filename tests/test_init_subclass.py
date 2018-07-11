# -*- coding: utf-8 -*-

import pytest

from final_class import final


class WithExistingInitSubClass(object):
    """We need this class to test that we do not miss existing hooks."""

    def __init_subclass__(cls, key, name, **kwargs):
        """Just some simple logics."""
        super().__init_subclass__(**kwargs)
        cls.key = key
        cls.name = name


@final
class UsingHook(WithExistingInitSubClass, key='some', name='Nikita'):
    """In this class we use the existing hook."""


def test_preserves_hook():
    """Ensures that existing hooks are still executed."""
    assert UsingHook.key == 'some'
    assert UsingHook.name == 'Nikita'


def test_no_subclasses():
    """Ensures that subclasses are still restricted."""
    with pytest.raises(TypeError):
        class Child(UsingHook):
            check = False
