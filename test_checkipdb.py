# -*- coding: utf-8 -*-

import pytest

pytest_plugins = "pytester"


# @pytest.fixture
# def example_ok(request):
#     """Create a test file."""
#     testdir = request.getfuncargvalue("testdir")
#     p = testdir.makepyfile("")
#     p.write("class AClass:\n\tpass\n\t\t\n\n# too many spaces")
#     return p
#
#
# @pytest.fixture
# def example_ko(request):
#     """Create a test file."""
#     testdir = request.getfuncargvalue("testdir")
#     p = testdir.makepyfile("")
#     p.write("import ipdb; ipdb.set_trace()\nclass AClass:\n\tpass\n\t\t\n\n# too many spaces")
#     return p
#
#
# def test_ok(testdir, example_ok, request):
#     testdir.tmpdir.ensure("test_ok.py")
#     result = testdir.runpytest("--cipdb --verbose", )
#     result.stdout.fnmatch_lines([
#         '*no tests*',
#     ])
#     assert result.ret != 0
#
#
# def test_ko(testdir, example_ko):
#     testdir.tmpdir.ensure("test_ko.py")
#     result = testdir.runpytest("--cipdb --verbose", )
#     result.stdout.fnmatch_lines([
#         '*no tests*',
#     ])
#     assert result.ret != 0


def test_myplugin(testdir):
    testdir.makepyfile("""
        def test_example():
            pass
    """)
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines('*PASSED*')


def test_ok(testdir):
    testdir.makepyfile("""
        def test_ok():
            import ipdb; ipdb.set_trace()
            pass
    """)
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines('*PASSED*')


