# -*- coding: utf-8 -*-

pytest_plugins = "pytester",


class TestBasic(object):

    def test_ok(self, testdir):
        testdir.makepyfile("""
            def test_ok():
                pass
        """)
        result = testdir.runpytest()
        result.stdout.fnmatch_lines('test_ok.py .')

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
        result = testdir.runpytest()
        result.stdout.fnmatch_lines('test_ko.py .')


