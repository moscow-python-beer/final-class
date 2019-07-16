# -*- coding: utf-8 -*-

import pytest


def test_subclassing_final(final_class):
    """Ensures that we can not subclass a final class."""
    with pytest.raises(
        TypeError, match='Subclassing final classes is restricted',
    ):
        class Child(final_class):
            fail = 0


def test_subclassing_final_as_mixin(final_class, regular_class):
    """Ensures that we can not use a final class as a mixin."""
    with pytest.raises(TypeError):
        class Child(final_class, regular_class):
            fail = 0

    with pytest.raises(TypeError):
        class OtherChild(regular_class, final_class):
            fail = 0
