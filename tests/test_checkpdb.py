# -*- coding: utf-8 -*-
from _pytest.config import ExitCode


class TestWithPdb(object):

    def test_with_no_pdb(self, testdir):
        testdir.makepyfile("""
            def test_ok_ipdb_gen():
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')

    def test_with_pdb(self, testdir):
        testdir.makepyfile("""
            # monkeypatching pdb
            def foo():
                return True
            import pdb; pdb.set_trace = foo

            def test_with_pdb_gen():
                import pdb; pdb.set_trace()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == ExitCode.TESTS_FAILED
        result.stdout.fnmatch_lines('* FAILED*')

    def test_with_pdb_commented_single_line(self, testdir):
        testdir.makepyfile("""
            def test_with_pdb_commented_single_line_gen():
                # import pdb; pdb.set_trace()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')

    def test_with_pdb_commented_docstring(self, testdir):
        testdir.makepyfile("""
            def test_with_pdb_commented_docstring_gen():
                \"\"\"
                import pdb; pdb.set_trace()
                \"\"\"
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')
