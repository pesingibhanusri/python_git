# Check if the list is already sorted or not. Ascending or descending

# ascending=1,2,3
# descending=5,4,3


list1=[5,4,3,2,1]
flag_ascending=True
flag_descending=True
for i in range(len(list1)-1):
     if list1[i]>list1[i+1]:
        flag_ascending=False
     elif list1[i]<list1[i+1]:
         flag_descending=False

if flag_ascending:
   print("ascending")
elif flag_descending:   
   print("descending")
else :
    print("not sorted")


#  Check if an array is a subset of another or not.

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 2, 3,56]

for i in range(len(arr2)):
    flag = False  
    for j in range(len(arr1)):
        if arr2[i] == arr1[j]:
            flag = True
            break  
    if not flag: 
        print("not subset")
        break
else:  
    print("subset")

# Check if a + b = target exists in a list

list1 = [1, 2, 3, 4]
target = 5
flag = False  


for i in range(len(list1)):
    for j in range(i + 1, len(list1)):  
        if list1[i] + list1[j] == target:
            flag = True 
            break 
    if flag:  
        break


if flag:
    print("exists")
else:
    print("not exists")
 


# 2. Missing number in a list. [1, 2, 3, 5,6,7,9, 8]
# 	1. Sum of n numbers using formulae - Sum of elements in list
# 	2. 2 loops method
# 	3. xor method.
# 	4. Sorting

nums=[1,2,3,5,6,7,8,9]
n=9
expected_sum=n*(n+1)//2
actual_sum=sum(nums)
missing_number = expected_sum - actual_sum
print(missing_number)


# ////////////////////////////////


nums = [1, 2, 3, 4, 6, 7, 9, 8]
for i in range(1, 10):
    if i not in nums:  
        missing_number = i  
        break  

print("Missing number", missing_number)
