
#School Administrative Database
#Made by Oswin

print('Hey! User')
print('Enter what you want to do user')
print('You may add,show the table,remove a row,add sample data,clear the table')
print('Use add,show,remove,add_sample,clear_table respectively")

global data,samp_data
data = ["ADMNO TIME YEAR NAME COURSE SCORE","HP1240 1993 3 Harry_potter Potions C","HG1240 1993 3 Hermione_Granger Potions B",
        "RW3452 1993 3 Ron_Weasley Chess A","SS3452 1978 4 Severus_snape Potions A" ,"LP3452 1978 3 Lily_Potter Wizardry A","TR6753 1945 4 Tom_riddle Defence_Aginst_Dark_art A"]
samp_data = ["HP1240 1993 3 Harry_potter Potions C","HG1240 1993 3 Hermione_Granger Potions B",
        "RW3452 1993 3 Ron_Weasley Chess A","SS3452 1978 4 Severus_snape Potions A" ,"LP3452 1978 3 Lily_Potter Wizardry A","TR6753 1945 4 Tom_riddle Defence_Aginst_Dark_art A"]


def add():
    loop = True
    print('Enter data of the form [ADMNO NAME COURSE PHNO EMAILID]\nMind the spaces \n Say \'end\' to stop giving input')
    while loop:
        raw_data = str(input("Enter data[ADMNO TIME YEAR NAME COURSE SCORE]:"))
        if raw_data == 'end':
            loop = False
        else:
            loop = True
        data.append(raw_data)
        
def show():
    print('+-------------------------------------+')
    for row in data:
        word  = row.split(' ')
        w=''
        for d in word:
            w=w+(str(d)+'|')
        print(w)
        print('+'+int(len(w)-2)*'-'+'+')
        
def remove():
    ask = str(input("Emter ADMNO to remove:"))
    for rd in data:
        if ask in rd:
            data.remove(rd)
            
def add_sample():
    global data,samp_data
    data=data+samp_data

def clear_table():
    global data
    data=["ADMNO TIME YEAR NAME COURSE SCORE"]

#main_loop
while True:
    user  = input(":")
    if user == 'add':
        add()
    if user == 'show':
        show()
    if user == 'remove':
        remove()
    if user == 'add_sample':
        add_sample()
    if user == 'clear_table':
        clear_table()
