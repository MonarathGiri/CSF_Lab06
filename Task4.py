def selection_sort_trace(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        print(f"Pass {i+1}: {lst}")

lst = [64, 25, 12, 22, 11]
selection_sort_trace(lst)