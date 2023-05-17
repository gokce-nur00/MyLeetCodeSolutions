def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    myList = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    myList.append([nums[i], nums[j], nums[k]])
    if (len(myList) > 0):
        print(myList)
        for i in range(len(myList)-1):
            for j in range(i+1, len(myList)):
                try:
                    temp = myList[i]
                    temp2 = myList[j]
                    temp.sort()
                    temp2.sort()
                    if temp == temp2:
                        myList.remove(myList[j])
                except:
                    print("done!")
    return myList
