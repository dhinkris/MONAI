# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import torch
from parameterized import parameterized

from monai.networks.nets import (
    se_resnet50,
    se_resnet101,
    se_resnet152,
    se_resnext50_32x4d,
    se_resnext101_32x4d,
    senet154,
)

input_param = {"spatial_dims": 3, "in_channels": 2, "num_classes": 10}

TEST_CASE_1 = [senet154(**input_param)]
TEST_CASE_2 = [se_resnet50(**input_param)]
TEST_CASE_3 = [se_resnet101(**input_param)]
TEST_CASE_4 = [se_resnet152(**input_param)]
TEST_CASE_5 = [se_resnext50_32x4d(**input_param)]
TEST_CASE_6 = [se_resnext101_32x4d(**input_param)]


class TestSENET(unittest.TestCase):
    @parameterized.expand([TEST_CASE_1, TEST_CASE_2, TEST_CASE_3, TEST_CASE_4, TEST_CASE_5, TEST_CASE_6])
    def test_senet154_shape(self, net):
        input_data = torch.randn(5, 2, 64, 64, 64)
        expected_shape = (5, 10)
        net.eval()
        with torch.no_grad():
            result = net.forward(input_data)
            self.assertEqual(result.shape, expected_shape)
