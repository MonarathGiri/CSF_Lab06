def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i + 1   # position (1-based)
    return -1

lst = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

pos = linear_search(lst, key)

if pos != -1:
    print("Element found at position", pos)
else:
    print("Element not found")