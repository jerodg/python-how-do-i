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

setup = """
from random import choice

import faker

fake = faker.Faker(providers=['faker.providers.lorem'])
td = [fake.paragraph(nb_sentences=7, variable_nb_sentences=True) for _ in range(7)]
srch = choice(choice(td).split(' '))
"""

method_0 = """any(srch in x for x in td)"""

method_1 = """
for row in data:
    if row.find(substr) != -1:
        return True
"""

method_2 = """return True if [x for x in data if x.find(substr) != -1] else False"""

method_3 = """return substr in '\t'.join(data)"""

method_4 = """
for x in data:
    if substr in x:
        return True
"""

method_5 = """return True if [x for x in data if substr in x] else False"""


def main():
    cla = ['poetry', 'run', "fastero",
           method_0, '-n', 'any()',
           method_1, '-n', 'find() w/ for-loop',
           method_2, '-n', 'find() w/ comprehension',
           method_3, '-n', 'join()',
           method_4, '-n', 'for-loop conditional',
           method_5, '-n', 'list-comprehension conditional',
           '--setup', setup]

    args = f'poetry run fastero "{method_0}" -n "any()" "{method_1}" -n "find() w/ for-loop" --setup "{setup}"'

    # print(args)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)

    try:
        outs, errs = proc.communicate(timeout=15)
        print(outs)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        print(outs)


if __name__ == "__main__":
    main()
