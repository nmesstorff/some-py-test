"""
# -*- coding: utf-8 -*-
File: build.py
Author: Norman Messtorff
Email: normes@normes.org
Github: https://github.com/nmesstorff
Description: Some tests round about python stuff
"""

from pybuilder.core import use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.flake8")
use_plugin("python.distutils")

default_task = "publish"
