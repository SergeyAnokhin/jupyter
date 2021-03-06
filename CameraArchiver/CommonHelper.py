from math import log2


class CommonHelper:
    def size_human(self, size):
        _suffixes = ['bytes', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb']
        # determine binary order in steps of size 10 
        # (coerce to int, // still returns a float)
        order = int(log2(size) / 10) if size else 0
        # format file size
        # (.4g results in rounded numbers for exact matches and max 3 decimals, 
        # should never resort to exponent values)
        return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])

