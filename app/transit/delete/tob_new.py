#!/usr/bin/python3
# -*- coding: utf-8 -*-

##########################
def conj(sdeg,ssign):
    result = ssign
    return sdeg, result,0,'conj'#'☌'

def semiquaAct(sdeg,ssign):
    left_sign_side = ssign + 1
    right_sign_side = left_sign_side + 10
    sdeg_plus_15 = sdeg + 15
     
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
        
    return new_sdeg,new_left_sign,new_right_sign,'semiqua'
###############squa#Act####
def sqareAct(sdeg,ssign):#p(10,11)
    left_sign_side = ssign + 3
    right_sign_side = left_sign_side + 6
     
    if left_sign_side > 12:
        left_sign = left_sign_side - 12
    else:
        left_sign = left_sign_side
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
    
    return sdeg,left_sign,right_sign,'square'
############sesqua#act 135deg#########
def sesquaAct(sdeg,ssign): #(3, 12)
    left_sign_side = ssign + 4
    right_sign_side = left_sign_side + 4
    sdeg_plus_15 = sdeg + 15
     
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
        
    return new_sdeg,new_left_sign,new_right_sign,'sesqua'
    
def oppoAct(sdeg,ssign):#10, 8
    right_sign_side = ssign + 6
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
    
    return sdeg,right_sign,0,'opp'

def sextile(sdeg,ssign):#3, 12
    left_sign_side = ssign + 2
    right_sign_side = ssign + 8
     
    if left_sign_side > 12:
        left_sign = left_sign_side - 12
    else:
        left_sign = left_sign_side
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
    
    return sdeg,left_sign,right_sign,'setai'

def trine(sdeg,ssign):#3, 12...1
    left_sign_side = ssign + 4
    right_sign_side = ssign + 4
     
    if left_sign_side > 12:
        left_sign = left_sign_side - 12
    else:
        left_sign = left_sign_side
        
    if right_sign_side > 12:
        right_sign = right_sign_side - 12
    else:
        right_sign = right_sign_side
    
    return sdeg,left_sign,right_sign,'trin'

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
