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
    count = Option(require=False, validate=validators.Integer(), default=1)

    def generate(self):

        greeting_msg = "hello, world"
        for i in range(0, self.count):
            yield {"_time": time.time(), "greeting": greeting_msg, "_raw": greeting_msg}


dispatch(HelloWorldCommand, sys.argv, sys.stdin, sys.stdout, __name__)
