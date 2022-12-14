#!/usr/bin/env python3
"""Integrate"""


def poly_integral(poly, C=0):
    """calculates the integral of a polynomial"""
    if not poly or not isinstance(poly, list):
        return None
    if not isinstance(C, (int, float)):
        return None

    integral = [C]
    for coeff in range(len(poly)):
        num = poly[coeff] / (coeff + 1)
        if num % 1 == 0:
            num = int(num)
        integral.append(num)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
