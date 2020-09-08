#Write a function called that takes a list and returns a new list with only the unique elements from the original
def findUnique(list1):
    list2 = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])
    return list2

print(findUnique([1,2,3,1,4,1,5,4,6,4]))