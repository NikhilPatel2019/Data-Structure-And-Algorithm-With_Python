def selection_sort(ar):
  for i in range(len(ar)-1):
    max_value = 90000
    min_index = i
    for j in range(min_index+1,len(ar)):
      if ar[j] < ar[min_index]:
        min_index = j
    ar[i],ar[min_index] = ar[min_index],ar[i]

arr = [9,8,7,6,5,4,3,2,1]
selection_sort(arr)
print(arr)