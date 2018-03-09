import random
def monopolyworp():
    Teller = 0
    res1=random.randrange(1,7)
    res2=random.randrange(1,7)
    while res1 == res2:
        print('{} + {} = {} (dubbel)'.format(res1, res2, res1 + res2))
        if  Teller < 3:
            Teller = Teller + 1
            res1 = random.randrange(1, 7)
            res2 = random.randrange(1, 7)
        else:
            print('{} + {} = (direct naar de gevangenis)'.format(res1, res2))
            break

    print('{} + {} = {}'.format(res1, res2, res1 + res2))

monopolyworp()
