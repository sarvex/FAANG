# function to perform linear search for element in array
def search(arr, element):
    return next(
        (index for index in range(0, len(arr)) if arr[index] == element), -1
    )


arr = [20, 5, 7, 25]
element = 5

print("Array Searched:", arr)
print("Searching for:", element)
print("Searched index=", search(arr, element))
