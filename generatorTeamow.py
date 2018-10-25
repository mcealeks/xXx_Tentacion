import random 

gracze = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'J', 'G', 'K']


def genTeam(lista):
    random.shuffle(gracze)
    polowaListy = len(gracze) //2
    team1 = gracze [ 0: polowaListy ]
    team2 = gracze [polowaListy : ]
    return team1,team2
(1,2) [0]
a = genTeam( [1,2,3,4,5,6,7,8,9] )
print(a[0])
print(a[1])
