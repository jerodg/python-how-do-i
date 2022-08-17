#!/usr/bin/env python
""" How Do I -> Python -> Find substring in list of strings?

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
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
from typing import List


def method_0(data: List[str], substr: str) -> bool:
    """Method 0: Using the any() method

    Return True if any element of the iterable is true, otherwise, False.

    Notes:
        Does not provide the location of the substr.

    Args:
        data (List[str]):
        substr: str

    Returns:
        bool (bool):

    References:
        https://docs.python.org/3/library/functions.html?highlight=any#any"""

    return any(substr in x for x in data)


#
# def method_1(data: List[str], substr: str) -> bool:
#     """ Method #1: Using the find() method with a for-loop
#
#     Return the lowest (first) index in the string where substring sub is found within the slice s[start:end].
#     Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
#
#     :param data: (List[str])
#     :param substr: str
#     :return: (bool)"""
#     for i, row in data:
#         row.find(substr)
#
#         if row.find(substr) != -1:  # find returns ?
#             return True
#
#
# def method_1a(data: List[str], substr: str) -> bool:
#     """ Method #1a: Using the find() method with a list comprehension
#
#     :param data: (List[str])
#     :param substr: str
#     :return: (bool)"""
#     return True if [x for x in data if x.find(substr) != -1] else False
#
#
# def method_2(data: List[str], substr: str) -> bool:
#     """ Method #2: Using the join() method
#
#     :return: boolean (bool)"""
#     return substr in '\t'.join(data)
#
#
# def method_4(data: List[str], substr: str) -> bool:
#     """ Method #4: Using a for-loop
#
#     :return: boolean (bool)"""
#     for x in data:
#         if substr in x:
#             return True
