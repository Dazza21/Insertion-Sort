#InsertionSort

def insertion_sort(list):

    for i in range(1, len(list)):
        item_insert = nums[i]

        j = i - 1

        while j >= 0 and nums[j] > item_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_insert


randomlist = [2,5,6,8,1,0]
insertion_sort(randomlist)
print(randomlist)


