queue = []

# Insert
queue.append(5)
queue.append(15)
queue.append(25)
queue.append(35)

print("Queue:", queue)

# Linear search
def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

key = int(input("Enter element to search: "))

if linear_search(queue, key) != -1:
    print("Element found")
else:
    print("Element not found")