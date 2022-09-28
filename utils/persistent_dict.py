#!/usr/bin/env python3
"""Python How Do I -> Utils -> Tinacious Dict

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
import csv
import json
import pickle
from copy import deepcopy
from logging import DEBUG, getLogger, INFO
from os import access, chmod, fdopen, R_OK, remove
from os.path import realpath
from shutil import move
from tempfile import mkstemp
from typing import NoReturn
import msgpack

logger = getLogger(__name__)
DBG = logger.isEnabledFor(DEBUG)
NFO = logger.isEnabledFor(INFO)


# todo: add HDF5 support
# todo: add zstd compression
# todo: implement features from: https://github.com/pdrb/dbj/blob/master/dbj.py
# - find(keys), insert, delete, many, autosave, killprotect, size, update, sort, search text(values),
# - backups(versioning)

class PersistentDict(dict):
    """Persistent, In-Memory dictionary
     - Auto-Discovery of input-file type
     - Output file-format: pickle, json, or csv"""

    def __init__(self, path: str, mode: str = 'c', access: int = None, fmt: str = 'pickle'):
        """
        :param path: str
        :param mode: str; (r|c|n); r(eadonly), c(reate), n(ew)
        :param access: int; Octal
        :param fmt: str; (csv|json|pickle|msgpack)"""
        super().__init__()
        self.PATH: str = path
        self.MODE: str = mode
        self.ACCESS: int = access
        self.FORMAT: str = fmt

        self.__load()

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sync()

    def __deepcopy__(self, requesteddeepcopy) -> object:
        """
        :param requesteddeepcopy:
        :return: PersistentDict()"""
        return deepcopy(self)

    def sync(self) -> NoReturn:
        """
        Save to temp file
        Overwrite persistence file with temp
        Set access permissions

        :return: NoReturn"""
        if self.MODE == 'r':
            if NFO:
                logger.info('Mode set as read-only; returning without committing to disk.')
            return

        # Reading an empty dictionary when using json or csv format causes an exception
        if (not self.items()) and (self.FORMAT != 'pickle'):
            if NFO:
                logger.info('Dictionary is empty; nothing to write')
            return

        fd, path = mkstemp(suffix=b'.tmp', text=False if self.FORMAT == 'pickle' else True)

        try:
            with fdopen(fd, 'wb+' if self.FORMAT in ['pickle', 'msgpack'] else 'w+') as fileobj:
                if self.FORMAT == 'csv':
                    csv.writer(fileobj).writerows(self.items())
                elif self.FORMAT == 'json':
                    json.dump(self, fileobj, separators=(',', ':'))
                elif self.FORMAT == 'pickle':
                    pickle.dump(obj=dict(self), file=fileobj, protocol=pickle.HIGHEST_PROTOCOL)
                elif self.FORMAT == 'msgpack':
                    msgpack.dump(self, fileobj)
                else:
                    raise NotImplementedError(f'Unknown format: {self.FORMAT}')
        except OSError as ose:
            logger.exception(ose)
            remove(path)

        try:
            move(path, self.PATH)
        except OSError as ose:
            logger.exception(ose)

        if self.ACCESS:
            try:
                chmod(self.PATH, self.ACCESS)
            except OSError as ose:
                logger.exception(ose)

        if NFO:
            logger.info('Sync to disk complete.')

    def __load(self) -> NoReturn:
        """:return: NoReturn"""
        if self.MODE == 'n':
            if NFO:
                logger.info('File mode set to n(ew); not loading existing file.')
            return
        elif access(self.PATH, R_OK):
            with open(self.PATH, 'rb' if self.FORMAT in ['pickle', 'msgpack'] else 'r') as fileobj:
                for loader in (pickle.load, json.load, csv.reader, msgpack.unpackb):
                    fileobj.seek(0)
                    try:
                        return self.update(loader(fileobj))
                    except Exception as e:
                        logger.exception(e)
                        raise ValueError('File not in a supported format')
        if NFO:
            logger.info('Existing file sucessfully loaded.')


if __name__ == '__main__':
    # print(__doc__)
    from random import sample

    with PersistentDict(realpath('./testing_d.td'), fmt='msgpack') as tdb:
        # print(tdb)
        n = 5
        r = 5
        tdb['nacho'] = {"ls0": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)],
                        "ls1": [divmod(ele, r + 1) for ele in sample(range((r + 1) * (r + 1)), n)]}
