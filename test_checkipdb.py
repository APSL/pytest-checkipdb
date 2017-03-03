# -*- coding: utf-8 -*-

import pytest
pytest_plugins = "pytester"


class TestBasic(object):

    @pytest.fixture
    def monkey_patch_ipdb(self):
        # monkeypatching ipdb
        def foo():
            return True
        import ipdb
        ipdb.set_trace = foo

    def test_with_no_ipdb(self, testdir):
        testdir.makepyfile("""
            def test_ok():
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')

    def test_with_ipdb(self, testdir, monkey_patch_ipdb):
        testdir.makepyfile("""
            def test_ko():
                import ipdb; ipdb.set_trace()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 1
        result.stdout.fnmatch_lines('* FAILED*')

    def test_with_ipdb_commented_single_line(self, testdir, monkey_patch_ipdb):
        testdir.makepyfile("""
            def test_ko():
                # import ipdb; ipdb.set_trace()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')

    def test_with_ipdb_commented_docstring(self, testdir, monkey_patch_ipdb):
        testdir.makepyfile("""
            def test_ko():
                \"\"\"
                import ipdb; ipdb.set_trace()
                \"\"\"
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')
