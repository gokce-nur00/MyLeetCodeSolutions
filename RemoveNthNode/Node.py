class Solution(object):
    def length(lst):
        r = 0
        while lst:
            lst = lst.next
            r += 1
        return r

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = length(head)
        i = 0
        print(head)
        print(l)
        for j in range(l):
            if i < n:
                i = i+1
            if i == n:
                head[j-1] = head[j]

        return head
