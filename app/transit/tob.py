#!/usr/bin/python3
# -*- coding: utf-8 -*-

def whatsn(m):
    if m == 1:
        sn = "ari".upper()
        q2 = '♈'
    elif m == 2:
        sn = "tua".upper()
        q2 = '♉'
    elif m == 3:
        sn = "gem".upper()
        q2 = '♊'
    elif m == 4:
        sn = "can".upper()
        q2 = '♋'
    elif m == 5:
        sn = "leo".upper()
        q2 = '♌'
    elif m == 6:
        sn = "vir".upper()
        q2 = '♍'
    elif m == 7:
        sn = "lib".upper()
        q2 = '♎'
    elif m == 8:
        sn = "sco".upper()
        q2 = '♏'
    elif m == 9:
        sn = "sag".upper()
        q2 = '♐'
    elif m == 10:
        sn = "cap".upper()
        q2 = '♑'
    elif m == 11:
        sn = "aqu".upper()
        q2 = '♒'
    elif m == 12:
        sn = "pis".upper()
        q2 = '♓'
    return sn,q2


def which_progressed_planet_aspecting(j, r):#which_progressed_planet_aspecting(u,transit)
    if j == r[0]:
        q = 'sun'
        q1 = f'{r[0][1]}'#which is the ssigh
    elif j == r[1]:
        q = 'moon'# {}'.format(c)
        q1 = f'{r[1][1]}'
    elif j == r[2]:
        q = 'merc'# {}'.format(c)
        q1 = f'{r[2][1]}'
    elif j == r[3]:
        q = 'ven'# {}'.format(c)
        q1 = f'{r[3][1]}'
    elif j == r[4]:
        q = 'mars'# {}'.format(c)
        q1 = f'{r[4][1]}'
    elif j == r[5]:
        q = 'jup'# {}'.format(c)
        q1 = f'{r[5][1]}'
    elif j == r[6]:
        q = 'sat'# {}'.format(c)
        q1 = f'{r[6][1]}'
    elif j == r[7]:
        q = 'ura'# {}'.format(c)
        q1 = f'{r[7][1]}'
    elif j == r[8]:
        q = 'nep'# {}'.format(c)
        q1 = f'{r[8][1]}'
    elif j == r[9]:
        q = 'plu'# {}'.format(c)
        q1 = f'{r[9][1]}'
        #deg =r[9][0] and ssigh=r[9][1]        
    elif j == r[10]:
        q = 'nod'# {}'.format(c)
        q1 = f'{r[10][1]}'
    try:
        if j == r[11]:
            q = 'asc'# {}'.format(c)
            q1 = f'{r[11][1]}'
        elif j == r[12]:
            q = 'mc'# {}'.format(c)
            q1 = f'{r[12][1]}'
    except:
        pass
    return q,q1 #returns planet name and sigh


def which_natal_planet_is_aspected(z):
    if z == 0:
        re = 'natsun'
        re1 = 'sun'
    elif z == 1:
        re = 'natmoon'
        re1 = 'moon'
    elif z == 2:
        re = 'natmerc'
        re1 = 'merc'
    elif z == 3:
        re = 'natven'
        re1 = 'ven'
    elif z == 4:
        re = 'natmars'
        re1 = 'mars'
    elif z == 5:
        re = 'natjup'
        re1 = 'jup'
    elif z == 6:
        re = 'natsat'
        re1 = 'sat'
    elif z == 7:
        re = 'natura'
        re1 = 'ura'
    elif z == 8:
        re = 'natnep'
        re1 = 'nep'
    elif z == 9:
        re = 'natplu'
        re1 = 'plu'
    elif z == 10:
        re = 'natnod'
        re1 = 'nod'
    elif z == 11:
        re = 'natasc'
        re1 = 'asc'
    elif z == 12:
        re = 'natmc'
        re1 = 'mc'
    #elif z == 13:
        #re = 'sun/moon'
    return re,re1
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
def sesquaAct(sdeg,ssign):
    if sdeg <= 15:
        result = sdeg + 15
        k = ssign + 4
        if k <= 12:
            result2 = k
        else:
            result2 = k - 12
        result3 = ssign - 5
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
    d = ssign + 4#16...5
    k = abs(ssign - 4)#8...3
    if d >= 12:
        result = d - 12#4
    else:
        result = d#5
    if k <= 3:
        result2 = 12 - k
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
    if planet_name == 'sun':
        return '☉'
    elif planet_name == 'moon':
        return '☽'
    elif planet_name == 'merc':
        return '☿'
    elif planet_name == 'ven':
        return '♀'
    elif planet_name == 'mars':
        return '♂'
    elif planet_name == 'jup':
        return '♃'
    elif planet_name == 'sat':
        return '♄'
    elif planet_name == 'ura':
        return '♅'
    elif planet_name == 'nep':
        return '♆'
    elif planet_name == 'plu':
        return '♇'
    elif planet_name == 'nod':
        return '☊'
    elif planet_name == 'asc':
        return 'A'
    elif planet_name == 'mc':
        return 'M'
    
def aspect_to_symbol(aspect):
    if aspect == 'conj':
        return '☌'
    elif aspect == 'semiqua':
        return '∠'
    elif aspect == 'square':
        return '□'
    elif aspect == 'opp':
        return '☍'
    elif aspect == 'sesqua':
        return '⚼'
    elif aspect == 'setai':
        return '⚹'
    elif aspect == 'trin':
        return '△'
