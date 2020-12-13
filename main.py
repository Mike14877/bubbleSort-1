# Bubble_Sort_Method

list_1 = [500, 1, 54, 63, 85]


def bubble_sort(list1):
    keep_continue = True
    while keep_continue:
        keep_continue = False
        for i in range(len(list1) - 1):
            if list_1[i] > list_1[i+1]:
                list_1[i], list_1[i+1] = list_1[i+1], list_1[i]
                keep_continue = False
        return list_1


print(bubble_sort(list_1))
