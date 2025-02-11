n = int(input())
arr = list(map(int, input().split()))

def selection_sort():
    for i in range(n-1):
        min_idx = i
        for k in range(i+1,n):
            if arr[min_idx] > arr[k]:
                min_idx = k 
        arr[i],arr[min_idx] = arr[min_idx],arr[i]

selection_sort()
for elem in arr:
    print(elem,end=" ")