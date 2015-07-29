from .curry import curry


attr = curry(lambda name, o: getattr(o, name))
