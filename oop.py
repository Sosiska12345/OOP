from __future__ import annotations
from typing import List, Union


class Matrix:
    def __init__(self, d: List[List[float]]):
        if not d or any(len(r) != len(d[0]) for r in d):
            raise ValueError("Invalid matrix")
        self.d = d

    def __repr__(self) -> str:
        return f"M{self.d}"

    def __add__(self, o: Matrix) -> Matrix:
        if len(self.d) != len(o.d) or len(self.d[0]) != len(o.d[0]):
            raise ValueError("Size mismatch")

        r = []
        for i in range(len(self.d)):
            row = []
            for j in range(len(self.d[0])):
                row.append(self.d[i][j] + o.d[i][j])
            r.append(row)
        return Matrix(r)

    def __mul__(self, o: Union[Matrix, float, int]) -> Matrix:
        if isinstance(o, (int, float)):
            r = []
            for i in range(len(self.d)):
                row = []
                for j in range(len(self.d[0])):
                    row.append(self.d[i][j] * o)
                r.append(row)
            return Matrix(r)

        if not isinstance(o, Matrix):
            raise TypeError("Invalid type")

        if len(self.d[0]) != len(o.d):
            raise ValueError("Cannot multiply")

        r = []
        for i in range(len(self.d)):
            row = []
            for j in range(len(o.d[0])):
                s = 0
                for k in range(len(self.d[0])):
                    s += self.d[i][k] * o.d[k][j]
                row.append(s)
            r.append(row)
        return Matrix(r)

    def transpose(self) -> Matrix:
        r = []
        for i in range(len(self.d[0])):
            row = []
            for j in range(len(self.d)):
                row.append(self.d[j][i])
            r.append(row)
        return Matrix(r)


# Пример
if __name__ == "__main__":
    m1 = Matrix([[1, 2], [2, 3]])
    m2 = Matrix([[2, 5], [7, 9]])

    print(f"m1 + m2 = {m1 + m2}")
    print(f"m1 * m2 = {m1 * m2}")
    print(f"m1 * 3 = {m1 * 3}")
    print(f"m1.T = {m1.transpose()}")