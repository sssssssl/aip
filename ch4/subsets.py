from copy import deepcopy


def subsets(S):
    if len(S) == 0:
        return [[], ]
    else:
        v = S.pop(0)
        subsets_without_v = subsets(S)
        subsets_with_v = deepcopy(subsets_without_v)
        for s in subsets_with_v:
            s.append(v)
        subsets_all = subsets_with_v + subsets_without_v
        return subsets_all


def main():
    S = [1, 2, 3]
    print(subsets(S))


if __name__ == '__main__':
    main()
