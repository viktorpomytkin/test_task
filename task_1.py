import sys


def circular_path(n, m):
    arr = list(range(1, n + 1))
    path = []
    idx = 0
    first = True
    while first or arr[idx] != 1:
        first = False
        path.append(arr[idx])
        idx = (idx + m - 1) % n
    return ''.join(map(str, path))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Использование: python task_1.py n1 m1 n2 m2")
        sys.exit(1)

    n1, m1, n2, m2 = map(int, sys.argv[1:])
    result = circular_path(n1, m1) + circular_path(n2, m2)
    print(result)
