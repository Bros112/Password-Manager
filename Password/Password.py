#__init__

Config = open('.proc/config.txt','a')
Config.writelines(['\n_','\n_','\n_','\n_']) 
Config.close()
sure = 0                                                #Maybe add 'are you sure?' prompt for settings

#Defining Functions

def replace_line(file_name, line_num, text):            #not mine but it was a pain to do myself
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text + '\n'
    Config = open(file_name, 'w')
    Config.writelines(lines)
    Config.close()                                      #End of coppied part

def attempts():
    Config=open('.proc/config.txt', 'r')
    replace_line('.proc/config.txt', 3, input('Enter the number of password attempts\n'))
    data = Config.readlines()
    Config.close
    try:
        int(data[3]) - 2
    except:
        print("That is not an integer")
        attempts()
    if int(int(data[3].replace('\n',''))) <= int('0'):             
        print('It has to be above 0')
        attempts()

#Admin Menu
def AdmnMenu():
    MenuNo = input('This is the admin menu\nWhat do you want to do?\nSee values(1)\nChange values(2)\nReset all config and exit(3)\nClose(4)\n')
    if MenuNo == '1':
        AdmnSee()
    if MenuNo == '2':
        AdmnChange()
    elif MenuNo == '3':
        replace_line('.proc/config.txt', 0, '')
        exit()
    elif MenuNo == '4':
        exit()

def AdmnSee():
    Config=open('.proc/config.txt', 'r')
    data = Config.readlines()
    Config.close
    print('\nPassword: ' + str(data[1]) +'Admin password: ' + str(data[2]) +'Password attemts: ' + str(data[3]) + '')
    input('(Press enter)\n')
    AdmnMenu()

def AdmnChange():
    changeNo = input('\nWhat do you want to change?\nPassword(1)\nAdmin password(2)\nNumber of pasword attempts(3)\nBack(4)\n')
    if changeNo == '1':
        replace_line('.proc/config.txt', 1, input('Enter a pasword\n'))
    elif changeNo == '2':
        replace_line('.proc/config.txt', 2, input('Enter an admin pasword\n'))
    elif changeNo == '3':
        attempts()
    elif changeNo == '4':
        AdmnMenu()
    else:
        print('Not valid input')
    AdmnChange()

#Start
def start():
    Config = open('.proc/config.txt','r')
    data = Config.readlines()
    if data[0][0] != '1':                                                   #First time?
        print('Welcome to the Password checker\nThis is the initialisation options')
        for i in range(0,1):
            Config.close()
            Config = open('.proc/config.txt','w')
            Config.write('1')                                               #Set to not first time
            Config.close()
            Config = open('.proc/config.txt','a')
            Config.writelines(['\n_','\n_','\n_','\n_'])                    #Password #Admin Password #Number of tries #Locked out?
            Config.close()
            replace_line('.proc/config.txt', 0, '1')
            replace_line('.proc/config.txt', 1, input('Enter a pasword\n'))
            replace_line('.proc/config.txt', 2, input('Enter an admin pasword\n'))
            Config.close()
            attempts()
            replace_line('.proc/config.txt', 4, '0')
            sure = 1
    else:
        Check()

#Password check
def Check():
        Config = open('.proc/config.txt','r')
        data = Config.readlines()
        Config.close
        Pass = data[1]
        AdmnPass = data[2]
        Attempts = int(data[3].replace('\n',''))
        AttemptsLft = Attempts #attempts left
        while AttemptsLft > int('0'):
            PassInp = input('Input password\n')
            if PassInp + '\n' == AdmnPass:
                AdmnMenu()
                AttemptsLft = 0
            if PassInp + '\n' == Pass:
                print('Correct!')
                AttemptsLft = 0
            elif PassInp + '\n' == Pass:
                print('Correct!')
                AttemptsLft = 0
            else:
                AttemptsLft -= 1
                print('Try again\n' + str(AttemptsLft) + ' attempts left')
                if AttemptsLft == 0:
                    replace_line('.proc/config.txt', 4, '1')




start()
