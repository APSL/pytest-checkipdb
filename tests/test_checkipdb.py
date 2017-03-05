# -*- coding: utf-8 -*-


class TestWithIpdb(object):

    def test_with_no_ipdb(self, testdir):
        testdir.makepyfile("""
            def test_ok_ipdb_gen():
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')

    def test_with_ipdb(self, testdir):
        testdir.makepyfile("""
            # monkeypatching ipdb
            def foo():
                return True
            import ipdb; ipdb.set_trace = foo

            def test_ko_ipdb_gen():
                ipdb.set_trace()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 1
        result.stdout.fnmatch_lines('* FAILED*')

    def test_with_ipdb_commented_single_line(self, testdir):
        testdir.makepyfile("""
            def test_with_ipdb_commented_gen():
                # import ipdb; ipdb.set_trace()
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')

    def test_with_ipdb_commented_docstring(self, testdir):
        testdir.makepyfile("""
            def test_with_ipdb_commented_docstring_gen():
                \"\"\"
                import ipdb; ipdb.set_trace()
                \"\"\"
                pass
        """)
        result = testdir.runpytest("--cipdb", "-v")
        assert result.ret == 0
        result.stdout.fnmatch_lines('* PASSED*')
