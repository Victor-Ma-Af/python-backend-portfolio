
def target_number(num_list, target):
    num_list.sort()
    print(num_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = 0
    end = len(num_list)- 1

    while start <= end:
        mid = (start + end) // 2
        if target == num_list[mid]:
            return f'the position of target is: {mid}'
        elif target < num_list[mid]:
            end = mid -1
        else:
            start = mid + 1
    return -1

random_list = [69, 74, 45, 16, 48, 8, 18, 30, 49, 25]

print(target_number(random_list, 74))