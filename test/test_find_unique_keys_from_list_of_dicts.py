#!/usr/bin/env python3
""" How Do I -> Python -> Test -> Dict -> Find Unique Keys from List of Dicts

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
import subprocess
from os.path import realpath
from time import perf_counter_ns
from typing import List

from pytest import fixture

from find_unique_keys_from_list_of_dicts import method_0, method_1, method_2
from print_helpers import bprint, tprint


@fixture()
def test_data() -> List[dict]:
    return [
        {"mk1": "mk1-stuff", "mk2": "mk2-stuff", "mk3": "N/A"},
        {"mk4": "mk4-stuff", "mk5": "mk5-stuff", "mk6": 100837363},
    ]


class TestFindUniqueKeysFromListOfDicts:
    def test_method_0(self, test_data):
        bprint("Find Unique Keys Method 0, Using Chain itertools")

        st = perf_counter_ns()
        result = method_0(test_data)
        et = perf_counter_ns()

        result.sort()

        assert result == ["mk1", "mk2", "mk3", "mk4", "mk5", "mk6"]

        tprint(result)

        bprint(f"Completed in {(et - st):f} nano-seconds.")

    def test_method_1(self, test_data):
        bprint("Find Unique Keys Method 1, Using list/dict Comprehension")

        st = perf_counter_ns()
        result = method_1(test_data)
        et = perf_counter_ns()

        result.sort()

        assert result == ["mk1", "mk2", "mk3", "mk4", "mk5", "mk6"]

        tprint(result)

        bprint(f"Completed in {(et - st):f} nano-seconds.")

    def test_method_2(self, test_data):
        bprint("Find Unique Keys Method 2, Using keys(),extend(),list() and set() methods")

        st = perf_counter_ns()
        result = method_2(test_data)
        et = perf_counter_ns()

        result.sort()

        assert result == ["mk1", "mk2", "mk3", "mk4", "mk5", "mk6"]

        tprint(result)

        bprint(f"Completed in {(et - st):f} nano-seconds.")

    def test_benchmark(self):

        proc = subprocess.Popen(realpath("bench_find_unique_keys_from_list_of_dicts/run.sh"), stdout=subprocess.PIPE)

        try:
            outs, errs = proc.communicate(timeout=15)
            print(outs)
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            print(outs)
