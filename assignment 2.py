lst = [2, 5, 4, 78, 85, 4, 6, 7]

def evenorodd(*args):
    
    for i in args:
        if i%2 ==0:
            print(f'{i} is even')
        else:
            print(f'{i} is odd')

evenorodd(*lst)