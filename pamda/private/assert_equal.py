

class EqualityAssertionError(AssertionError):
    def __init__(self, equal, actual, expected):
        template = "Expected {0} {1} {2}"
        equal_str = "to equal" if equal else "not to equal"
        message = template.format(
            str(actual),
            equal_str,
            str(expected)
        )
        super(EqualityAssertionError, self).__init__(message)


class EqualAssertionError(EqualityAssertionError):
    def __init__(self, actual, expected):
        super(EqualAssertionError, self).__init__(True, actual, expected)


class NotEqualAssertionError(EqualityAssertionError):
    def __init__(self, actual, expected):
        super(NotEqualAssertionError, self).__init__(False, actual, expected)


def assert_equal(actual, expected):
    if actual != expected:
        raise EqualAssertionError(actual, expected)


def assert_not_equal(actual, expected):
    if actual == expected:
        raise NotEqualAssertionError(actual, expected)
