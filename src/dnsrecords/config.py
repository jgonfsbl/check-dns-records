#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pylint: disable=W0102,E0712,C0103

""" DNS Records """

__updated__ = "2024-04-28 01:36:51"

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

FICH_WITH_DOMAINS = os.environ.get("FICH_WITH_DOMAINS")
