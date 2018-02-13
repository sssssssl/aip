def is_palindrome(s):
    return do_test_palindrome(s, 0, len(s)-1)


def do_test_palindrome(s, start, end):
    if start == end:    # base case:1 character only
        return True
    elif s[start] != s[end]:
        return False
    else:
        if start + 1 == end:    # base case: 2 characters
            return True
        elif do_test_palindrome(s, start+1, end-1):
            return True
        return False


def main():
    s1 = 'fuckyou'
    print('{}:{}'.format(s1, is_palindrome(s1)))
    s2 = 'racecar'
    print('{}:{}'.format(s2, is_palindrome(s2)))


if __name__ == '__main__':
    main()
