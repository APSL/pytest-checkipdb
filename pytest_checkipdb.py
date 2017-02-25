# -*- coding: utf-8 -*-

import pytest

to_check = [
    'import ipdb; ipdb.set_trace()',
    'import ipdb',
    'ipdb.set_trace()',
    'ipdb.'
]


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption(
        '--cipdb',
        action='store_true',
        dest='check_ipdb',
        help='perform ipdb sanity check on .py files'
    )


def pytest_collect_file(parent, path):
    config = parent.config
    if path.ext != '.py' or not config.option.check_ipdb:
        return
    return CheckIpdbItem(path, parent=parent)


class CheckIpdbItem(pytest.Item, pytest.File):

    def __init__(self, path, parent):
        super(CheckIpdbItem, self).__init__(path, parent=parent)
        self.raw_content = self.fspath.open().read()

    def runtest(self):
        for item in to_check:
            if item in self.raw_content:
                raise CheckIpdbError('Detected: "{}" in "{}"'.format(item, self.fspath))

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(CheckIpdbError):
            return excinfo.value.args[0]
        return super(CheckIpdbItem, self).repr_failure(excinfo)


class CheckIpdbError(Exception):
    """ indicates an error during cipdb checks. """
