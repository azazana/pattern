def is_singleton(cls):
    """Return True if `cls` is a singleton class."""
    return cls.__new__ is cls.__init__

