# -*- coding: utf-8 -*-
from _pytest.config import ExitCode


class TestWithBreakpoint(object):

    def test_with_no_breakpoint(self, testdir):
        testdir.makepyfile("""
            def test_ok_breakpoint_gen():
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == ExitCode.OK
        result.stdout.fnmatch_lines('* PASSED*')

    def test_with_breakpoint(self, testdir):
        testdir.makepyfile("""
            # monkeypatching breakpoint
            def foo():
                return True
            breakpoint = foo

            def test_with_breakpoint_gen():
                breakpoint()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == ExitCode.TESTS_FAILED
        result.stdout.fnmatch_lines('* FAILED*')

    def test_with_breakpoint_commented_single_line(self, testdir):
        testdir.makepyfile("""
            def test_with_breakpoint_commented_single_line_gen():
                # breakpoint()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == ExitCode.OK
        result.stdout.fnmatch_lines('* PASSED*')

    def test_with_breakpoint_commented_docstring(self, testdir):
        testdir.makepyfile("""
            def test_with_breakpoint_commented_docstring_gen():
                \"\"\"
                breakpoint()
                \"\"\"
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == ExitCode.OK
        result.stdout.fnmatch_lines('* PASSED*')
