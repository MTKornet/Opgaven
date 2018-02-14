def new_password(old,new):
    return new != old and len(new)>=6
oldpassword = input('Wat is uw oude wachtwoord!')
newpassword = input('Wat is uw nieuwe wachtwoord!')
while not new_password(oldpassword,newpassword):
    oldpassword = input('Wat is uw oude wachtwoord!')
    newpassword = input('Wat is uw nieuwe wachtwoord!')