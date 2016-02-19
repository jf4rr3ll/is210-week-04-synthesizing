#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that converts Fahrenheit to Celsius
    and displays the result as a decimal.
    """

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Defines a function that converts Fahrenheit to Celsius.

    Args:
        degrees(dec): Degrees in Fahrenheit.

    Returns:
        decimal: Degrees converted to Celsius.

    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(32)
        Decimal('0')
    """

return ((decimal.Decimal(degrees) - 32) * 5) / 9


def celsius_to_kelvin(degrees):
    """Defines a function that converts Celsius to Kelvin

    Args:
        degrees(dec): Degrees in Celsius.

    Returns:
        decimal: Degrees converted to Kelvin.

    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> celsius_to_kelvin(0)
        Decimal('273.15')
    """


return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """Defines a function that converts Fahrenheit to Kelvin

    Args:
        degrees(dec): Degrees in Fahrenheit

    Returns:
        decimal: Degrees convertet to Kelvin

    Examples:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')

        >>>fahrenheit_to_kelvin(32)
        Decimal('273.16')
    """

return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
