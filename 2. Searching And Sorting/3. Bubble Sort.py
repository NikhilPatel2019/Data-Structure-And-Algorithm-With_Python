#Time Complexity(Worst Case) = O(n^2)
#Time Complexity(Best Case) = O(n)
#Space Complexity = O(1)

lst = [9,8,7,6,5,4,3,2,1]

def bubble_sort(arr):
  for i in range(len(arr)-1):
    #Traverse through only unsorted list
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]


print("Before Sorting: ", lst)
bubble_sort(lst)
print("After Sorting:  ", lst)

#Optimized Bubble Sort
print("----------Optimized Bubble Sort---------------")
def optimized_bubble_sort(arr):
  for i in range(len(arr)-1):
    flag = False
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        flag = True
        arr[j],arr[j+1] = arr[j+1],arr[j]
    if not flag:
      return

lst2 = [1,2,9,8,6,5,4]
print("Before Sorting: ", lst2)
optimized_bubble_sort(lst2)
print("After Sorting: ", lst2)
