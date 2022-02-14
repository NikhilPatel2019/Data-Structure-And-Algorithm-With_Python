#Time Complexity(Best Case) = O(n log n)
#Time Complexity(Worst Case) = O(n^2)
#Space Complexity = (1)

def partition(arr, p, r):
  #choose pivot
  pivot = arr[p]
  i = p
  for  j in range(p+1, r+1):
    if arr[j] < pivot:
      i+=1
      arr[i],arr[j] = arr[j],arr[i]
  arr[p],arr[i] = arr[i],arr[p]
  return i

def quickSort(arr, p ,r):
  if p < r:
    q = partition(arr, p, r)
    quickSort(arr, p, q-1)
    quickSort(arr, q+1, r)

arr = [54,26,93,17,77,31,44,55]
quickSort(arr, 0 , len(arr)-1)
print(arr)