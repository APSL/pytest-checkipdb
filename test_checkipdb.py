# -*- coding: utf-8 -*-

pytest_plugins = "pytester"


class TestBasic(object):

    def test_ok(self, testdir):
        testdir.makepyfile("""
            def test_ok():
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')

    def test_ko(self, testdir):
        testdir.makepyfile("""
            # monkeypatching ipdb
            def foo():
                return True

            def test_ko():
                import ipdb;
                ipdb.set_trace = foo
                ipdb.set_trace()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 1
        result.stdout.fnmatch_lines('* FAILED*')


