from typing import List, Union

MatrixData = List[List[float]]


def add(a:MatrixData, b:MatrixData)->MatrixData:
    r=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        r.append(row)
    return r



def mul(a: MatrixData, b: MatrixData) -> MatrixData:
    r = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(a[0])):
                s += a[i][k] * b[k][j]
            row.append(s)
        r.append(row)
    return r


def mul_scalar(a: MatrixData, s: Union[float, int]) -> MatrixData:
    r = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] * s)
        r.append(row)
    return r


def transpose(a: MatrixData) -> MatrixData:
    r = []
    for i in range(len(a[0])):
        row = []
        for j in range(len(a)):
            row.append(a[j][i])
        r.append(row)
    return r


# Пример
if __name__ == "__main__":
    m1 = [[1, 2], [3, 4]]
    m2 = [[2, 5], [7, 9]]

    print(f"add(m1, m2) = {add(m1, m2)}")
    print(f"mul(m1, m2) = {mul(m1, m2)}")
    print(f"mul_scalar(m1, 3) = {mul_scalar(m1, 3)}")
    print(f"transpose(m1) = {transpose(m1)}")