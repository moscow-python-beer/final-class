# -*- coding: utf-8 -*-

from final_class import final


def test_is_class(final_class):
    """Ensures that we are still working with class."""
    assert isinstance(final_class, type)


def test_is_the_same_class(regular_class):
    """Ensures that we are still working with the same class."""
    assert regular_class is final(regular_class)


def test_is_instancable(final_class):
    """Ensures that we can still creates instances for this class."""
    assert isinstance(final_class(), final_class)


def test_has_attributes(final_class):
    """Ensures that we still have declared attributes."""
    assert final_class.regular_value == 1
    assert final_class().regular_value == 1
