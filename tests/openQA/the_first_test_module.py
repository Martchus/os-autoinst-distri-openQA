from testapi import *


def run(self):
    record_soft_failure("the first test module")


def test_flags(self):
    return {'fatal': 1}
