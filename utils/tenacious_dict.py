#!/usr/bin/env python3
"""Python How Do I -> Test -> Discover the Intersection of Two Lists of Tuples

Copyright ©2016-2022 Jerod Gawne <https://github.com/jerodg/>

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
from os.path import realpath, exists
import ujson
import msgpack
from kill_protect import KillProtect


class TenaciousDict(dict):

    def __init__(self, db_path: str, db_mode: str = "a", db_format: str = "msgpack"):
        """Init

        :param db_path: (str) Relative or absolute path to database file
        :param db_mode: (str) One of:
                                  a => append if exists, create new if not
                                  r => read-only
                                  w => write-over
        :param db_format: (str) One of:
                                    csv => plain-text csv
                                    json => plain-text json
                                    pickle => binary pickle format
                                    msgpack => binary msgpack format
        """
        self.db_path: str = realpath(db_path)
        self.db_mode: str = db_mode
        self.db_format: str = db_format

        super().__init__()
        self.load()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()

    def load(self):
        if self.db_mode == "w":
            return

        if not exists(self.db_path):
            return

        m = "b" if self.db_mode in ["pickle", "msgpack"] else "t"

        match self.db_format:
            case "csv":
                with open(self.db_path, f"r{m}") as db:
                    self.update(msgpack.load(db))
            case "pickle":
                with open(self.db_path, f"r{m}") as db:
                    self.update(msgpack.load(db))
            case "json":
                with open(self.db_path, f"r{m}") as db:
                    self.update(ujson.load(db))
            case "msgpack":
                with open(self.db_path, f"r{m}") as db:
                    self.update(msgpack.load(db))

    def save(self):
        with KillProtect():
            m = "b" if self.db_mode in ["pickle", "msgpack"] else "t"

            match self.db_mode:
                case "a":
                    with open(self.db_path, f"w{m}+") as db:
                        msgpack.dump(self, db)
                case "r":
                    return
                case "w":
                    with open(self.db_path, f"w{m}") as db:
                        msgpack.dump(self, db)


if __name__ == '__main__':
    # print(__doc__)
    from random import sample
    with TenaciousDict(db_path="./test.td") as td:
        # n = 5
        # r = 5
        # td['nacho'] = {"ls0": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)],
        #                 "ls1": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)]}
        print(td)
