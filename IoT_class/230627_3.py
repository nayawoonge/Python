#3배수, 5배수 합 while문

sum = 0 
i = 1
while i<=30 :
  if i % 3 == 0 or i % 5 == 0 :
    sum += i
  i += 1
  
print(sum)