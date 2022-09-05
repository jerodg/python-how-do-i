#!/usr/bin/env python3
""" How Do I -> Python -> Utils

Copyright © 2019-2022 Jerod Gawne <https://github.com/jerodg/>

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
from typing import Any, Iterable, NoReturn, Optional


def bprint(message) -> NoReturn:
    """Banner Print

    Args:
        message: (str)

    Returns:
        (NoReturn)"""
    msg = f'\n▃▅▇█▓▒░۩۞۩ {message.center(58)} ۩۞۩░▒▓█▇▅▃'
    print(msg)


def tprint(data: Any, top: Optional[int] = None) -> NoReturn:
    """Test Print

    Args:
        data: (Any)
        top: (int)

    Returns:
        (NoReturn)"""
    if type(data) is Iterable:
        if top:
            top_hdr = f'Top {top} ' if top else ''
            print(f'{top_hdr}Result{"s" if len(data) > 1 else ""}: {len(data)}')
            print(*data[:top], sep='\n')
        else:
            print(f'Result{"s" if len(data) > 1 else ""}:')
            print(*data, sep='\n')
    else:
        print(f'Result:\n-> {data}')


if __name__ == '__main__':
    print(__doc__)
