for i in range(2, 201):
    if i>1:
        for j in range(2, i):
            if i%j == 0:
                break
            else:
                print(f'{i} is prime number')
                break
