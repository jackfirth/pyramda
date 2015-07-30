

class PredicateCaseAssertionError(AssertionError):
    def __init__(self, expected, pred, v):
        name = pred.__name__
        v_str = str(v)
        template = "Expected predicate {0} to be {1} for input {2}"
        message = template.format(name, expected, v_str)
        super(PredicateCaseAssertionError, self).__init__(message)


class PredicateFalseCaseAssertionError(PredicateCaseAssertionError):
    def __init__(self, pred, v):
        super(PredicateFalseCaseAssertionError, self).__init__(False, pred, v)


class PredicateTrueCaseAssertionError(PredicateCaseAssertionError):
    def __init__(self, pred, v):
        super(PredicateTrueCaseAssertionError, self).__init__(True, pred, v)


def assert_pred_cases(pred, *cases):
    for v, expected in cases:
        pv = pred(v)
        if pv and not expected:
            raise PredicateFalseCaseAssertionError(pred, v)
        if not pv and expected:
            raise PredicateTrueCaseAssertionError(pred, v)


def true_case(v):
    return (v, True)


def false_case(v):
    return (v, False)
