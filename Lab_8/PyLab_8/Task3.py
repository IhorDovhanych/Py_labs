def act(i) :
    
    if i == 0:
        return 1
    elif i > 0:
        return act(i-1) + 2*i
    

print(act(10))
        
    