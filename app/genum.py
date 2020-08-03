import pandas as pd
import numpy as np

#from flask import Blueprint, redirect, render_template, request, url_for
import datetime


from app.hello import contains_y,jeff,digit_sum, check_karma

from app.hello1 import r0_all_missing,r0_all,r1_all,r1_all_missing,r2_all,r2_all_missing,r3_all,r3_all_missing,r4_all
from app.hello1 import r4_all_missing,r5_all,r5_all_missing,r6_all,r6_all_missing,r7_all,r7_all_missing,missing_numbers,s_num

import collections
from collections import OrderedDict

x = datetime.datetime.now()
year_now = x.year
month_now = x.strftime("%m")
day_now = x.strftime("%d")

def generate_numbers(FN,MN,LN,btd1,btm1,bty1):
    ####################
    btd = int(btd1)
    btm = int(btm1)
    bty = int(bty1)
    
    if MN == '':
        name2 = contains_y(FN[len(FN)-1]).upper()
        name1 = contains_y(FN[:len(FN)-1]).upper()
    else:
        name2 = contains_y(MN).upper()
        name1 = contains_y(FN).upper()
        
    name3 = contains_y(LN).upper()
    
    k1=jeff(name1)
    sE=k1[0]
    vo=k1[1]
    co=k1[2]
    
    k2=jeff(name2)
    sE1=k2[0]
    vo1=k2[1]
    co1=k2[2]
    
    k3=jeff(name3)
    sE2=k3[0]
    vo2=k3[1]
    co2=k3[2]
    
    individual_expression_in_names = (sE+sE1+sE2)
    
    ##########going for expression or desiney number
    
    destiny_number = digit_sum(digit_sum(individual_expression_in_names))
    karma_in_destiny = check_karma(individual_expression_in_names)
    
    exp = karma_in_destiny
    karma1 = check_karma(karma_in_destiny) #check karma in expression
    exp11 = destiny_number
    
    ##########going for soul urge or heart desire number
    individual_vowels_in_names = (vo+vo1+vo2)
    
    heart_desire = digit_sum(digit_sum(individual_vowels_in_names))
    karma_in_heart_desire = check_karma(digit_sum(individual_vowels_in_names))
    sU = heart_desire
    sU1 = individual_vowels_in_names
    
    individual_imagenumber_in_names = (co+co1+co2) #image number or personality the consulnants in names
    personality  = digit_sum(digit_sum(individual_imagenumber_in_names))
    iM = individual_imagenumber_in_names
    iM1 = personality
    
    #heart_desire and personality brigde
    hP = abs(sU - iM1)
    
    #############Everything Numbers###################
    bd = [int(x) for x in str(btd)]
    bm = [int(x) for x in str(btm)]
    by = [int(x) for x in str(bty)]
    
    s = bd + bm + by #list all numbers and sum
    
    #birthday - 22 and 11
    # if birthday is 9
    if btd == 11:
        bd1 = btd #2
        bd22 = 11
    elif btd == 22:
        bd1 = digit_sum(btd) #4
        bd22 = 22
    elif btd == 29:
        bd1 = digit_sum(digit_sum(btd)) #2
        bd22 = digit_sum(btd) #11
    else:
        bd1 = digit_sum(btd) #13=4
        bd22 = 0
                
    karma2 = check_karma(btd1)
    
    birth_force = digit_sum(digit_sum(sum(s))) #life path
    karma_in_birth_force = check_karma(sum(s))
    ln = karma_in_birth_force
    lp = birth_force
    karma = karma_in_birth_force
    
    lb = abs(lp - bd1) #birthday and life path brigde
    
    #things current
    sum_bd = sum(bd)
    sum_bm = sum(bm)
    sum_by = digit_sum(sum(by))
    for_py = digit_sum(sum_bd + sum_bm)
    
    cy1 = digit_sum(digit_sum(year_now)) #current year
    
    #personal year number bd + bm + cy1
    py_num = digit_sum(digit_sum((sum_bd + sum_bm + cy1)))# personal year
    
    #Your Life Path - Expression Bridge
    LEB = abs(birth_force - destiny_number)
    
    reality_number = digit_sum(destiny_number + birth_force)
    Mrity = reality_number
    
    list_name = list(name1 + name2 + name3)
    join_all_apha_in_name = ''.join(list_name)
    
    convert_alpha_in_name_to_number = [ord(char.lower())-96 for char in join_all_apha_in_name if char.lower()
                                   in join_all_apha_in_name.lower()]
    
    new_convert_alpha_in_name_to_number = [] #[5, 4, 5, 2, 1, 3, 3, 8, 3, 8, 3, 2, 5, 3, 6, 2, 5, 3]
    for i in convert_alpha_in_name_to_number:
        summed = digit_sum(i)
        new_convert_alpha_in_name_to_number.append(summed)
    
    freq = collections.Counter(new_convert_alpha_in_name_to_number)# Counter({3: 6, 5: 4, 2: 3, 8: 2, 4: 1, 1: 1, 6: 1})
    
    physical = freq[4] + freq[5]
    mental = freq[1] + freq[8]
    emotional = freq[2] + freq[3] + freq[6]
    intuitive = freq[7] + freq[9]
    phy = physical
    men = mental
    emo = emotional
    intt = intuitive
    
    #point of security
    point_of_security = digit_sum(digit_sum(physical + mental + emotional + intuitive))
    ps = point_of_security
    
    #specialized trait and point of intensification
    how_many_one = freq[1] #1 [3 or 4]
    how_many_two = freq[2] #3 [1]
    how_many_three = freq[3] #6 [1]
    how_many_four = freq[4] #1 [1]
    how_many_five = freq[5] #5 [3 or 4]
    how_many_six = freq[6] #1 [1]
    how_many_seven = freq[7] # 0 [0]
    how_many_eight = freq[8] # 2 [1 or 0]
    how_many_nine = freq[9] #0 [3 or more]
    one = how_many_one
    two = how_many_two
    thr = how_many_three 
    fou = how_many_four
    fiv = how_many_five
    six = how_many_six
    sev = how_many_seven
    eig = how_many_eight
    nin = how_many_nine
    
    #missing numbers in name
    exp_list = k1[3] + k1[4] + k2[3] + k2[4] + k3[3] + k3[4] #[5, 5, 1, 0, 4, 2, 3, 5, 3, 3, 0, 3, 8, 3, 8, 2, 5, 6, 3, 0, 2, 5]
    gen_list = [1,2,3,4,5,6,7,8,9]
    s1 = set(exp_list) #{0, 1, 2, 3, 4, 5, 6, 8}
    cha = [x for x in gen_list if x not in s1]
    
    #challenges
    first_challenge = abs((digit_sum(sum(bm))) - (digit_sum(sum(bd))))
    second_challenge = abs((digit_sum(sum(bd))) - (digit_sum(sum(by))))
    third_challenge = abs(first_challenge - second_challenge)
    fourth_challenge = abs((digit_sum(sum(bm))) - (digit_sum(sum(by))))
    cH = first_challenge
    cH1 = second_challenge
    cH2 = third_challenge
    cH3 = fourth_challenge
    
    #pinnacles
    first_pinnacle = digit_sum((digit_sum(sum(bm))) + (digit_sum(sum(bd))))
    second_pinnacle = digit_sum((digit_sum(sum(bd))) + (digit_sum(sum(by))))
    third_pinnacle = digit_sum(first_pinnacle + second_pinnacle)
    fourth_pinnacle = digit_sum((digit_sum(sum(bm))) + (digit_sum(sum(by))))
    p1 = first_pinnacle
    p2 = second_pinnacle
    p3 = third_pinnacle
    p4 = fourth_pinnacle
    
    #pinnacles starts
    first_pinnacle_starts = 36 - birth_force
    first_pinnacle_ends = first_pinnacle_starts + 9
    p11 = first_pinnacle_starts
    
    second_pinnacle_starts = first_pinnacle_ends + 1
    second_pinnacle_ends = second_pinnacle_starts + 9
    p22 = second_pinnacle_starts
    
    third_pinnacle_starts = second_pinnacle_ends + 1
    third_pinnacle_ends = third_pinnacle_starts + 9
    p33 = third_pinnacle_starts
    
    fourth_pinnacle_starts = third_pinnacle_ends + 1
    fourth_pinnacle_ends = third_pinnacle_starts + 9
    p44 = fourth_pinnacle_starts
    
    #print(third_pinnacle_starts,third_pinnacle_ends)
    
    #using pandas to table events
    ##########################################
    def getFirstLetter(d):
        bank = ['0']
        uppercase = list(d.upper())
        for i in uppercase:
            if i in ['A','J','S']:
                firstLetterList = i*1
                bank.append(firstLetterList)
            elif i in ['B','K', 'T']:
                firstLetterList = i*2
                bank.append(firstLetterList)
            elif i in ['C','L','U']:
                firstLetterList = i*3
                bank.append(firstLetterList)
            elif i in ['D','M', 'V']:
                firstLetterList = i*4
                bank.append(firstLetterList)
            elif i in ['E','N','W']:
                firstLetterList = i*5
                bank.append(firstLetterList)
            elif i in ['F','O', 'X']:
                firstLetterList = i*6
                bank.append(firstLetterList)
            elif i in ['G','P','Y']:
                firstLetterList = i*7
                bank.append(firstLetterList)
            elif i in ['H','Q', 'Z']:
                firstLetterList = i*8
                bank.append(firstLetterList)
            elif i in ['I','R']:
                firstLetterList = i*9
                bank.append(firstLetterList)
        jbank = ''.join(bank)
        return jbank
    
    def Lettered_name(name):
        pure_bank1 = getFirstLetter(name)
        pure_bank2 = (getFirstLetter(name).strip('0'))*3
        letter_bank = pure_bank1 + pure_bank2
        l = len(letter_bank) - 55
        new_letter_bank = letter_bank[:-l]
        #print(len(letter_bank),l,len(new_letter_bank))
        return new_letter_bank
    
    #print(Lettered_name(name2))
    
    def numInName(g):
        numInNames = [ord(char.lower())-96 for char in g]
        v = [digit_sum(digit_sum(x)) for x in numInNames]
        return [0]+v
    
    #numInName((Lettered_name(str(name1)).strip('0')))
    
    #taking care of lenght issue
    def fillent(r1,r2,r3):
        d = [r1,r2,r3]
        l = max(d, key=len)
        maxOne = len(l)#51
        new_r1 = r1 + [0] * (maxOne - len(r1))
        new_r2 = r2 + [0] * (maxOne - len(r2))
        new_r3 = r3 + [0] * (maxOne - len(r3))
        return new_r1,new_r2,new_r3
    
    #################
    
    p_month = digit_sum(int(month_now) + py_num)
    
    p_day_cal = digit_sum(digit_sum(int(day_now)) + digit_sum(int(month_now)) + py_num)
    k_pday = p_day_cal
    p_day = digit_sum(p_day_cal)
    
    uni_day_cal = digit_sum(int(month_now)) + digit_sum(digit_sum(int(day_now))) + digit_sum(digit_sum(year_now))
    
    k_day = uni_day_cal
    uni_day = digit_sum(uni_day_cal)
    
    #universal monthly pinnacle and
    first_pinnacle_of_the_day = digit_sum(int(month_now)) + digit_sum(digit_sum(int(day_now)))
    second_pinnacle_of_the_day = digit_sum(int(month_now)) + digit_sum(digit_sum(year_now))
    third_pinnacle_of_the_day = first_pinnacle_of_the_day + second_pinnacle_of_the_day
    final_pinnacle_of_the_day = digit_sum(int(month_now)) + digit_sum(digit_sum(year_now))
    Gpina = final_pinnacle_of_the_day
    
    #universal monthly challenge
    first_challenge_of_the_day = abs(digit_sum(int(month_now)) - digit_sum(digit_sum(int(day_now))))
    second_challenge_of_the_day = abs(digit_sum(int(month_now)) - digit_sum(digit_sum(year_now)))
    third_challenge_of_the_day = abs(first_pinnacle_of_the_day - second_pinnacle_of_the_day)
    final_challenge_of_the_day = abs(digit_sum(int(month_now)) - digit_sum(digit_sum(year_now)))
    Gcha = final_challenge_of_the_day
    
    #personal day pinnacles and
    first_pinnacle_of_the_pday = first_pinnacle_of_the_day
    second_pinnacle_of_the_pday = digit_sum(int(month_now)) + py_num
    third_pinnacle_of_the_pday = first_pinnacle_of_the_pday + second_pinnacle_of_the_pday
    final_pinnacle_of_the_pday = digit_sum(int(month_now)) + py_num
    Gper_pi = final_pinnacle_of_the_pday
    
    #personal day challenges
    first_challenge_of_the_pday = first_challenge_of_the_day
    second_challenge_of_the_pday = abs(digit_sum(int(month_now)) - py_num)
    third_challenge_of_the_pday = abs(first_pinnacle_of_the_pday - second_pinnacle_of_the_pday)
    final_challenge_of_the_pday = abs(digit_sum(int(month_now)) - py_num)
    Gper_cha = final_challenge_of_the_pday
    
    #which pinnacle is current
    age_now = year_now - bty
    
    if age_now in range(first_pinnacle_starts,first_pinnacle_ends):
        curr_pina = first_pinnacle
    elif age_now in range(second_pinnacle_starts,second_pinnacle_ends):
        curr_pina = second_pinnacle
    elif age_now in range(third_pinnacle_starts,third_pinnacle_ends):
        curr_pina = third_pinnacle
    elif age_now in range(fourth_pinnacle_starts,fourth_pinnacle_ends):
        curr_pina = fourth_pinnacle
    else:
        curr_pina = first_pinnacle
    
    ################## pandas things #######
    # RC
    krc = digit_sum((year_now - bty)) + digit_sum((year_now - bty)-1)
    rc = digit_sum(digit_sum(digit_sum((year_now - bty)) + digit_sum((year_now - bty)-1)))
    
    year = [i for i in range(bty, bty+55)]
    age = [i for i in range(0, 55)]
    fname = fillent(year, list(Lettered_name(str(name1))), age)[1] 
    mname = fillent(year, list(Lettered_name(str(name2))), age)[1]
    lname = fillent(year, list(Lettered_name(str(name3))), age)[1]
    
    numf_name = fillent(year, numInName((Lettered_name(str(name1)).strip('0'))), age)[1]
    numm_name = fillent(year, numInName((Lettered_name(str(name2)).strip('0'))), age)[1]
    numl_name = fillent(year, numInName((Lettered_name(str(name3)).strip('0'))), age)[1]
    
    df = pd.DataFrame({'year':year, 'age':age, 'fname':fname, 'mname':mname, 'lname':lname,
                  'numf_name':numf_name,'numm_name':numm_name,'numl_name':numl_name}, index=age)
    
    df['Karma'] = df['numf_name'] + df['numm_name'] + df['numl_name']
    df['Essence'] = df['Karma'].apply(digit_sum)
    df['Essence'] = df['Essence'].apply(digit_sum)
    
    y_num = []
    for i in df['year']:
        d = digit_sum(digit_sum(digit_sum(i)))
        y_num.append(digit_sum(d + for_py))
    
    df['y_num'] = y_num
    
    cur_y = []
    for i in df['year']:
        cur_y.append(digit_sum(digit_sum(digit_sum(i))))
        
    df['u_y_num'] = cur_y
    
    df['pinac'] = curr_pina
    
    df['outcome'] = df['Essence'] + df['y_num'] + df['u_y_num'] + df['pinac']
    df['Go'] = df['outcome'].apply(digit_sum)
    
    event = df.loc[year_now - bty]
    year = event['year']
    Essence = event['Essence']
    pynum = event['y_num']
    uniynum = event['u_y_num']
    pina = event['pinac']
    pmonth = p_month
    uniday = uni_day
    pday = p_day
    #print(event)
    #############
    #speed reading
    d = collections.Counter(s)# count number of,, just do print  Counter({2: 4, 1: 1, 9: 1, 8: 1})
    #print('d = ',d)
    p = list(d.keys())
    #print('p = ',p) #[2, 1, 9, 8]
    b = OrderedDict(sorted(d.items()))
    try:
        A = b[1]
    except(KeyError):
        A = 0
    try:
        B = b[2]
    except(KeyError):
        B = 0
    try:
        C = b[3]
    except(KeyError):
        C = 0
    try:
        D = b[4]
    except(KeyError):
        D = 0
    try:
        E = b[5]
    except(KeyError):
        E = 0
    try:
        F = b[6]
    except(KeyError):
        F = 0
    try:
        G = b[7]
    except(KeyError):
        G = 0
    try:
        H = b[8]
    except(KeyError):
        H = 0
    try:
        I = b[9]
    except:
        I = 0
    #All missing or all not missing p=[2, 1, 9, 8] ##page 62
    def power_lines(r,p,n):
        d = list(set(r).intersection(p))
        m = list(set(r).difference(d))
        if d == []:
            return f'r{n}_all_missing'
        elif d == r:
            return f'r{n}_all'
        else:
            return ''

