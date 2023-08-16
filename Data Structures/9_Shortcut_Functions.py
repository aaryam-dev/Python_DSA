import bisect

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

index = bisect.bisect_left(sorted_list, target)
if index < len(sorted_list) and sorted_list[index] == target:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found")


#######################

unsorted_list = [5, 2, 9, 1, 5, 6, 3]
sorted_list = sorted(unsorted_list)
print("Sorted list:", sorted_list)


#######################


unsorted_list = [5, 2, 9, 1, 5, 6, 3]
unsorted_list.sort()
print("Sorted list (in-place):", unsorted_list)
