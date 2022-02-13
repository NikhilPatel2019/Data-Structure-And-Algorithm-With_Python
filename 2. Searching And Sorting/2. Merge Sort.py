#Time Complexity = O(n log n)
#Space Complexity = O(n)

def merge_sort(arr):
  if len(arr) <= 1:
    return
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]

  merge_sort(left)
  merge_sort(right)

  merge_two_sorted_array(left,right,arr)

def merge_two_sorted_array(a,b,arr):
  len_a = len(a)
  len_b = len(b)
  i = j = k = 0

  #Comparing Both the arrays
  while i < len_a and j <len_b:
    if a[i] <= b[j]:
      arr[k] = a[i]
      i+=1
    else:
      arr[k] = b[j]
      j+=1
    k+=1
  #Inserting Remaining Elements into an array
  while i<len_a:
      arr[k] = a[i] 
      i+=1
      k+=1
  while j<len_b:
      arr[k] = b[j]
      j+=1
      k+=1

a1 = [9,8,7,6,5,4,3,2,1]

print(merge_sort(a1))
print(a1)
