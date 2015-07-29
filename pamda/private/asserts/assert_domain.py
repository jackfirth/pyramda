

class DomainAssertionError(AssertionError):
    def __init__(self, in_domain, f, domain_args):
        name = f.__name__
        domain_args_str = ", ".join(map(str, domain_args))
        template = "Expected the argument{0} {1} {2} in the domain of {3}"
        plural_suffix = "" if len(domain_args) == 1 else "s"
        in_domain_str = "to be" if in_domain else "not to be"
        message = template.format(
            plural_suffix,
            domain_args_str,
            in_domain_str,
            name
        )
        super(DomainAssertionError, self).__init__(message)


class InDomainAssertionError(DomainAssertionError):
    def __init__(self, f, domain_args):
        super(InDomainAssertionError, self).__init__(True, f, domain_args)


class NotInDomainAssertionError(DomainAssertionError):
    def __init__(self, f, domain_args):
        super(NotInDomainAssertionError, self).__init__(False, f, domain_args)


def assert_in_domain(f, *args, **kwargs):
    try:
        f(*args, **kwargs)
    except ValueError:
        raise InDomainAssertionError(f, args)


def assert_not_in_domain(f, *args, **kwargs):
    try:
        f(*args, **kwargs)
        raise NotInDomainAssertionError(f, args)
    except ValueError:
        return
