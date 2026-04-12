n=5
m=4

i=0
while i < n:
 j=0
 while j < m:
     if i==0 or i==n-1 or j==0 or j==m-1:
         print('1', end="")
     else:
         print('0', end="")
     j=j+1
 print()
 i=i+1
 

 
    
