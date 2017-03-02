import random
import time
import sys

state = 'punt'
position = 0
gscore = 0
hscore = 0
quarter = 1
round = 1

def displayBoard(guest, host, offense, position, gscore, hscore, state):
    guest_info = ' '
    host_info = ' '
    game_info = state
    print('')
    print('R U S H  Z O N E')
    if quarter > 4:
        print('Overtime ', end='')
    else:
        print('Quarter ' + str(quarter), end='')
    print(', Round ' + str(round))
    if offense > 0:
        guest_info = '*'
        if state == 'first down':
            if position <= 50:
                game_info = state + ' on ' + guest + ' ' + str(position)
            else:
                game_info = state + ' on ' + host + ' ' + str(100 - position) 
    else:
        host_info = '*'
        if state == 'first down':
            if position >= 50:
                game_info = state + ' on ' + host + ' ' + str(100 - position)
            else:
                game_info = state + ' on ' + guest + ' ' + str(position)

    print(guest + ': ' + str(gscore) + guest_info + \
          '        ' + host + ': ' + str(hscore) + host_info + \
          ' ' + game_info)
    print('Guest 0  10  20  30  40  50  40  30  20  10   0 Host')
    if len(guest) > len(host):
        height = len(guest)
    else:
        height = len(host)
    h = 0
    while h < height:
        if h < len(guest):
            gname = guest[h]
        else:
            gname = ' '
        if h < len(host):
            hname = host[h]
        else:
            hname = ' '
        print('  ' + gname, end="")
        i = 0
        while i < 11:
            if h == int(height/2) and i == int(position/10):
                if offense > 0:
                    print(' O->', end="")
                else:
                    print(' <-O', end="")
            else:
                print('   |', end="")
            i = i + 1
        print('  ' + hname)
        h = h + 1
    print('Guest 0  10  20  30  40  50  40  30  20  10   0 Host')        

def switch(offense):
    global quarter
    global round
    round = round + 1
    if round > 3:
        round = 1
        if quarter < 4:
            print('\nEnd of quarter ' + str(quarter) +'\n')
        quarter = quarter + 1
        if quarter == 5:
            if gscore != hscore:
                print('Game Over')
                if gscore > hscore:
                    print(guest + ' ' + str(gscore) + ' vs ' + \
                          host + ' ' + str(hscore) + '   ' + \
                          guest + ' won!')
                else:
                    print(guest + ' ' + str(gscore) + ' vs ' + \
                          host + ' ' + str(hscore) + '   ' + \
                          host + ' won!')
                sys.exit(0)
            else:
                print('\nGame tied, going to Overtime\n')
        if quarter > 5:
            print('Game Over')
            if gscore > hscore:
                print(guest + ' ' + str(gscore) + ' vs ' + \
                      host + ' ' + str(hscore) + '   ' + \
                      guest + ' won!')
            elif gscore < hscore:
                print(guest + ' ' + str(gscore) + ' vs ' + \
                      host + ' ' + str(hscore) + '   ' + \
                      host + ' won!')
            else:
                print(guest + ' ' + str(gscore) + ' vs ' + \
                      host + ' ' + str(hscore) + '   ' + \
                      'Tie')
            sys.exit(0)
            
    if offense < 0:
        return 1
    else:
        return -1

def touchdown(offense, position):
    if offense > 0 and position > 100:
        return True
    if offense < 0 and position < 0:
        return True
    return False

def targe_distance(offense, position):
    if offense > 0:
        return 100 - position
    else:
        return position

print('RUSH ZONE')
guest = input('Please provide guest (Tail) team\'s name: ')
host = input('Please provide host (Head) team\'s name: ')
print('Rolling the coin now...')
time.sleep(1)
if random.randint(0,1) == 1:
    print('It is Tail: ' + guest + ' gets the ball')
    offense = 1
    position = 0
else:
    print('It is Head: ' + host + ' gets the ball')
    offense = -1
    position = 100
print('Preparing to kick off...')
time.sleep(2)
              
