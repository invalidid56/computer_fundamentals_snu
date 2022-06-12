# invalidid56@snu.ac.kr 식물생산과학부 강준서
# myarray.py; Define Class to Control Matrix and Vector
# Don't Use by Direct call


def correct_length(here, there):
    if len(here) < len(there):
        new_here = here
        while len(there) != len(new_here):
            for h in here:
                new_here.append(h)
                if len(new_here) == len(there):
                    break
        here = new_here

    elif len(here) > len(there):
        new_there = there
        while len(here) != len(new_there):
            for t in there:
                new_there.append(t)
                if len(here) == len(new_there):
                    break
        there = new_there

    return zip(here, there)


class Vector:
    def __init__(self, *args):
        self._elements = args[0] if type(args[0]) is list else list(args)

    def get_elements(self):
        return self._elements

    def __repr__(self):
        return str("Vector("+', '.join([str(e) for e in self.get_elements()])+")")

    def __str__(self):
        return str("Vector(" + ', '.join([str(e) for e in self.get_elements()]) + ")")

    def __len__(self):
        return len(self._elements)

    def __getitem__(self, idx):
        return self._elements[idx]

    def __setitem__(self, idx, value):
        self._elements[idx] = value
        return 0

    def __mul__(self, other):   # element-wise
        if isinstance(other, Vector):
            return Vector([e * o for e, o in correct_length(self.get_elements(), other.get_elements())])

        elif isinstance(other, int) or isinstance(other, float):
            return Vector([e*other for e in self._elements])

        return 0

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector([e+o for e, o in correct_length(self.get_elements(), other.get_elements())])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector([e+other for e in self._elements])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other_minus = (-1) * other
        return self.__add__(other_minus)

    def __rsub__(self, other):
        return (-1) * self.__sub__(other)


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self._elements = [0.00 for _ in range(rows*cols)]

    def __getitem__(self, item):
        row = item[0]
        col = item[1]
        return self._elements[row + self.rows * col]

    def __setitem__(self, key, value):
        row = key[0]
        col = key[1]

        self._elements[row + self.rows * col] = float(value)
        return 0

    def __str__(self):
        result = ''
        for r in range(self.rows):
            for c in range(self.cols):
                item = self.__getitem__([r, c])
                result += '\t' + str(item)
            result += '\n' if not r == (self.rows-1) else ''
        return result

