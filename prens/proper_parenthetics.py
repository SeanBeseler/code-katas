from linked_list import LinkedList


def check_prens(prens):
    """check the prens"""
    LList = LinkedList()
    count = 0
    left = 0
    right = 0
    for x in prens:
        LList.push(x)
        count += 1
    for y in range(count):
        pr = LList.pop().val
        if pr == '(':
            left += 1
        elif pr == ')':
            if right == left or right < left:
                right += 1
            else:
                return -1
    if right == left:
        return 0
    return 1
