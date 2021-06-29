tRoom, tCond = input().split(' ')
tRoom = int(tRoom)
tCond = int(tCond)
mode = input()

if (mode == 'fan') or (tRoom > tCond and mode == 'heat') or (tRoom < tCond and mode == 'freeze'):
    print(tRoom)
else:
    print(tCond)
