def fast_power(x, n):
    if n == 0:
        return 1
    else:
        partial = fast_power(x, n//2)
        result = partial * partial
        if n % 2 != 0:
            result *= x
        return result


def fast_power_iter(x, n):
    if n == 0:
        return 1
    else:
        rem = []
        while n:
            rem.append(n % 2)
            n //= 2
        t = len(rem) - 1
        res = 1
        while t >= 0:
            res = res * res
            if rem[t]:
                res *= x
            t -= 1
        return res


def main():
    print(fast_power(2, 25))
    print(fast_power_iter(2, 25))
    print(fast_power(7, 36))
    print(fast_power_iter(7, 36))


if __name__ == '__main__':
    main()
