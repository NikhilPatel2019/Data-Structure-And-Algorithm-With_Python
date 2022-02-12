def insertionSort(arr):
  for i in range(1,len(arr)):
    key = arr[i]
    j = i - 1;
    while j>= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j = j - 1
    
    arr[j+1] = key

arr = [1,10,2,20,5]
insertionSort(arr)

for v in arr:
  print(v)

#Time Complexity = O(n^2) --> For Worst case
#Time Complexity = O(n) --> For Best case
#Space Complexity = O(1)  