import math

def sigma2():

    i = 0
    
    prev = 0.0
    current = 1.0
    
    print(current)
    
    while(i < 300):
    
        prev = current
        
        current = math.cos(prev)
        
        print(current)
        
        i += 1
        
        
def main():


    sigma2()
    
    
main()
        
