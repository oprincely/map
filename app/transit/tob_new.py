#!/usr/bin/python3
# -*- coding: utf-8 -*-

##########################
def conj(sdeg,ssign):
    result = ssign
    return sdeg, result,0,'conj'#'☌'

def semiquaAct(sdeg,ssign):
    if sdeg <= 15:
        result = sdeg + 15
        k = ssign + 1
        if k <= 12:
            result2 = k
        else:
            result2 = k - 12
        result3 = ssign - 2
    elif sdeg >= 16:
        h = sdeg + 15
        result = h - 30
        k = ssign + 2
        if k <= 12:
            result2 = k
        else:
            result2 = k - 12
        result3 = ssign - 1
    return result,result2,result3,'semiqua'#'∠'
###############squa#Act####
def sqareAct(sdeg,ssign):#p(10,11)
    if ssign <= 9:
        result2 = ssign + 3
        result3 = result2 - 6
    elif ssign >= 9:
        j = ssign + 3#14
        result2 = j - 12#2
        result3 = result2 + 6#8
    return sdeg,result2,result3,'square'#'□'  10,2,8,square
############sesqua#act 135deg#########
def sesquaAct(sdeg,ssign): #(3, 12)
    if sdeg <= 15:
        result = sdeg + 15 #3+15=18
        k = ssign + 4 #12+4=16
        if k <= 12:
            result2 = k
        else:
            result2 = k - 12 #16-12=4
        result3 = ssign - 5 #12-5=7
    elif sdeg >= 16:
        h = sdeg + 15
        result = h - 30
        k = ssign + 5
        if k <= 12:
            result2 = k
        else:
            result2 = k - 12
        result3 = ssign - 4
    return result,result2,result3,'sesqua'#'⚼'
    
def oppoAct(sdeg,ssign):#10, 8
    if ssign <=6:
        result = ssign + 6
    elif ssign >= 7:
        result = ssign - 6
    return sdeg,result,0,'opp'#'☍'

def sextile(sdeg,ssign):#3, 12
    d = ssign + 2#14...5
    k = abs(ssign - 2)#10...3
    if d >= 12:
        result = d - 12#2
    else:
        result = d#5
    if k <= 3:
        result2 = 12 - k
    else:
        result2 = k#10...9
    return sdeg,result,result2,'setai'#,'⚹'

def trine(sdeg,ssign):#3, 12...1
    d = ssign + 4#16...5 first sigh
    k = abs(ssign - 4)#8...3 other sigh
    if d >= 12:
        result = d - 12#4
    else:
        result = d#5
    if k >= 12:
        result2 = k - 12
    else:
        result2 = k#8...9
    return sdeg,result,result2,'trin'#'△'

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
