from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Suit(Enum):
    SPADE = "spade"
    HEART = "heart"
    CLUB = "club"
    DIAMOND = "diamond"

class ConfigKey(Enum):
    FROM = "From"           # Mailbox of message author
    SENDER = "Sender"       # Mailbox of message sender
    REPLY_TO = "Reply-To"         # Mailbox for replies to message
    TO = "To"               # Primary recipient mailbox
    CC = "Cc"               # Carbon-copy recipient mailbox
    BCC = "Bcc"             # Blind-carbon-copy recipient

    def __init__(self, code):
        Enum.__init__(self)

        # cached canonical code
        self._code = self._canonicalize_code(code)

    @property
    def code(self):
        return self._code

    @classmethod
    def get_by_code(cls, code):
        """
        :param code: canonical code
        :return: enum object if code matches. Otherwise, None.
        """
        canonical_code = cls._canonicalize_code(code)

        for entry in cls:
            if entry.code == canonical_code:
                return entry

        return None

    @classmethod
    def _canonicalize_code(self, code):
        if not code:
            return None

        canonical_code = code.strip().lower().replace("-", "_")

        return canonical_code

def test_str():
    assert "Color.RED" == str(Color.RED)
    assert "<Color.RED: 1>" == repr(Color.RED)

    assert "Suit.SPADE" == str(Suit.SPADE)
    assert "<Suit.SPADE: 'spade'>" == repr(Suit.SPADE)

def test_type():
    assert Color == type(Color.RED)
    assert isinstance(Color.RED, Color)


def test_attributes():
    assert "RED", Color.RED.name
    assert 1, Color.RED.value

    assert Color.RED == Color(1)
    assert Color.RED == Color['RED']

    assert "SPADE", Suit.SPADE.name
    assert "spade", Suit.SPADE.value

def test_iteration():
    for color in Color:
        assert isinstance(color, Color)
        assert color in Color

def test_converting_to_dict():
    # converting to a {Color, 'a']
    value_by_color = dict( (i, i.value) for i in Color )
    #print("colors=", value_by_color)

    expected = {Color.RED: 1, Color.GREEN: 2, Color.BLUE: 3}
    assert expected == value_by_color

def test_class_method():
    assert "from" == ConfigKey.FROM.code
    assert "reply_to" == ConfigKey.REPLY_TO.code

    assert ConfigKey.FROM == ConfigKey.get_by_code("from")
    assert ConfigKey.REPLY_TO == ConfigKey.get_by_code("reply_to")

