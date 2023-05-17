def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    special_cases = ["CM", "CD", "XC", "XL", "IX", "IV"]
    convert_cases = ["CDD", "CCCC", "XLL", "XXXX", "IVV", "IIII"]
    single_cases = ["I", "V", "X", "L", "C", "D", "M"]
    single_equal_cases = [1, 5, 10, 50, 100, 500, 1000]

    total = 0
    for i in range(len(special_cases)):
        if (s.find(special_cases[i]) != -1):
            s = s.replace(special_cases[i], convert_cases[i])
    print(s)
    for i in range(len(single_cases)):
        num = s.count(single_cases[i])
        if num != -1:
            total = total + single_equal_cases[i]*num
            s = s.replace(single_cases[i], "")
    return total
