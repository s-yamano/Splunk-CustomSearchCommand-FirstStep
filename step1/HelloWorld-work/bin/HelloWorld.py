#!/usr/bin/env python

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import \
    dispatch, GeneratingCommand, Configuration, Option, validators

@Configuration()
class HelloWorldCommand(GeneratingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """
    def generate(self):
        return [{"_time": time.time(), "greeting": "hello, world"}]


dispatch(HelloWorldCommand, sys.argv, sys.stdin, sys.stdout, __name__)
