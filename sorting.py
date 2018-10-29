
arr= []
n = int(input("Enter how many numbers you want to sort "))
for a in range(n):
  num = int(input("please enter a number "))
  arr.append(num)
for a in range(n-1):
  if(arr[a] > arr[a + 1]):
        temp = arr[a]
        arr[a] = arr[a + 1]
        arr[a + 1] = temp
    print(a)
print(arr)
