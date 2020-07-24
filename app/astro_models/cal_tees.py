from tob import *
from describept import *
from webscrapping import *
from midptmodel import *
#from engine import *


def main_cal_tees(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon):
    number = before_month_call(98,month_to_num[btm-1],bty)
    ############### for me
    naspectname = [['sun'], ['moon'], ['merc'], ['ven'], ['mars'], ['jup'], ['sat'], ['ura'],
                   ['nep'], ['plu'], ['nod'], ['asc'], ['mc']]
                   
    naspect1 = naspect(btd, month(number, month_to_num[btm-1],bty),asc,mc)
    arc,progressed = solar_arc(btd, month(number, month_to_num[btm-1], bty),[13,9],[13,6], transit_year),[[0, 45], prog_moon, [0, 45], [0, 45], [0, 45]]
    transit = ephemeris_of_day(transit_day, month(98, month_to_num[transit_month-1], transit_year))
    
    def mid_pts(planet1,planet2,name_of_planet1,name_of_planet2):
        #print(planet1)
        sdeg = planet1[0]
        #print('mid sdeg', type(sdeg))
        sname = name_of_planet1[0]#name of midpt eg sun
        ssign = planet1[1]
        mdeg = planet2[0]
        mname = name_of_planet2[0]#name of midpt eg moon
        msign = planet2[1]
        sun_moon_midpt = mp_sign(int(round((sign_num(sdeg,ssign) + sign_num(mdeg,msign))/2,0)))
        #print(sun_moon_midpt)
        return sun_moon_midpt,sname,mname
    
    ##############
    def calculate_midpts():
        planet_midpt = []
        s = []
        symbol = []
        
        def mid_pts(planet1,planet2,name_of_planet1,name_of_planet2):
            sdeg = planet1[0]
            sname = name_of_planet1[0]#name of midpt eg sun
            ssign = planet1[1]
            mdeg = planet2[0]
            mname = name_of_planet2[0]#name of midpt eg moon
            msign = planet2[1]
            sun_moon_midpt = mp_sign(int(round((sign_num(sdeg,ssign) + sign_num(mdeg,msign))/2,0)))
            g = f'{sname}/{mname}'
            s1 = to_symbol(sname)
            s2 = to_symbol(mname)
            l = f'{s1}/{s2}'
            #print(sun_moon_midpt)
            planet_midpt.append(mp_sign(int(round((sign_num(sdeg,ssign) + sign_num(mdeg,msign))/2,0))))
            s.append(g)
            symbol.append(l)
            
        def call_midpts(w,w1,w2,w3): 
            n,n1,n2,n3 = w,w1,w2,w3
            while n3 != len(naspectname) and n1 != len(naspect1):
                mid_pts(naspect1[n],naspect1[n1],naspectname[n2],naspectname[n3])
                n1,n3 = n1 + 1,n3 + 1
                
        def increment(g):#1
            n = g
            n2 = n
            n1 = n + 1
            n3 = n1
            return n,n1,n2,n3
        
        def calculate():
            va = 0
            while va != len(naspect1):
                call_midpts(increment(va)[0], increment(va)[1], increment(va)[2], increment(va)[3])
                va = va + 1
        calculate()
        return planet_midpt,s,symbol
    
    ###########
    def in_transit_move_midpts(u,u1, transit, aspect,mname,symb,tipe):
        result =[]
        if u in transit:
            f = which_progressed_planet_aspecting(u,transit)[0] #plu
            f1 = which_progressed_planet_aspecting(u,transit)[1] #12
            what_now = f'{f}_{mname}' #plu_sun/moon
            k = (f'{tipe} {to_symbol(f)} {aspect_to_symbol(aspect)} {symb}')
            now = check_what_now(what_now)
            if what_now in describe:
                result.append(f'{k} {now} {whatsn(int(f1))[1]} {describe[what_now]}')
            else:
                result.append(f'{k} {now} {whatsn(int(f1))[1]}')
        elif u1 in transit:
            f = which_progressed_planet_aspecting(u1,transit)[0] #plu
            f1 = which_progressed_planet_aspecting(u1,transit)[1]
            what_now = f'{f}_{mname}' #plu_sum/moon
            k = (f'{tipe} {to_symbol(f)} {aspect_to_symbol(aspect)} {symb}')
            now = check_what_now(what_now)
            if what_now in describe:
                result.append(f'{k} {now} {whatsn(int(f1))[1]} {describe[what_now]}')
            else:
                result.append(f'{k} {now} {whatsn(int(f1))[1]}')
        if result == []:
            return ''
        else:
            return result
        #return result
    
    def in_transit_move(u, u1, transit, aspect,planet_position,tipe):
        result =[]
        if u in transit:
            #then which of them; planet aspect name and sigh
            f2 = which_progressed_planet_aspecting(u,transit)[0] #planet name 'sun'
            #print('f2 = ',f2)
            f3 = which_progressed_planet_aspecting(u,transit)[1] #planet sigh '12'
            #print('f3 = ',f3)
            which_natal = which_natal_planet_is_aspected(planet_position)
            #
            if tipe == 'Tr':
                ns = f'{f2}_to_{which_natal[0]}' #representation #sun_to_natven
                ns_sym = f'Tr {to_symbol(f2)} {aspect_to_symbol(aspect)} {to_symbol(which_natal[1])}' #♃_☉/☽
            elif tipe == 'arc':
                ns = f'{f2}_to_{which_natal[0]}' #representation #sun_to_natven
                ns_sym = f'{to_symbol(f2)}={to_symbol(which_natal[1])}' #♃=☉/☽
            elif tipe == 'Pr':
                ns = f'{f2}_to_{which_natal[0]}' #representation #sun_to_natven
                ns_sym = f'Pr {to_symbol(f2)} {aspect_to_symbol(aspect)} {to_symbol(which_natal[1])}' #♃_☉/☽
            
            #check if it is depresion or gain or loss
            now1 = check_what_now(ns)
            #convert the number of the sigh to sigh ari or aqu...whatsn(int(f3))
            ##print(f'{ns}:{aspect} {now1} {whatsn(int(f3))}')
            if ns in describe:
                ##print(describe[ns])
                ##print()
                result.append(f'{ns_sym} {whatsn(int(f3))[1]} {describe[ns]}')
            else:
                ##print('Not description yet!')
                ##print()
                result.append(f'{ns_sym} {whatsn(int(f3))[1]}')
    
        elif u1 in transit:
            #then which of them; planet aspect name and sigh
            f2 = which_progressed_planet_aspecting(u1,transit)[0] #planet name 'sun'
            print('u1 .. f2 = ',f2)
            f3 = which_progressed_planet_aspecting(u1,transit)[1] #planet sigh '12'
            print('u1 ... f3 = ',f3)
            which_natal = which_natal_planet_is_aspected(planet_position)
            #
            if tipe == 'Tr':
                ns = f'{f2}_to_{which_natal[0]}' #representation #sun_to_natven
                ns_sym = f'Tr {to_symbol(f2)} {aspect_to_symbol(aspect)} {to_symbol(which_natal[1])}' #♃_☉/☽
            elif tipe == 'arc':
                ns = f'{f2}_to_{which_natal[0]}' #representation #sun_to_natven
                ns_sym = f'{to_symbol(f2)}={to_symbol(which_natal[1])}' #♃=☉/☽
            elif tipe == 'Pr':
                ns = f'{f2}_to_{which_natal[0]}' #representation #sun_to_natven
                ns_sym = f'Pr {to_symbol(f2)} {aspect_to_symbol(aspect)} {to_symbol(which_natal[1])}' #♃_☉/☽
            
            #check if it is depresion or gain or loss
            now1 = check_what_now(ns)
            #convert the number of the sigh to sigh ari or aqu...whatsn(int(f3))
            ##print(f'{ns}:{aspect} {now1} {whatsn(int(f3))}')
            if ns in describe:
                ##print(describe[ns])
                ##print()
                result.append(f'{ns_sym} {whatsn(int(f3))[1]} {describe[ns]}')
            else:
                ##print('Not description yet!')
                ##print()
                result.append(f'{ns_sym} {whatsn(int(f3))[1]}')
        
        if result == []:
            return ''
        else:
            return result
            
            
    def rip_transit_movemont(conj):
        all_current_transit = []
        #all_current_tmpt = []
        def what_to_natal():
            current_transitn = []
            d = []
            planet_position = 0
            while planet_position != len(naspect1):
                #get first naspect
                first_naspect = naspect1[planet_position]
                #get planet degree
                sdeg = first_naspect[0]#25
                #get planet sigh
                ssign = first_naspect[1]#10
                #check for aspect
                conj(sdeg,ssign) #(3,12,0,conj)
                #where the aspect occur
                u = [conj(sdeg,ssign)[0],conj(sdeg,ssign)[1]]#3,12 = current_transit
                u1 = [conj(sdeg,ssign)[0],conj(sdeg,ssign)[2]]#3,0
                #what aspect conj or square or opp
                aspect = conj(sdeg,ssign)[3] #conj
                #get the aspecting planet and sigh
                current_transitn.append(in_transit_move(u,u1, transit, aspect,planet_position,'Tr'))
                planet_position = planet_position + 1
                
            for item in current_transitn:
                if item != '':
                    d.append(item)
                else:
                    pass
                    
            return d
        
        def what_to_midpts():
            current_transitm = []
            d = []
            
            midpts = calculate_midpts()[0]
            mid_names = calculate_midpts()[1]
            mid_symbol = calculate_midpts()[2]
            
            n=0
            while n != len(midpts):
                #get the midpt
                fisrt_mid = midpts[n] #(22,11)
                #get the symbol
                symb = mid_symbol[n] #sun/moon
                #get the name
                mname = mid_names[n] ##sun/moon
                #get planet degree
                mdeg = fisrt_mid[0]#22
                #get planet sigh
                msign = fisrt_mid[1]#11
                #get aspects
                conj(mdeg,msign) #(3,12,0,conj)
                #where the aspect will occur
                u = [conj(mdeg,msign)[0],conj(mdeg,msign)[1]]#3,12
                u1 = [conj(mdeg,msign)[0],conj(mdeg,msign)[2]]#3,0
                #what aspect conj or square or opp
                aspect = conj(mdeg,msign)[3] #conj
                #get the aspecting planet and sigh
                current_transitm.append(in_transit_move_midpts(u,u1, transit, aspect,mname,symb,'Tr'))
                
                n = n + 1
                
            for item in current_transitm:
                if item != '':
                    d.append(item)
                else:
                    pass
                    
            return d
            
        #print(what_to_midpts())
        all_current_transit.append(what_to_natal())
        all_current_transit.append(what_to_midpts())
        return all_current_transit
    
    
    def do_calculate_for_natal():
        to_natals = []
        to_natals_clean = []
        
        to_natals.append(rip_transit_movemont(conj))
        to_natals.append(rip_transit_movemont(sqareAct))
        to_natals.append(rip_transit_movemont(oppoAct))
        
        for item in to_natals:
            if item != '':
                to_natals_clean.append(item)
            else:
                pass
        return to_natals_clean
    
    return do_calculate_for_natal()