# Given a list of numbers and a number k, return whether any two numbers from the list
# add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def day1(lst,k):
    previous = dict()
    for i in lst:
        if str(k-i) in previous:
            return True
        previous[str(i)] = k
    return False


print(day1([10, 15, 3, 7], 17))