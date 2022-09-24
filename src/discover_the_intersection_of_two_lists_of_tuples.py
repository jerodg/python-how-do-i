#!/usr/bin/env python3
"""Python How Do I -> Discover the Intersection of Two Lists of Tuples

Copyright ©2022 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

Reference:
https://mathworld.wolfram.com/Circle-CircleIntersection.html
https://en.wikipedia.org/wiki/Circle"""


def method0(ls0: list, ls1: list) -> set:
    """Using sorted(), set(), &, and list comprehension

    :param ls0: (list)
    :param ls1: (list)
    :return: (set)"""
    return set([tuple(sorted(x)) for x in ls0]) & set([tuple(sorted(y)) for y in ls1])


def method1(ls0: list, ls1: list) -> set:
    """Using list comprehension, map(), frozenset(), and &

    :param ls0: (list)
    :param ls1: (list)
    :return: (set)"""
    return set(map(frozenset, ls0)) & set(map(frozenset, ls1))


def method2(ls0: list, ls1: list) -> list:
    """Using list comprehension

    :param ls0: (list)
    :param ls1: (list)
    :return: (list)"""
    return [x for x in ls0 for y in ls1 if x == y]


def method3(ls0: list, ls1: list) -> list:
    """Using set.intersection()

    :param ls0: (list)
    :param ls1: (list)
    :return: (list)"""
    return list(set(ls0).intersection(set(ls1)))


if __name__ == "__main__":
    print(__doc__)
