#field betting
import random
min = 1
max = 6
def dice_roll():
    d1 = random.randint(min,max)
    d2 = random.randint(min,max)
    total = d1 + d2
    return total
def padovan(n):
    if n < 1:
        return "Error"
    elif n > 0 and n < 4:
        return 1
    else:
        return padovan(n - 2) + padovan(n - 3)
def payout(roll):
    if roll == 2:
        pay = 2
    elif roll >2 and roll < 5:
        pay = 1
    elif roll > 8 and roll < 12:
        pay = 1
    elif roll == 12:
        pay = 3
    else:
        pay = 0
    return pay
startcash = int(raw_input("starting cash: "))
table_min = int(raw_input("table minimum: "))
table_max = int(raw_input("table maximum: "))
#take = int(raw_input("target take: "))
runs = int(raw_input("number of times to run: ")) 
turn = 0
totaliter = 0
truemax = 0
def fieldloop(startcash, table_min, table_max):
    bankroll = startcash
    unit = table_min
    win = False
    sequence = 1
    totalcount = 0
    bet = 0
    maxbank = 0
    #take = startcash * 4
    #starting the loop
    while (bankroll > 0):
        #if bankroll > take:
        #    return bankroll, maxbank
        if not win:
            bet = unit * padovan(sequence)
            if (bet > table_max) or (bankroll - bet <= 0):
                break
            if totalcount > 50:
                break
            roll = int(dice_roll())
            #print("Bet: %s Roll: %s\n" % (bet, roll))
            pays = payout(roll)
            if pays > 0:
                payment = (pays * bet)
                bankroll += payment
                if bankroll > maxbank:
                    maxbank = bankroll
                #print("Win: %s Bankroll: %s\n" % (payment, bankroll))
                totalcount += 1
                win = True
            else:
                bankroll -= bet
                #print("Lose! Bankroll: %s\n" % bankroll)
                totalcount += 1
                sequence += 1
        else:
            bet *= 2
            roll = int(dice_roll())
            #print("Bet: %s Roll: %s\n" % (bet, roll))
            pays = payout(roll)
            if pays > 0:
                win = False
                payment = (pays * bet)
                bankroll += payment
                if bankroll > maxbank:
                    maxbank = bankroll
                #print("Win: %s Bankroll: %s\n" % (payment, bankroll))
                totalcount += 1
                sequence = 1
            else:
                bankroll -= bet
                #print("Lose! Bankroll: %s\n" % bankroll)
                win = False
                sequence += 1
                totalcount += 1      

    return bankroll, maxbank
while turn < runs:
    iter, maxbank = fieldloop(startcash, table_min, table_max)
    if maxbank >  truemax:
        truemax = maxbank
    print ("%s\n" % iter)
    totaliter += iter
    turn += 1
print ("total played: %s total won : %s profit: %s avg winning: %s max win: %s" % (startcash * runs, totaliter, totaliter - (startcash * runs), (totaliter / runs)- startcash, truemax))
