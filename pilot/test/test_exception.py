#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Authors:
# - Wen Guan, wen.guan@cern.ch, 2017
# - Paul Nilsson, paul.nilsson@cern.ch, 2018-23


import logging
import sys

from pilot.common.exception import RunPayloadFailure, PilotException

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class TestException(unittest.TestCase):
    """
    Unit tests for exceptions.
    """

    def test_run_payload_failure(self):
        """
        Make sure that es message thread works as expected.
        """

        try:
            pass
            raise RunPayloadFailure(a='message a', b='message b')
        except PilotException as ex:
            self.assertIsInstance(ex, PilotException)
            self.assertEqual(ex.get_error_code(), 1305)
            logging.info("\nException: error code: %s\n\nMain message: %s\n\nFullStack: %s" % (ex.get_error_code(),
                                                                                               str(ex),
                                                                                               ex.get_detail()))

        try:
            pass
            raise RunPayloadFailure("Test message")
        except PilotException as ex:
            self.assertIsInstance(ex, PilotException)
            self.assertEqual(ex.get_error_code(), 1305)
            logging.info("\nException: error code: %s\n\nMain message: %s\n\nFullStack: %s" % (ex.get_error_code(),
                                                                                               str(ex),
                                                                                               ex.get_detail()))
