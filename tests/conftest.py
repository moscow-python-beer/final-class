# -*- coding: utf-8 -*-

import pytest

from final_class import final


@final
class FinalClass(object):
    """This class is used for testing final classes."""

    regular_value = 1


class RegularClass(object):
    """This class is used as a regular class for testing."""

    some_value = 8


@pytest.fixture()
def final_class():
    """Providing FinalClass into the tests."""
    return FinalClass


@pytest.fixture()
def regular_class():
    """Providing RegularClass into the tests."""
    return RegularClass
