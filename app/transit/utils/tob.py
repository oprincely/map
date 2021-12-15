#!/usr/bin/python3
# -*- coding: utf-8 -*-

##########################
def conj(point): #(3,3,12,'sun')
    result = point[2]
    pt_1 = point[0],point[1],result,point[3]
    pt_2 = point[0],point[1],0,point[3]
    return pt_1,pt_2,'conj'

def semiquaAct(point):
    left_sign_side = point[2] + 1
    right_sign_side = left_sign_side + 10
    sdeg_plus_15 = point[0] + 15
     
    if left_sign_side > 12:
        left_sign = left_sign_side - 12
    else:
        left_sign = left_sign_side
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
        
    if sdeg_plus_15 > 29:
        new_left_sign = left_sign + 1
        new_right_sign = right_sign + 1
        new_sdeg = sdeg_plus_15 - 29
    else:
        new_left_sign = left_sign
        new_right_sign = right_sign
        new_sdeg = sdeg_plus_15
        
    pt_1 = new_sdeg,point[1],new_left_sign,point[3]
    pt_2 = new_sdeg,point[1],new_right_sign,point[3]
        
    return pt_1,pt_2,'semiqua'
###############squa#Act####
def sqareAct(point):#p(10,11)
    left_sign_side = point[2] + 3
    right_sign_side = left_sign_side + 6
     
    if left_sign_side > 12:
        left_sign = left_sign_side - 12
    else:
        left_sign = left_sign_side
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side

    pt_1 = point[0],point[1],left_sign,point[3]
    pt_2 = point[0],point[1],right_sign,point[3]
        
    return pt_1,pt_2,'square'
############sesqua#act 135deg#########
def sesquaAct(point): #(3, 12)
    left_sign_side = point[2] + 4
    right_sign_side = left_sign_side + 4
    sdeg_plus_15 = point[0] + 15
     
    if left_sign_side > 12:
        left_sign = left_sign_side - 12
    else:
        left_sign = left_sign_side
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
        
    if sdeg_plus_15 > 29:
        new_left_sign = left_sign + 1
        new_right_sign = right_sign + 1
        new_sdeg = sdeg_plus_15 - 29
    else:
        new_left_sign = left_sign
        new_right_sign = right_sign
        new_sdeg = sdeg_plus_15

    pt_1 = new_sdeg,point[1],new_left_sign,point[3]
    pt_2 = new_sdeg,point[1],new_right_sign,point[3]
        
    return pt_1,pt_2,'sesqua'
    
def oppoAct(point):#10, 8
    right_sign_side = point[2] + 6
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
    
    pt_1 = point[0],point[1],right_sign,point[3]
    pt_2 = point[0],point[1],0,point[3]
        
    return pt_1,pt_2,'opp'

def sextile(point):#3, 12
    left_sign_side = point[2] + 2
    right_sign_side = point[2] + 8
     
    if left_sign_side > 12:
        left_sign = left_sign_side - 12
    else:
        left_sign = left_sign_side
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
    
    pt_1 = point[0],point[1],left_sign,point[3]
    pt_2 = point[0],point[1],right_sign,point[3]
        
    return pt_1,pt_2,'setai'

def trine(point):#3, 12...1
    left_sign_side = point[2] + 4
    right_sign_side = point[2] + 4
     
    if left_sign_side > 12:
        left_sign = left_sign_side - 12
    else:
        left_sign = left_sign_side
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
    
    #return sdeg,left_sign,right_sign,'trin'

    pt_1 = point[0],point[1],left_sign,point[3]
    pt_2 = point[0],point[1],right_sign,point[3]
        
    return pt_1,pt_2,'trin'

depression = ['nep_merc/sat', 'sat_nep/plu','plu_sat/asc','asc_sat/plu','merc_to_natsat','sat_to_natmerc']
romance = ['ven_to_natsun', 'sun_to_natven', 'ven_sun/moon', 'moon_to_natven','jup_sun/ven', 'ven_sun/jup',
           'ven_moon/jup','ven_jup/nep', 'ven_jup/mc','ura_to_natven', 'ven_sun/ura', 'nod_sun/ura, sun_ven/ura',
           'mars_ven/ura','ven_to_natnep', 'ven_sun/nep', 'nep_sun/ven','mars_to_ven', 'ven_to_natmars', 'mc_ven/mars',
           'ven_moon/mars', 'mars_ven/nod']
gain = ['jup_to_natplu','plu_to_natjup','sun_jup/plu','moon_jup/plu','merc_jup/plu','ven_jup/plu','mars_jup/plu','sat_jup/plu',
        'ura_jup/plu','nep_jup/plu','nod_jup/plu','asc_jup/plu','mc_jup/plu']
loss = ['sat_to_natplu','plu_to_natsat','sun_sat/plu','moon_sat/plu','merc_sat/plu','ven_sat/plu','mars_sat/plu','jup_sat/plu',
        'ura_sat/plu','nep_sat/plu','nod_sat/plu','asc_sat/plu','mc_sat/plu']
enengy_and_drive = ['moon_sun/mars','merc_sun/mars']
oppurtunity_and_strategy = ['jup_to_natsat','sat_to_natjup','sun_jup/sat','moon_jup/sat','merc_jup/sat','ven_jup/sat',
                            'mars_jup/sat','ura_jup/sat','nep_jup/sat','plu_jup/sat','nod_jup/sat','asc_jup/sat','mc_jup/sat']


def check_what_now(what_now):
    if what_now in depression:
        return 'depression'
    elif what_now in romance:
        return 'romance'
    elif what_now in gain:
        return 'gain'
    elif what_now in loss:
        return 'loss'
    elif what_now in oppurtunity_and_strategy:
        return 'oppurtunity/strategy'
    else:
        return ''
        
        
def to_symbol(planet_name):
    to_sym_dict = {'sun':'☉','moon':'☽','merc':'☿','ven':'♀','mars':'♂','jup':'♃','sat':'♄','ura':'♅','nep':'♆',
                   'plu':'♇','nod':'☊','asc':'A','mc':'M','vtx':'V','dc':'Dc','sun/moon':'☉/☽'}
    return to_sym_dict[planet_name]
    
def aspect_to_symbol(aspect):
    aspect_dict = {'conj':'☌','semiqua':'∠','square':'□','opp':'☍','sesqua':'⚼','setai':'⚹','trin':'△'}
    return aspect_dict[aspect]

