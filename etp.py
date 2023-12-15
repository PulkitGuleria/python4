# Python3 implementation of the approach

# NUM = 31

# # Function to calculate the position
# # of characters
# def positions(str):
# 	for i in str:
		
# 		# Performing AND operation
# 		# with number 31
# 		print((ord(i) & NUM), end =" ")

# # Driver code
# str = "yfvkhvbk"
# positions(str)

str = input("")
for i in range(0,len(str)):
    if i %2 == 0:
        print(str[i].upper(),end="")
    else:
        print(str[i],end="")