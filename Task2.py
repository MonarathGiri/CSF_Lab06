import math

def indexed_search(lst, key):
    n = len(lst)
    step = int(math.sqrt(n))
    
    prev = 0
    while prev < n and lst[min(step, n)-1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    for i in range(prev, min(step, n)):
        if lst[i] == key:
            return i
    
    return -1

lst = [5, 10, 15, 20, 25, 30]
key = int(input("Enter element: "))

if indexed_search(lst, key) != -1:
    print("Element found")
else:
    print("Element not found")
