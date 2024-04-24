
def odds(x,y):
    # Forma 1
    initial = x  if x % 2 == 0 else x - 1
    print(list( range(initial,y) ) )
    
    # Forma 2 
    odd = lambda n: n % 2 ==0
    print(list( filter(odd, range(x,y)) ))

    # Forma 2 - Nao funcional
    for n in range(x, y):
        if n % 2 == 0:
            print(n)
    
if __name__ ==  "__main__":
    odds(32, 300)