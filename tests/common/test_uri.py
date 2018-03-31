import unittest

from joules.common.uri import parse_uri
from joules.common.uri import URIParseError


valid_scheme = 'file'
valid_location = '/home/users/test.txt'
valid_uri = f'{valid_scheme}:{valid_location}'
invalid_uri = f'{valid_scheme}{valid_location}'


class TestURI(unittest.TestCase):
    def test_parse_valid_uri(self):
        scheme, location = parse_uri(valid_uri)
        self.assertEqual(scheme, 'file')
        self.assertEqual(location, '/home/users/test.txt')

    def test_parse_invalid_uri(self):
        self.assertRaises(URIParseError, parse_uri, invalid_uri)


if __name__ == '__main__':
    unittest.main()
