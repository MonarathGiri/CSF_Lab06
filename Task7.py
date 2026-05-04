stack = []

# Push
stack.append(30)
stack.append(10)
stack.append(50)
stack.append(20)

print("Stack:", stack)

# Selection sort
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

sorted_stack = selection_sort(stack.copy())
print("Sorted Stack:", sorted_stack)