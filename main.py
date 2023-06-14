def Max_1(x, y, z):
    m = x
    if y > m:
        m = y
    if z > m:
        m = z
    return m


def Max_2(x, y, z, f, g):
    m = Max_1(x, y, z)
    n = Max_1(m, f, g)
    return n


def Min_1(x, y, z):
    n = x
    if y < n:
        n = y
    if z < n:
        n = z
    return n


def Min_2(x, y, z, f, g):
    m = Min_1(x, y, z)
    n = Min_1(m, f, g)
    return n


def multi(a, b, c, d, e):
    s = Max_2(a, b, c, d, e)
    t = Min_2(a, b, c, d, e)
    u = s * t
    return u


def divide(a, b, c, d, e):
    s = Max_2(a, b, c, d, e)
    t = Min_2(a, b, c, d, e)
    u = s / t
    return u


def main():
    print("任意の数字を5つ入力してください。")
    x = int(input("1つ目の数字："))
    y = int(input("2つ目の数字："))
    z = int(input("3つ目の数字："))
    f = int(input("4つ目の数字："))
    g = int(input("5つ目の数字："))

    print("最大値と最小値の積は ", multi(x, y, z, f, g), " です。")
    print("最大値と最小値の商は ", divide(x, y, z, f, g), " です。")


main()
