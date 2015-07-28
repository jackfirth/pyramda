from functools import wraps, partial
from .curry_spec import \
    CurrySpec, \
    ArgValues, \
    make_func_curry_spec, \
    remove_args_from_curry_spec
from .curry_spec_fulfill import arg_values_fulfill_curry_spec


def curry_by_spec(curry_spec, f):
    @wraps(f)
    def curried(*args, **kwargs):
        arg_values = ArgValues(args, kwargs)
        if arg_values_fulfill_curry_spec(curry_spec, arg_values):
            return f(*args, **kwargs)
        else:
            partialed_f = wraps(f)(partial(f, *args, **kwargs))
            new_spec = remove_args_from_curry_spec(curry_spec, arg_values)
            return curry_by_spec(new_spec, partialed_f)
    return curried


def curry(f):
    curry_spec = make_func_curry_spec(f)
    return curry_by_spec(curry_spec, f)
