import time


def binary_search(lst, item):

    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        ans = lst[mid]
        if ans == item:
            return f"index: {mid}"
        elif ans > item:
            high = mid - 1
        elif ans < item:
            low = mid + 1

    return None


def bin_search_letters(lst, name):
    letter = name[0]
    print(letter)
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        ans = lst[mid]
        if ans[0] == letter:
            return f"index: {mid}, znachenie: {ans}"
        if ans[0] > letter:
            high = mid - 1
        else:
            low = mid + 1

    return None

