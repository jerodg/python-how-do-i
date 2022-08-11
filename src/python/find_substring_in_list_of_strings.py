#!/usr/bin/env python3
"""
How Do I -> Python -> Find substring in list of strings?

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
"""
xml = [y for y in (x.strip() for x in __doc__.splitlines()) if y]


class FindSubstring(object):

    def __int__(self, data: list, locator: str):
        self.data: list = data
        self.locator: str = locator

    def method_0(self, locator: str) -> bool:
        """
        Method #0: Using the any() method

        :param locator: (str)

        :return: boolean (bool)
        """
        return any(locator in _ for _ in self.data)

    def method_1(self, locator: str) -> bool:
        """
        Method #1: Using the find() method

        :param locator: (str)

        :return: boolean (bool)
        """
        for i in self.data:
            if i.find(locator) != -1:
                return True

    def method_2(self, locator: str) -> bool:
        """
        Method #2: Using the join() method

        :param locator: (str)

        :return: boolean (bool)
        """
        return locator in '\t'.join(self.data)

    def method_3(self, locator: str) -> bool:
        """
        Method #4: Using a list comprehension

        :param locator: (str)

        :return: boolean (bool)
        """
        return True if [x for x in self.data if x.find(locator) != -1] else False
