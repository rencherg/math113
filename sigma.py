

def sigma(a1, num):

    total = a1
    prev = a1
    i = 2
    
    print('a1: ' + str(prev))

    while(i < num + 1):
    
        if(((i-1) % 2) == 0):
        
            prev = (prev * 0.5)
            
            total += prev

        else:
        
            prev = ((3 * prev) + 1)
            
            total += prev
            
        
        print('a' + str(i) + ': ' + str(round(prev, 4)))
        
        if((i % 5) == 0):
        
            print()
            
        i += 1
            

def main():

    a1 = 25
    num = 40
    
    sigma(a1, num)
            
    
    
main()
            
