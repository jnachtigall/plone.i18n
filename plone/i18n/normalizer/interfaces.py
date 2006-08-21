from zope.interface import Interface

class INormalizer(Interface):
    """A normalizer can normalize any unicode text string according to a
       specific ruleset implemented in the normalizer itself.
    """

    def normalize(text, locale=None):
        """The normalize method takes and input unicode text and an optional
           locale string and returns a normalized version of the text.
           If the locale is not None the ouput might differ dependent on the
           locale.
        """

class IIDNormalizer(INormalizer):
    """An ID normalizer can normalize any unicode string and returns a
       version that only contains of ASCII characters allowed in a typical
       scripting or programming language id, such as CSS class names or Python
       variable names for example.
    """

class IURLNormalizer(INormalizer):
    """An URL normalizer can normalize any unicode string and returns a
       URL-safe version that only contains of ASCII characters allowed in a URL.
    """

class IUserPreferredNormalizer(Interface):
    """An adapter for the HTTPRequest to provide user preferred language
       dependent normalization.
    """

    def normalize(text):
        """Returns a normalized Unicode string."""

class IUserPreferredURLNormalizer(IUserPreferredNormalizer):
    """An adapter for the HTTPRequest to provide user preferred language
       dependent normalization, based on an URL normalizer.
    """
