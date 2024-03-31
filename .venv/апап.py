
for b in range(0, 100):
    for c in range(0, 100):
        for t in range(0, 100):
            if (10*b + 5*c + 0.5*t == 100) and (b+c+t == 100):
                print('x =', b, 'y =', c, 'z =', t)

'''
для a от 0 до 100:

   для b от 0 до 100:

       для c от 0 до 100:

           если (10b + 5c + 0.5d = 100) и (b + c + d = 100):

               вывод a, b, c
               
'''