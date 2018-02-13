def count_vowel_consonant(s):
    rs = s.replace(' ', '')
    return do_count(rs, 0, len(rs)-1)


def do_count(s, start, end):
    num_vowel = num_consonant = 0
    if is_vowel(s[start]):
        num_vowel = 1
    else:
        num_consonant = 1
    if start < end:
        sub_vowel, sub_consonant = do_count(s, start+1, end)
        num_vowel += sub_vowel
        num_consonant += sub_consonant
    return (num_vowel, num_consonant)


def is_vowel(c):
    return (c in ['a', 'e', 'i', 'o', 'u'])


def main():
    s = 'i just want to fuck you'
    print(count_vowel_consonant(s))


if __name__ == '__main__':
    main()
