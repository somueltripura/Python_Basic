# Set of python
data = [1,2,2,3,4,4]
unique_data = set(data)
print(unique_data)

#membership check
nums = {1,2,3}

if 2 in nums:
    print("YES")



#Data filtering common element declarare
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)
print(common)