score = int(input('score number: '))
if score >= 60:
    if score < 70:
        print('grade is D')
    else:
        if score < 80:
            print('grade is C')
        else:
            if score < 90:
                print('grade is B')
            else:
                print('grade is A')
else:
    print('grade is F')













