def BinarySearch(SearchList, target):
    left = 0
    right = len(SearchList) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if SearchList[mid] < target:
            left = mid + 1
            continue
        if SearchList[mid] == target:
            return mid
        if SearchList[mid] > target:
            right = mid - 1
            return None


temp_list = [1, 3, 4, 6, 8, 9]

print(BinarySearch(temp_list, 5))
print(BinarySearch(temp_list, 1))
print(BinarySearch(temp_list, 3))
print(BinarySearch(temp_list, 4))
print(BinarySearch(temp_list, 6))
print(BinarySearch(temp_list, 8))
print(BinarySearch(temp_list, 9))