while True:
    displayBoard(guest, host, offense, position, gscore, hscore, state)
    if offense < 0:
        offname = host
        defname = guest
    else:
        offname = guest
        defname = host

    waitEnter = True
    
    if state == 'punt':
        if offense < 0:
            position = 100
        else:
            position = 0
        punt_offense = random.randint(1,6)
        punt_defense = random.randint(1,6)
        punt_yard = (punt_offense - punt_defense) * 10
        if punt_yard <= 0:
            punt_yard = 20
        position = position + offense * punt_yard
        print(offname + ' point ' + str(punt_offense) + ', ' + defname + \
              ' point ' + str(punt_defense) + '. Ball on ' + offname + ' ' + \
              str(punt_yard))
        # input('Press Enter to continue...')
        state = 'first down'
        
    elif state == 'first down':
        # three downs at the same time
        o1 = random.randint(1,6)
        o2 = random.randint(1,6)
        o3 = random.randint(1,6)
        o = o1 + o2 + o3
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d = d1 + d2 + d3
        ostate = 1
        if o1==o2 or o1==o3 or o2==o3:
            ostate = 2
            if o1==o2 and o2==o3:
                ostate = 3
        dstate = 1
        if d1==d2 or d1==d3 or d2==d3:
            dstate = 2
            if d1==d2 and d2==d3:
                dstate = 3
        print(offname + ' point ' + str(o1) + '+' + str(o2) + '+' + str(o3) + \
              '=' + str(o) + ', ' + defname + ' point ' + str(d1) + '+' + str(d2) + \
              '+' + str(d3) + '=' + str(d) + '.')
        if dstate == 3 and ostate < 3:
            # Fumble
            print(offname + ' FUMBLE, lose ' + str(d1 * 10) + ' yards')
            offense = switch(offense)
            position = position + offense * d1 * 10
            if touchdown(offense, position):
                state = 'touchdown'
        elif ostate == 3:
            print(offname + ' Triple!')
            position = position + offense * o1 * 10
            if touchdown(offense, position):
                state = 'touchdown'
        elif ostate == 2:
            print(offname + ' Double!')
            position = position + offense * 20
            if touchdown(offense, position):
                state = 'touchdown'
        elif o >= d:
            print(offname + ' First Down!')
            position = position + offense * 10
            if touchdown(offense, position):
                state = 'touchdown'
        else:
            # Ask offense
            if targe_distance(offense, position) > 50:
                kick = 'punt'
            else:
                kick = 'field goal'
            oinput = ''
            while oinput != '1' and oinput != '2':
                oinput = input(offname + ': do you want to ' + kick + \
                               '(1) or go for it (2)? ')
            if oinput == '1':
                # kick
                kick_distance = random.randint(1,6)
                print(offname + ' kicked ' + str(kick_distance * 10) + \
                      ' yards')
                if kick == 'punt':
                    position = position + offense * kick_distance * 10
                    offense = switch(offense)
                    state = 'first down'
                else:
                    # field goal
                    if touchdown(offense, position + offense * kick_distance * 10):
                        print('Field goal ' + offname + '!')
                        if offense > 0:
                            # guest
                            gscore = gscore + 3
                        else:
                            hscore = hscore + 3
                        offense = switch(offense)
                        state = 'punt'
                    else:
                        print(offname + ' field goal attempt fails')
                        if targe_distance(offense, position) <= 20:
                            if offense > 0:
                                position = 80
                            else:
                                position = 20
                        offense = switch(offense)
                        state = 'first down'
            else:
                # go for it
                o4 = random.randint(1,6)
                d4 = random.randint(1,6)
                print(offname + ' point: ' + str(o1) + '+' + str(o2) + '+' + \
                      str(o3) + '+' + str(o4) + '=' + str(o+o4) + ', ' + \
                      defname + ' point: ' + str(d1) + '+' + str(d2) + '+' + \
                      str(d3) + '+' + str(d4) + '=' + str(d+d4))
                if (o + o4) >= (d + d4):
                    position = position + offense * 10
                    print('Fourth down conversion is good!')
                    if touchdown(offense, position):
                        state = 'touchdown'
                        waitEnter = False
                    else:
                        state = 'first down'
                else:
                    print('Fourth down failed')
                    offense = switch(offense)
                    state = 'first down'

    elif state == 'touchdown':
        print('TOUCHDOWN ' + offname + '!')
        oinput = ''
        while oinput != '0' and oinput != '1':
            oinput = input('Do you want to 2 point conversion (1) or not (0)? ')
        if oinput == '0':
            xp = 1
            waitEnter = False
        else:
            # 2 point conversion
            o1 = random.randint(1,6)
            d1 = random.randint(1,6)
            print(offname + ' point: ' + str(o1) + ', ' + defname + ' point: ' + str(d1))
            if o1 >= d1:
                print(offname + ' extra point is good')
                xp = 2
            else:
                print(offname + ' extra point no good')
                xp = 0
        
        if offense > 0:
            # guest
            gscore = gscore + 6 + xp
        else:
            hscore = hscore + 6 + xp
        offense = switch(offense)
        state = 'punt'

    else:
        print('Wrong state: ' + state)
        break

    if waitEnter:
        input('Press Enter to continue...')
