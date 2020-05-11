#!/usr/bin/env python

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import \
    dispatch, EventingCommand, Configuration, Option, validators


@Configuration()
class ToUpperCommand(EventingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """
    def transform(self, events):
       # Put your event transformation code here
        for event in events:
            for field in self.fieldnames:
                if field in event:
                    event[field] = event[field].upper()
            yield event
        return

dispatch(ToUpperCommand, sys.argv, sys.stdin, sys.stdout, __name__)
