def insert_sort(origin_list):
    sorted_list = []
    for i in range(0, len(origin_list)):
        if len(sorted_list) == 0:
            sorted_list.append(origin_list[i])
            continue
        for j in range(len(sorted_list) - 1, -1, -1):
            if sorted_list[j] <= origin_list[i]:
                sorted_list.insert(j + 1, origin_list[i])
                break
            if j == 0:
                sorted_list.insert(0, origin_list[i])
    origin_list[:] = sorted_list[:]


origin_list = [5, 3, 1, 7, 9, 8]
insert_sort(origin_list)
print(origin_list)


def bubble_sort(origin_list):
    for i in range(len(origin_list), 0, -1):
        for j in range(0, i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[
                    j + 1], origin_list[j]


origin_list = [5, 3, 1, 7, 9, 8]
bubble_sort(origin_list)
print(origin_list)


def quick_sort(origin_list, start, end):
    if start >= end:
        return
    left = start
    right = end
    flag_index = left
    while left < right:
        while right > left:
            if origin_list[right] < origin_list[flag_index]:
                origin_list[right], origin_list[flag_index] = origin_list[
                    flag_index], origin_list[right]
                flag_index = right
                break
            right -= 1
        while left < right:
            if origin_list[left] > origin_list[flag_index]:
                origin_list[left], origin_list[flag_index] = origin_list[
                    flag_index], origin_list[left]
                flag_index = left
                break
            left += 1
    quick_sort(origin_list, start, flag_index)
    quick_sort(origin_list, flag_index + 1, end)


origin_list = [5, 3, 1, 3, 7, 9, 8]
quick_sort(origin_list, 0, len(origin_list) - 1)
print(origin_list)


def merge_sort(origin_list, start, end):
    if end <= start:
        return
    mid = int((start + end) / 2)
    merge_sort(origin_list, start, mid)
    merge_sort(origin_list, mid + 1, end)
    left_head = int(start)
    right_head = int(mid + 1)
    temp_list = []
    while left_head <= mid and right_head <= end:
        if origin_list[left_head] < origin_list[right_head]:
            temp_list.append(origin_list[left_head])
            left_head += 1
        if origin_list[left_head] >= origin_list[right_head]:
            temp_list.append(origin_list[right_head])
            right_head += 1
    if left_head <= mid:
        temp_list += origin_list[left_head:mid + 1]
    if right_head <= end:
        temp_list += origin_list[right_head:end + 1]
    for i in range(0, len(temp_list)):
        origin_list[i + start] = temp_list[i]


origin_list = [5, 3, 1, 3, 7, 9, 8]
merge_sort(origin_list, 0, len(origin_list) - 1)
print(origin_list)
