# Copyright 2019 Nokia
  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import json
import jinja2
from ansible.plugins.filter.core import regex_search


class LocalstorageTest(unittest.TestCase):

    def setUp(self):
        env = jinja2.Environment(
           loader=jinja2.FileSystemLoader('./role/templates')
           )
        env.filters['search'] = regex_search
        env.tests['search'] = regex_search
        self.template = env.get_template('localstorage.j2')

    def ordered(self, obj):
        if isinstance(obj, dict):
            return sorted((k, self.ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(self.ordered(x) for x in obj)
        return obj

    def verify(self, usecase):
        with open('./tests/inputs/%s.json' % usecase) as data:
            inventory = json.load(data)
        rendered = self.template.render(inventory)
        actual = json.loads(rendered)
        with open('./tests/outputs/%s.json' % usecase) as data:
            expected = json.load(data)
        self.assertEqual(self.ordered(actual), self.ordered(expected))

    def test_single_profile(self):
        self.verify('single_profile')

    def test_double_profile(self):
        self.verify('double_profile')

    def test_triple_profile(self):
        self.verify('triple_profile')

    def test_missing_volume(self):
        self.verify('missing_volume')

    def test_missing_volume2(self):
        self.verify('missing_volume2')

    def test_fewer_partition(self):
        self.verify('fewer_partition')

    def test_multinode_hybrid1(self):
        self.verify('multinode_hybrid1')

    def test_multinode_hybrid2(self):
        self.verify('multinode_hybrid2')

    def test_multinode_hybrid3(self):
        self.verify('multinode_hybrid3')

    def test_multinode_hybrid4(self):
        self.verify('multinode_hybrid4')

    def test_multinode_hybrid5(self):
        self.verify('multinode_hybrid5')

    def test_multinode_hybrid6(self):
        self.verify('multinode_hybrid6')

    def test_multinode_hybrid7(self):
        self.verify('multinode_hybrid7')

    def test_multinode_hybrid8(self):
        self.verify('multinode_hybrid8')

    def test_multinode_hybrid9(self):
        self.verify('multinode_hybrid9')

if __name__ == '__main__':
    unittest.main()
