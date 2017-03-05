# -*- coding: utf-8 -*-

import pytest
import ast


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
        t = ast.parse(self.raw_content)
        Visitor().visit(t)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(CheckIpdbError):
            return '{} in file {}'.format(excinfo.value.args[0], self.fspath)
        return super(CheckIpdbItem, self).repr_failure(excinfo)


class CheckIpdbError(Exception):
    """ indicates an error during cipdb checks. """


class Visitor(ast.NodeVisitor):

    def visit_Call(self, node):
        try:
            for item in ['ipdb', 'pdb']:
                if node.func.value.id == item:
                    line_number = node.func.value.lineno
                    col_number = node.func.value.col_offset
                    raise CheckIpdbError('Detected {} call at line {} col {}'.format(item, line_number, col_number))
        except AttributeError:
            pass
        ast.NodeVisitor.generic_visit(self, node)
