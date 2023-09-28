Set1 = {1/(2**i) for i in range(1,5)} # Add Set Comprehension Code Here
Set2 = {i**2 for i in range(-2,3)} # Add Set Comprehension Code Here
Set3 = {i for i in range(1,25) if (24%i ==0)} # Add Set Comprehension Code Here
Set4 = {i for i in range(-10,11) if(i%2 != 0)} # Add Set Comprehension Code Here

# Note that sets do not maintain order so it may vary
print(Set1)
print(Set2)
print(Set3)
print(Set4)