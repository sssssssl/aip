def even_before_odd(L):
    last_even_index = do_rearrange(L, 0, len(L)-1)
    return L


def do_rearrange(L, start, end):
    """
    return index of the last even number.
    """
    if start == end:
        if L[start] % 2 != 0:
            return start - 1
        else:
            return start
    else:
        last_even_index = do_rearrange(L, start, end-1)
        first_odd_index = last_even_index + 1
        if L[end] % 2 == 0 and first_odd_index < end:
            L[first_odd_index], L[end] = L[end], L[first_odd_index]
            last_even_index = first_odd_index
        return last_even_index


def main():
    L = [43, 45, 55, 66, 57, 99, 100]
    print(even_before_odd(L))


if __name__ == '__main__':
    main()
