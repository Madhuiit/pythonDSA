n = 7 

# checking all the number between 2 to 6  does not divide the the nuber 7
print(all(n%i != 0 for i in range(2,int(n**0.5)+1)))