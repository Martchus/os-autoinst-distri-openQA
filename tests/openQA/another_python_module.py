from testapi import *


def run(self):
    record_soft_failure("log soft failure for testing purposes")


def test_flags(self):
    return {'fatal': 1}
