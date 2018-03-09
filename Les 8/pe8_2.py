import random
def monopolyworp():
    res1=random.randrange(1,7)
    res2=random.randrange(1,7)
    if res1==res2:
        print('{} + {} = {} (dubbel)'.format(res1,res2,res1+res2))
        res1 = random.randrange(1, 7)
        res2 = random.randrange(1, 7)
        if res1==res2:
            print('{} + {} = {} (dubbel)'.format(res1,res2,res1+res2))
            res1 = random.randrange(1, 7)
            res2 = random.randrange(1, 7)
            if res1==res2:
                print('{} + {} = (direct naar de gevangenis)'.format(res1,res2))
            else:
                 print('{} + {} = {}'.format(res1,res2,res1+res2))

        else:
            print('{} + {} = {}'.format(res1, res2, res1 + res2))
    else:
        print('{} + {} = {}'.format(res1, res2, res1 + res2))

print(monopolyworp())