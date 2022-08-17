#!/usr/bin/env python3
"""
How Do I -> Python -> Test -> Find substring in list of strings?

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
from src.python.find_substring_in_list_of_strings import method_0
import faker
from random import choice
from pytest import fixture
from src.python.utils import bprint, tprint


@fixture()
def test_data() -> tuple:
    fake = faker.Faker(providers=["faker.providers.lorem"])
    td = [fake.paragraph(nb_sentences=7, variable_nb_sentences=True) for _ in range(7)]
    srch = choice(choice(td).split(" "))

    return td, srch


class TestFindSubstringInListOfStrings:
    def test_method_0(self, test_data):
        bprint('Find Substring Method 0, Using Any()')
        td, key = test_data
        result = method_0(td, key)
        tprint(result)

        assert result is True