#print(power_lines(r,p))
        
        
    r = [1, 2, 3]
    Rall = power_lines(r,p,0)
    
    r1 = [4, 5, 6]
    R1all = power_lines(r,p,1)
    
    r2 = [7, 8, 9]
    R2all = power_lines(r,p,2)
    
    r3 = [1, 4, 7]
    R3all = power_lines(r,p,3)
    
    r4 = [2, 5, 8]
    R4all = power_lines(r,p,4)
    
    r5 = [3, 6, 9]
    R5all = power_lines(r,p,5)
        
    r6 = [1, 5, 9]
    R6all = power_lines(r,p,6)
        
    r7 = [3, 5, 7]
    R7all = power_lines(r,p,7)
    
    # number of time a number occured
    def bashes(n,d):
        for k, v in d.items(): #Counter({2: 4, 1: 1, 9: 1, 8: 1})
            if k == n and v == d[n]:
                bash = (s_num[k][v]);
                return bash
            
    def remove_bashes_none(b):
        if b == None:
            return ''
        else:
            return b
        
        
    bash1 = remove_bashes_none(bashes(1,d))
    bash2 = remove_bashes_none(bashes(2,d))
    bash3 = remove_bashes_none(bashes(3,d))
    bash4 = remove_bashes_none(bashes(4,d))
    bash5 = remove_bashes_none(bashes(5,d))
    bash6 = remove_bashes_none(bashes(6,d))
    bash7 = remove_bashes_none(bashes(7,d))
    bash8 = remove_bashes_none(bashes(8,d))
    bash9 = remove_bashes_none(bashes(9,d))
        
        
    mini_reading = [exp,exp11, sU, sU1, iM, iM1,hP, ln, lp,bd1, lb, cH, cH1, cH2, cH3, LEB,
                    Mrity,cha,btd1,bd22,p1,p11,p2,p22,p3,p33,p4,p44,year_now,py_num,karma,karma1,karma2]
    
    speed_reading = [lp,A,B,C,D,E,F,G,H,I,Rall,R1all,R2all,R3all,R4all,R5all,R6all,R7all,p,bash1,bash2,bash3,bash4,bash5,
                    bash6,bash7,bash8,bash9]

    full_reading = [exp,exp11,ln,lp,year_now,sU,sU1]
    
    event = [exp11,sU,iM1,lp,Mrity,phy,men,emo,intt,one,two,thr,fou,fiv,six,sev,eig,nin,ps,cH,cH1,cH2,cH3,
             Essence,pynum,uniynum,pina,rc,pmonth,uniday,pday,Gpina,Gcha,Gper_pi,Gper_cha,k_day,k_pday,year_now]

    return mini_reading, speed_reading, full_reading, event
###########################
