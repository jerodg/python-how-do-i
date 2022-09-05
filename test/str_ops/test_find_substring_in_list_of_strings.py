#!/usr/bin/env python3
""" How Do I -> Python -> Test -> Find substring in list of strings?

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
from random import choice
from time import perf_counter_ns

import faker
from pytest import fixture

from print_helpers import bprint, tprint
from src.str_ops.find_substring_in_list_of_strings import method_0, method_1, method_1a, method_2, method_3


@fixture()
def test_data() -> tuple:
    fake = faker.Faker(providers=["faker.providers.lorem"])
    td = [fake.paragraph(nb_sentences=7, variable_nb_sentences=True) for _ in range(7)]
    srch = choice(choice(td).split(" "))

    return td, srch


class TestFindSubstringInListOfStrings:
    def test_method_0(self, test_data):
        bprint('Find Substring Method 0, Using any()')
        td, key = test_data

        st = perf_counter_ns()
        result = method_0(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f'Completed in {(et - st):f} nano-seconds.')

    def test_method_1(self, test_data):
        bprint('Find Substring Method 1, Using find() with a for-loop')
        td, key = test_data

        st = perf_counter_ns()
        result = method_1(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f'Completed in {(et - st):f} nano-seconds.')

    def test_method_2(self, test_data):
        bprint('Find Substring Method 1a, Using find() with a comprehension')
        td, key = test_data

        st = perf_counter_ns()
        result = method_1a(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f'Completed in {(et - st):f} nano-seconds.')

    def test_method_3(self, test_data):
        bprint('Find Substring Method 2, Using join()')
        td, key = test_data

        st = perf_counter_ns()
        result = method_2(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f'Completed in {(et - st):f} nano-seconds.')

    def test_method_4(self, test_data):
        bprint('Find Substring Method 3, Using a for-loop')
        td, key = test_data

        st = perf_counter_ns()
        result = method_3(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f'Completed in {(et - st):f} nano-seconds.')

    def test_method_5(self, test_data):
        bprint('Find Substring Method 4, Using a comprehension')
        td, key = test_data

        st = perf_counter_ns()
        result = method_3(td, key)
        et = perf_counter_ns()

        assert result is True

        tprint(result)

        bprint(f'Completed in {(et - st):f} nano-seconds.')

    def test_benchmark(self):

        proc = subprocess.Popen(realpath('../../bench/str_ops/find_substring_in_list_of_strings'), stdout=subprocess.PIPE)

        try:
            outs, errs = proc.communicate(timeout=15)
            print(outs)
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            print(outs)
