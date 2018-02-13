def k_largest_bubble(L, k):
    n = len(L)
    for i in range(k):
        for j in range(i+1, n):
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
    return L[:k]


def k_largest(L, k):
    n = len(L)
    for i in range(k):
        max_index = find_max(L, i, n)
        L[max_index], L[i] = L[i], L[max_index]
    return L[:k]


def find_max(L, start, end):
    max_v = L[start]
    max_index = start
    for i in range(start+1, end):
        if L[i] > max_v:
            max_v = L[i]
            max_index = i
    return max_index


def main():
    L = [1, 2, 3, 4, 99, 6, 7]
    res = k_largest(L[:], 5)
    print(res)
    res2 = k_largest_bubble(L[:], 5)
    print(res2)


if __name__ == '__main__':
    main()
