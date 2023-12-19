f_positive = ['good','not bad','excellent','fine','great','epic','wonderful','nice']
f_negative = ['bad','not good','worst','not fine','meh','normal','okay','sucks','trash']
name = input("What is your name ?\n")
f = input('Hello lil '+ name +"...how's lyf ?\n" ).lower()
for i in f_positive:
    if i in f:
        print('Good to hear that..')
        s = input('May I know why is it so ??\n').lower()
        if 'no' in s:
            print("Alright your choice")
        else:
            print('Ohhhh.. ')
        
for i in f_negative:
    if i in f:
        print("Aww too bad.. i thought it would be good")
        s = input('Why is it so ?\n').lower()
        if  'i dont know' in s or 'idk' in s:
            t = input('Do u want me to help you ?\n').lower()
            if 'yes' in t or 'yeah'  in t or 'maybe' in t:
                print("Go to gym. Hehe (No but srsly gym helps)")
                fo = input('Will you ?\n').lower()
                if 'yes' in fo or 'yeah'  in fo:
                    print('Good for you')
                elif 'no' in fo or 'nope' in fo or 'nah' in fo:
                    print('Noob')
                else:
                    print('Hmmm alright.')
            elif 'no' in t or 'nope' in t or 'nah' in t:
                print('Sucks for you.')
        else:
            print('Ohhh okay...eveyrthing is going to be fine ')

fif = input('btw..where r u from ?\n').lower()
print('hmmmm...',fif+".... never heard of that place")
six = input('Is it in India ?\n').lower()
if 'yes' in six or 'yeah'  in six:
    print('I would like to visit it someday then.')
elif 'idk' in six or 'i dont know' in six or 'maybe' in six:
    print('Dude how do u not know..u live there')
else:
    print('International... i see :)')
seven = input('Where are u right now ?\n').lower()
if fif in seven or 'home' in seven:
    print("Oh that's nice")
else:
    eig = input('Will you go back home soon ?\n').lower()
    if 'yes' in eig or 'yeah'  in eig or 'maybe' in eig:
        print("Oh that's nice")
    else:
        print("you should visit.")
nin = input("Do you have a family ?\n").lower()
if 'yes' in nin or 'yeah'  in nin:
    print("Ahh shucks.... i thought i could adopt you")
else:
    ten = input('Can i adopt you ?\n').lower()
    if 'yes' in ten or 'yeah'  in ten:
        print('Soon Enough.. i will')
    elif 'idk' in ten or 'i dont know' in ten or 'maybe' in ten:
        print('I will give enough time to think then')
    else:
        print('Well... your loss')
print('Adios amigo !!')


    