import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str
else:
    string_types = basestring  # NOQA


def remove_tone(s):
    '''Removes all tones from string `s`'''
    assert isinstance(s, string_types)
    pass


def to_ascii(s):
    '''Replace all Vietnamese special characters with ASCII version.

    This is the ASCII version which causes ambiguous when phones don't support
    Vietnamese.
    '''
    assert isinstance(s, string_types)
    pass


def get_tone(word):
    '''Get tone from given word'''
    assert isinstance(word, string_types)
    pass
