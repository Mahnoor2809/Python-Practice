 import random
 lst = []
 for i in range(0,10):
  lst.append(random.randint(100,1000))
 print(lst)
 min_val = 0
 min_idx = 0
 for i in range(len(lst) - 1):
    if i==0: 
       if lst[i] < lst[i + 1]:
         min_val = lst[i]
         min_idx = i
       else:
         min_val = lst[i + 1]
         min_idx = i + 1
     else:
        if min >lst[i]
           min_val = lst[i]
           min_idx = i 
        
     print("Minimum Value", min_val)
     print("Minimum Index", min_idx)