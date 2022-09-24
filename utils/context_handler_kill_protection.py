#!/usr/bin/env python3
"""Python How Do I -> Utils -> Context Handler Kill Protection

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
import signal
import sys


class ContextHandlerKillProtection(object):
    """Context Manager Protection From Common Kill Signals"""

    def __init__(self):
        self.killed = False

    def kill_handler(self, signum, frame):
        """

        :param signum:
        :param frame:
        :return:
        """
        self.killed = True

    def __enter__(self):
        """

        :return:
        """
        self.prev_sigint = signal.signal(signal.SIGINT, self.kill_handler)
        self.prev_sigterm = signal.signal(signal.SIGTERM, self.kill_handler)

    def __exit__(self, type, value, traceback):
        """

        :param type:
        :param value:
        :param traceback:
        :return:
        """
        if self.killed:
            sys.exit(0)

        signal.signal(signal.SIGINT, self.prev_sigint)
        signal.signal(signal.SIGTERM, self.prev_sigterm)
