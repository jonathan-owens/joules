"""
A URI is a uniform resource identifier. See [Wikipedia](
https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) for more information.

In this implementation of a URI parser, we assume the general form of a URI
to be:

```
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
```

Currently supported schema are:

* file
"""


class URIParseError(Exception):
    """
    URIParseError are exceptions related to the parsing of URIs.
    """
    pass


def parse_uri(string):
    """
    Parses `string` to extract URI information from it. Returns the scheme
    and the location of the resource.

    :param string: Properly formatted URI string
    :type string: str

    :return: The scheme and resource location
    :rtype: str, str

    :raises URIParseError: If we cannot parse the input string as a proper URI.
    """
    # Note that this function is currently pretty silly looking, but it will
    # grow as the package expands to provide more functionality.

    # The scheme and location are separated by the FIRST colon
    try:
        scheme, location = string.split(':', 1)
    except ValueError:
        # If no colon was found in the passed URI.
        raise URIParseError('Unable to find scheme and location in URI %s. '
                            'No : character present.' % string)

    return scheme, location
