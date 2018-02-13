def reverse_s(s):
    return do_reverse_s(s, 0, len(s)-1)


def do_reverse_s(s, start, end):
    if start == end:
        return s[start]
    else:
        return s[end] + do_reverse_s(s, start, end-1)


def main():
    s = 'fuckyou'
    print(reverse_s(s))


if __name__ == '__main__':
    main()
