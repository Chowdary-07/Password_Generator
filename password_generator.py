class score:
    #to calculation_score of password
    def __init__(self,cap_let,small_let,digits,charcters,str):
        self.cap_let=cap_let
        self.small_let=small_let
        self.digits=digits
        self.charcters=charcters
        self.str=str
    def calculation_score(self):
        cap=self.cap_let; small=self.small_let; dig=self.digits; sep=self.charcters
        #print(len(cap),len(dig),len(sep))
        if len(cap)>=2 and len(dig)>=2 and len(sep)>=2:
            if len(str) in range(11,30):
                    return ' Super Strong'
            else:
                return ' too long'
        elif len(cap)>=1 and len(dig)>=1 and len(sep)>=1:
            if len(str) in range(6,9):
                return ' Weak'
            elif  len(str) in range(8,13):
                return ' Moderate'
            elif  len(str) in range(13,30):
                return ' Strong'
            else:
                return ' too long'
class Generator:
    def __init__(self):
        pass
    def strong_password_generator(self):
        n=random.randint(8,12)
        strong_password_created=''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=n))
        return strong_password_created

    def super_strong_password_generator(self):
        m=random.randint(12,30)
        super_strong_password_created=''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=m))
        return super_strong_password_created
print('Password Generator')
choice=int(input('\t1.Test your password score\n\t2.Genrate new password \t\t\n'))
if choice==1:
    #Test password
    import re
    str=input('******\tIncldue Caps & Special characters\t*****\t\n\n\t\tPassword:')
    cap_let=re.findall('[A-Z]',str)
    small_let=re.findall('[a-z]',str)
    digits=re.findall('\d',str)
    charcters=re.findall('[^\w\s\d]|_',str)
    total_score=len(charcters)+len(digits)+len(cap_let)+len(small_let)
    #function for missing elements in password
    def cause(list_temp,str):
        if(len(str)<6):
            return 4
        else:
            temp=[]
            for i in range(len(list_temp)):
                if len(list_temp[i])==0:
                    temp.append(i)
            return temp
    while True:
        if len(cap_let)>=1 and len(small_let)>=1 and len(digits)>=1 and len(charcters)>=1 and len(str)>=6:
            print('\t\t\nPassword Valid')
            obj=score(cap_let,small_let,digits,charcters,str)
            temp_str=obj.calculation_score()
            print('\tYour password'+temp_str)
            break
        else:
            list_temp=[cap_let,small_let,digits,charcters]
            string_list=cause(list_temp,str)
            if string_list==4:
                print('\t\t\nPassword should be 6 characters')
            else:
                string_name=['Cap Letters are missed','Small Letters are missed','Digits are missed','Special characters are missed']
                for i in string_list:
                    print('\t\t'+string_name[i])
            break
elif choice==2:
    import string
    import random
    #Generate password
    choice_1=int(input('\t1.Strong\n\t2.Super Strong\t\t\n'))
    generator_obejct=Generator()
    while True:
        if choice_1==1:
            print(' Your Strong Password\t'+generator_obejct.strong_password_generator())
            break
        elif choice_1==2:
            print('Your Super Strong Password\t'+generator_obejct.super_strong_password_generator())
            break
        else:
            print('Invalid Entry')
else:
    print('Invalid Entry')
