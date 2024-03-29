def mergeTwoLists(self, l1, l2):
    # operator precedence in python : ()
    if (not l1) or (l2 and (l1.val > l2.val)):
        # swap
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1