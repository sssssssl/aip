def min_max(L):
    return do_min_max(L, 0, len(L))


def do_min_max(L, start, end):
    if start + 1 >= end:
        return (L[start], L[start])
    else:
        v1, v2 = L[start], L[start+1]
        if v1 > v2:
            max_v, min_v = v1, v2
        else:
            max_v, min_v = v2, v1
        if start + 2 < end:
            max_sub, min_sub = do_min_max(L, start+2, end)
            if max_sub > max_v:
                max_v = max_sub
            if min_sub < min_v:
                min_v = min_sub
        return (max_v, min_v)


def main():
    L = [1, 2, 55, 4, -5, 6, -9]
    print(min_max(L))


if __name__ == '__main__':
    main()
