"""
awslimitchecker/tests/test_version.py

The latest version of this package is available at:
<https://github.com/jantman/awslimitchecker>

##############################################################################
Copyright 2015 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of awslimitchecker, also known as awslimitchecker.

    awslimitchecker is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    awslimitchecker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with awslimitchecker.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
##############################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/pydnstest> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
##############################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
##############################################################################
"""

import awslimitchecker.version as version

import re


class TestVersion(object):

    def test_project_url(self):
        expected = 'https://pypi.python.org/pypi/awslimitchecker/{v}'.format(
            v=version._VERSION)
        assert version._PROJECT_URL == expected

    def test__get_project_url(self):
        assert version._get_project_url() == version._PROJECT_URL

    def test__get_version(self):
        assert version._get_version() == version._VERSION

    def test_is_semver(self):
        # see:
        # https://github.com/mojombo/semver.org/issues/59#issuecomment-57884619
        semver_ptn = re.compile(
            r'^'
            r'(?P<MAJOR>(?:'
            r'0|(?:[1-9]\d*)'
            r'))'
            r'\.'
            r'(?P<MINOR>(?:'
            r'0|(?:[1-9]\d*)'
            r'))'
            r'\.'
            r'(?P<PATCH>(?:'
            r'0|(?:[1-9]\d*)'
            r'))'
            r'(?:-(?P<prerelease>'
            r'[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*'
            r'))?'
            r'(?:\+(?P<build>'
            r'[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*'
            r'))?'
            r'$'
        )
        assert semver_ptn.match(version._VERSION) is not None
