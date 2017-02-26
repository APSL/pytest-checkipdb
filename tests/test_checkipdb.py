# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def example(request):
    """Create a test file."""
    testdir = request.getfuncargvalue("testdir")
    p = testdir.makepyfile("")
    p.write("class AClass:\n    pass\n       \n\n# too many spaces")
    return p


@pytest.fixture
def example_ko(request):
    """Create a test file."""
    testdir = request.getfuncargvalue("testdir")
    p = testdir.makepyfile("")
    p.write("import ipdb; ipdb.set_trace()\nclass AClass:\n    pass\n       \n\n# too many spaces")
    return p


def test_ok(testdir, example, request):
    result = testdir.runpytest("--cipdb")
    # result.stdout.fnmatch_lines([
    #     '*PASSED*',
    # ])
    assert result.ret != 0


def test_ko(testdir, example_ko):
    result = testdir.runpytest("--cipdb")
    # result.stdout.fnmatch_lines([
    #     '*::test_sth PASSED',
    # ])
    assert result.ret != 0
