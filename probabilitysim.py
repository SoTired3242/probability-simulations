import random

def is_string_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def is_string_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def factorial(n):
    if is_string_int(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    else :
        raise ValueError("Factorial is not defined for non-integer")

def combination(x,y):
    if is_string_int(x) and is_string_int(y):
        if x>y:
            return factorial(int(x))/(factorial(int(y))*factorial((int(x)-int(y))))
        elif x==y:
            thething = 1
            return thething
        else:
            raise ValueError("Factorial is not defined when the first number is less than the second")
    else:
        raise ValueError("Combination is not defined for non-integer")

def coinflipanswer(coinnum,headnum,tailnum):
    if is_string_int(headnum) and is_string_int(tailnum) and is_string_int(coinnum):
        coinnum = int(coinnum)
        headnum = int(headnum)
        tailnum = int(tailnum)
        if headnum+tailnum == coinnum:
            if headnum == 0 and tailnum == 0:
                raise ValueError("Please make sure that only one variable (headnum or tailnum) is 0")
            else:
                ans1 = (combination(coinnum,headnum))/(2**coinnum)
                return ans1
        else:
            raise ValueError("Head count and tail count dont add up to total number of coins, please note coins landing on their edges isnt represented in this simulation :)")
    else:
        raise ValueError("Coinflipsim requires headnum, tailnum and coinnum to be integers.")

def coinflipsim(coinnum2,headnum2,tailnum2, simnum):
    if is_string_int(headnum2) and is_string_int(tailnum2) and is_string_int(coinnum2) and is_string_int(simnum):
        coinnum2 = int(coinnum2)
        headnum2 = int(headnum2)
        tailnum2 = int(tailnum2)
        simnum = int(simnum)
        if headnum2+tailnum2 == coinnum2:
            headcounter = 0
            tailcounter = 0
            successcounter = 0
            for i in range(0,simnum):
                for i in range(0,coinnum2):
                    randomthing = random.randint(1,2)
                    if randomthing == 1:
                        headcounter += 1
                    elif randomthing == 2:
                        tailcounter += 1
                    else:
                        print("error, something wrong happened")
                    if headcounter == headnum2 and tailcounter == tailnum2:
                        successcounter += 1
                headcounter = 0
                tailcounter = 0
            if simnum > 0:
                return (successcounter/simnum)
            else:
                raise ValueError("Simnum must be greater than 0")
        else:
            raise ValueError("Coinflipsim requires headnum and tailnum to add up to total number of coins")
    else:
        raise ValueError("Coinflipsim requires headnum, tailnum and coinnum to be integers.")

def montyhallanswer(n,g): #where n is number of doors and g is number of goats revealed after your pick
    if is_string_int(n) and is_string_int(g):
        n = int(n)
        g = int(g)
        if n>g and g>0 and n>0:
            return (n-1)/(n*(n-g-1))
        else:
            raise ValueError("Number of goats must be less than number of doors, and both goats and doors must be greater than 0")
    else:
        raise ValueError("Montyhall requires all variables to be integers")


def montyhallsim(n,g,simnum2):
    if is_string_int(n) and is_string_int(g) and is_string_int(simnum2):
        if g<n and g>0 and n>0 and simnum2>0:
            if g+1!=n:
                yaycounter = 0
                for i in range(0,simnum2):
                    mylist=[]
                    # creates a baseline (n bad doors)
                    for i in range(0, n):
                        mylist.append("bad")
                    #makes one door good (n-1 bad doors, 1 good)
                    goodoor = random.randint(0,len(mylist)-1)
                    mylist[goodoor]="good"

                    #chooses a random door and saves whether the door is good or bad
                    chosen = random.randint(0,len(mylist)-1)
                    chosenstr = str(mylist[chosen])

                    #sets g doors that arent the good or chosen one to be revealed
                    for i in range(0,len(mylist)-1):
                        if mylist[i] == chosen or mylist[i] == "good":
                            continue
                        else:
                            mylist[i] = "revealed"
                            if(mylist.count("revealed")==g):
                                break

                    #goes thru all the revealeds and deletes them
                    for i in range(0,mylist.count("revealed")):
                        mylist.remove("revealed")

                    #removes the chosen one as well (since we are switching  always in the sim we dont need it anymore)
                    mylist.remove(chosenstr)
                    #chooses a random term from the remaining doors (the remaining doors are the one we didnt choose and the g doors that were revealed
                    switchanswerstr = str(mylist[random.randint(0,len(mylist)-1)])
                    if switchanswerstr == "good":
                        yaycounter += 1
                return yaycounter/simnum2
            else:
                raise ValueError("This mathematically doesnt work, difference between num of doors and num of doors revealed cant be 1")
        else:
            raise ValueError("Montyhall requires all variables to be greater than 0 and for the number of doors revealed to be less than the total number of doors")
    else:
        raise ValueError("Montyhall requires all variables to be integers")


a = 4
b = 2
print(montyhallsim(a,b,10000000000))
print(montyhallanswer(a,b))