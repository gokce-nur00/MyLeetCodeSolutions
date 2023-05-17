import itertools


def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    number_lists = [["a", "b", "c"],
                    ["d", "e", "f"],
                    ["g", "h", "i"],
                    ["j", "k", "l"],
                    ["m", "n", "o"],
                    ["p", "q", "r", "s"],
                    ["t", "u", "v"],
                    ["w", "x", "y", "z"],
                    ]
    return_lists = []
    if len(digits) == 0:
        return []
    else:
        for i in range(len(digits)):
            index = int(digits[i])-2
            return_lists.append(number_lists[index])
    if len(return_lists) == 1:
        return return_lists[0]
    else:
        combinations = []
        solution = []
        combinations = list(itertools.product(*return_lists))
        for element in combinations:
            s = ""
            for i in element:
                s = s + i
            solution.append(s)
        print(solution)
        return solution
