def print_doo():
    return ' doo' * 6


def baby_shark():
    sharks=["mommy","daddy","grandpa","grandmaa"]
    for shark in sharks:
        for index in range(3):print(shark+"sharks ,% s"%(print_doo()))
        print (shark+' shark!\n')
        for index in range(3):
            print('let\'s go hunt,%s'%(print_doo()))
            print('let\'s go hunt!\n\nRunway..')
baby_shark()