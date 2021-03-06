# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
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
# =============================================================================

from .tensorproduct import tensorproduct
from .pauligraph import PauliGraph
from .jsonutils import convert_dict_to_json, convert_json_to_dict
from .random_matrix_generator import random_unitary, random_h2_body, random_h1_body
from .decimal_to_binary import decimal_to_binary
from .summarize_circuits import summarize_circuits
from .cnx import cnx
from .entangler_map import get_entangler_map, validate_entangler_map
from .dataset_helper import (get_feature_dimension, get_num_classes,
                             split_dataset_to_data_and_labels, map_label_to_class_name,
                             reduce_dim_to_via_pca)
from .qpsolver import optimize_svm


__all__ = ['tensorproduct',
           'PauliGraph',
           'convert_dict_to_json',
           'convert_json_to_dict',
           'random_unitary',
           'random_h2_body',
           'random_h1_body',
           'decimal_to_binary',
           'summarize_circuits',
           'cnx',
           'get_entangler_map',
           'validate_entangler_map',
           'get_feature_dimension',
           'get_num_classes',
           'split_dataset_to_data_and_labels',
           'map_label_to_class_name',
           'reduce_dim_to_via_pca',
           'optimize_svm']
