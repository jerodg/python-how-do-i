#!/usr/bin/env python3
"""Python How Do I -> Test -> Discover the Intersection of Two Lists of Tuples

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
import rich
import os

LOGGING_CONFIG = {
        'version':                  1,
        'disable_existing_loggers': False,
        'propagate':                True,
        'formatters':               {
                'terse': {
                        'class':   'logging.Formatter',
                        'style':   '{',
                        'datefmt': '%I:%M:%S',
                        'format':  '<{levelname}> [{name}] ({lineno}) {asctime} => {message}'
                }
        },
        'handlers':                 {
                'terse_console': {
                        'level':     'DEBUG',
                        'class':     'logging.StreamHandler',
                        'formatter': 'terse',
                        'stream':    'ext://sys.stdout'
                },
                'rich': {
                        'level': 'DEBUG',
                        'class': 'rich.logging.RichHandler',
                        'formatter': 'terse',
                        'stream': 'ext://sys.stdout'
                        }
                # 'file':          {
                #         'level':       'INFO',
                #         'class':       'logging.handlers.TimedRotatingFileHandler',
                #         'formatter':   'terse',
                #         'filename':    os.path.realpath('./logs/bricata.log'),
                #         'when':        'd',
                #         'interval':    1,
                #         'backupCount': 30
                # },
                # 'file1':         {
                #         'level':       'INFO',
                #         'class':       'logging.handlers.TimedRotatingFileHandler',
                #         'formatter':   'terse',
                #         'filename':    os.path.realpath('./logs/autodidact.log'),
                #         'when':        'd',
                #         'interval':    1,
                #         'backupCount': 30
                # }
        },
        # 'loggers':                  {
        #         'autodidact': {
        #                 'handlers': ['file'],
        #                 'level':    'WARNING'
        #         }
        #
        # },
        'root':                     {
                'handlers': ['rich'],
                'level':    'DEBUG'
        }
}
