from setuptools import setup, find_packages
import os



def read_file(file):
    with open(file) as f:
        content = f.read()
    return content


readme = read_file(os.path.join(os.path.dirname(__file__), "README.md"))
license = read_file(os.path.join(os.path.dirname(__file__), "LICENSE"))

# Only the setup.py for pip was added here
# All credits go to the original author: https://github.com/sail-sg/Adan

# Copyright 2022 Garena Online Private Limited
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

setup(
    name='adan',
    version='0.0.1',
    packages=find_packages(),
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[],
    python_requires=">=3.8",
    # author="Division of Medical Image Computing, German Cancer Research Center",
    # maintainer_email='m.baumgartner@dkfz-heidelberg.de',
)
