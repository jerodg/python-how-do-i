#!/usr/bin/env python3
""" How Do I -> Python -> Test -> Dict ->

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
from time import perf_counter_ns

from pytest import fixture

from print_helpers import bprint, tprint


@fixture()
def test_data() -> list:
    return []


class TestFindUniqueKeysFromListOfDicts:
    def test_method_0(self, test_data):
        bprint("Method 0, ")
        st = perf_counter_ns()
        result = ""
        et = perf_counter_ns()

        assert result == ""

        tprint(result)

        bprint(f"Completed in {(et - st):f} nano-seconds.")
