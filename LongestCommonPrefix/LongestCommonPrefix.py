def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    common = strs[0]

    for word in strs:
        while not word.startswith(common):
            common = common[:-1]

    return common
