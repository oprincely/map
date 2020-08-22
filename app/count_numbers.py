
def count_1s(number):
    one = [3,4]
    if number < one[0]:
        return 'no_1s'
    elif number > one[0] and one[1]:
        return 'many_1s'
    elif number == one[0] or one[1]:
        return 'average_1s'
    
def count_2s(number):
    two = [1]
    if number < two[0]:
        return 'no_2s'
    elif number > two[0]:
        return 'many_2s'
    elif number == two[0]:
        return 'average_2s'
    
def count_3s(number):
    three = [1]
    if number < three[0]:
        return 'no_3s'
    elif number > three[0]:
        return 'many_3s'
    elif number == three[0]:
        return 'average_3s'
    
def count_4s(number):
    four = [1]
    if number < four[0]:
        return 'no_4s'
    elif number > four[0]:
        return 'many_4s'
    elif number == four[0]:
        return 'average_4s'
    
def count_5s(number):
    five = [3,4]
    if number < five[0]:
        return 'no_5s'
    elif number > five[0] and five[1]:
        return 'many_5s'
    elif number == five[0] or five[1]:
        return 'average_5s'
    
def count_6s(number):
    six = [1]
    if number < six[0]:
        return 'no_6s'
    elif number > six[0]:
        return 'many_6s'
    elif number == six[0]:
        return 'average_6s'
    
def count_7s(number):
    seven = [0]
    if number == seven[0]:
        return 'no_7s'
    elif number > seven[0]:
        return 'many_7s'
    elif number == seven[0]:
        return 'average_7s'
    
def count_8s(number):
    eight = [0,1] #2
    if number > eight[1]: #0 and 1
        return 'many_8s'
    elif number == eight[1]: #1
        return 'average_8s'
    else:
        return 'no_8s'

#print(count_8s(1))

def count_9s(number):
    nine = [3]
    if number < nine[0]:
        return 'no_9s'
    elif number > nine[0]:
        return 'many_9s'
    elif number == nine[0]:
        return 'average_9s'
    
def vocation_pointer(b):
    vocation = []
    many_1s_and_8s = [] #business interest and you are not carried away by emotion.
    many_2s_and_3s_and_6s = [] #artistic ability, opportunity along professional lines, inspirational service, and instruction.
    many_4s_and_7s = [] #scientific, mechanical, and mathematical tendencies.
    many_5s = [] #versatility, also sales promotion and public administration.
    many_7s_and_9s = [] #literary ability
    many_8s = []#philosophical feeling expressed through printing and publishing, correspondence, and newspapers.
    
    if b == 'many_1s':
        many_1s_and_8s.append(b)
    elif b == 'many_2s':
        many_2s_and_3s_and_6s.append(b)
    elif b == 'many_3s':
        many_2s_and_3s_and_6s.append(b)
    elif b == 'many_4s':
        many_4s_and_7s.append(b)
    elif b == 'many_5s':
        many_5s.append(b)
    elif b == 'many_6s':
        many_2s_and_3s_and_6s.append(b)
    elif b == 'many_7s':
        many_4s_and_7s.append(b)
        many_7s_and_9s.append(b)
    elif b == 'many_8s':
        many_1s_and_8s.append(b)
        many_8s.append(b)
    elif b == 'many_9s':
        many_7s_and_9s.append(b)
        
    #print('many_2s_and_3s_and_6s = ',many_2s_and_3s_and_6s)
        
    for v in many_1s_and_8s:
        if 'many_1s' and 'many_8s' in many_1s_and_8s:
            vocation.append('many_1s_and_8s')
            
    for v in many_2s_and_3s_and_6s:
        if 'many_2s' and 'many_3s' and 'many_6s' in many_2s_and_3s_and_6s:
            vocation.append('many_2s_and_3s_and_6s')
            
    for v in many_7s_and_9s:
        if 'many_7s' and 'many_9s' in many_7s_and_9s:
            vocation.append('many_7s_and_9s')
            
    for v in many_8s:
        if 'many_8s' in many_8s:
            vocation.append('many_8s')
            
    for v in many_5s:
        if 'many_5s' in many_5s:
            vocation.append('many_5s')
            
    for v in many_4s_and_7s:
        if 'many_4s' and 'many_7s' in many_4s_and_7s:
            vocation.append('many_4s_and_7s')
    return vocation
