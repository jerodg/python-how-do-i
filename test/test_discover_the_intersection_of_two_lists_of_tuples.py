#!/usr/bin/env python3
""" Python How Do I -> Test -> Discover the Intersection of Two Lists of Tuples

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
from os.path import realpath
from random import sample
from time import perf_counter_ns
from typing import Tuple

import pyarrow as pa
# from pyarrow import orc
from pytest import fixture
import pandas as pd
from discover_the_intersection_of_two_lists_of_tuples import method0, method1, method2, method3
from print_helpers import bprint, tprint
import pyorc


def test_create_data():
    n = 1000
    r = 1000
    # pf = pd.DataFrame(data={"test_discover_the_intersection_of_two_lists_of_tuples": {"ls0": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)],
    #                                                                                   "ls1": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)]}})
    # dd.to_orc(dd.from_pandas(pf, npartitions=2), path="/tmp/orc")

    # orc.write_table(pa.table({"test_discover_the_intersection_of_two_lists_of_tuples": {
    #         "ls0": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)],
    #         "ls1": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)]}}),
    #         realpath("./data/test_data.orc"))
    #
    # data = {"ls0": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)],
    #         "ls1": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)]}

    with open(realpath("./data/test_data.orc"), "wb") as data:
        with pyorc.Writer(data, "struct<col0:string,col1:array,col2:array>") as writer:
            writer.write(("test_discover_the_intersection_of_two_lists_of_tuples",
                         [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)],
                         [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)]))


# @fixture()
# def test_data() -> Tuple:
#     # n = 100
#     # r = 100
#     # return ([divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)],
#     #         [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)])
#     return orc.read_table(realpath("./data/test_data.orc")).to_pandas()


class TestDiscoverTheIntersectionOfTwoListsOfTuples:
    def test_method0(self, test_data):
        bprint("Discover the Intersection of Two Lists of Tuples Method 0,"
               " Using sorted(), set(), &, and list comprehension")
        # ls0, ls1 = test_data
        print(test_data)
        # print(ls0)
        # print(ls1)
        st = perf_counter_ns()
        # result = method0(ls0, ls1)
        et = perf_counter_ns()

        # assert result is True

        # tprint(result)

        bprint(f"Completed in {(et - st):f} nano-seconds.")

    def test_method1(self, test_data):
        bprint("Find Substring Method 1, Using find() with a for-loop")
        td, key = test_data

        st = perf_counter_ns()
        result = method1(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f"Completed in {(et - st):f} nano-seconds.")

    def test_method2(self, test_data):
        bprint("Find Substring Method 2, Using find() with a comprehension")
        td, key = test_data

        st = perf_counter_ns()
        result = method2(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f"Completed in {(et - st):f} nano-seconds.")

    def test_method3(self, test_data):
        bprint("Find Substring Method 3, Using join()")
        td, key = test_data

        st = perf_counter_ns()
        result = method3(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f"Completed in {(et - st):f} nano-seconds.")
