# def search(arr, target):
#     for n in arr:
#         if n == target:
#             return True
#     return False


def search(arr, target):
    if len(arr) == 0:
        return False
    if arr[-1] == target:
        return True
    return search(arr[:-1], target)




print(search([15, 27, 65, 98, 14, 16, 2, 7, 47], 1))
