#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2016 MarkLogic Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0#
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# working directory=tests
import unittest
import logging
from newrelic_marklogic_plugin.http_utils import HTTPUtil

log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)
host= "node1"

class HTTPUtilTests(unittest.TestCase):
    def testRest1(self):
        response = HTTPUtil.http_get("http", host, 8002, "/manage/v2?view=status", "admin", "admin", "public",
                                     "DIGEST")
        assert response

    def testRest2(self):
        response = HTTPUtil.http_get(scheme="http",
                                     host=host,
                                     port=8002,
                                     path="/manage/v2?view=status",
                                     user="admin",
                                     passwd="admin",
                                     realm="public",
                                     auth="DIGEST")
        assert response

    def testRest3(self):
        response = HTTPUtil.http_get(url="http://www.google.com", headers={'Accept': 'text/html'}, format="html")
        log.debug(response)
        assert response

    def testRestPost(self):
        response = HTTPUtil.http_post(scheme="https",
                                      url="https://platform-api.newrelic.com/platform/v1/metrics",
                                      headers={'Accept': 'application/json',
                                               'Content-Type': 'application/json',
                                               'X-License-Key': 'e8cf9b3d7aaca22a8632c7e01a14f8e722519b8a'},
                                      payload={
                                          "agent": {
                                              "host": host,
                                              "pid": 1234,
                                              "version": "1.0.0"
                                          },
                                          "components": [{
                                              "name": "marklogic_unittest",
                                              "guid": "com.marklogic",
                                              "duration": 60,
                                              "metrics": {
                                                  "Component/MarkLogic[UnitTest]": 50
                                              }
                                          }]
                                      })
        assert response
