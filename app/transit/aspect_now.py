from __future__ import print_function, division
import datetime
from .webscrapping_extended import planet_points,planet_pos,month_year
from .tob import oppoAct,sqareAct,conj,sesquaAct,semiquaAct,to_symbol,aspect_to_symbol
from .mid_pts import MidPts
from .arc import Arc
#from .progress_pts import prog_planets
from .describept import describe

#btd = 22
#btm = 2
#bty = 1982
#Year = ''#2019

#tday = 9
#tmonth = 10
#tyear = 2020
def cal_aspects_now(btd,btm,bty,tday,tmonth,tyear,Year):
    transit_name = (('mars'), ('jup'), ('sat'), ('ura'),('nep'), ('plu'), ('nod'))
    transit = planet_points(tday, month_year(tmonth-1, tyear),'transit')

    nat_pts = planet_points(btd, month_year(btm-1, bty),'natal')
    #print('nat_pts = ',nat_pts)
    nat_name = (('sun'), ('moon'), ('merc'), ('ven'), ('mars'), ('jup'), ('sat'), ('ura'),
                   ('nep'), ('plu'), ('nod'), ('asc'), ('mc'),('vetx'))

    obj = MidPts()
    midpts = obj.calculate_midpts()[0]
    midpts_name = obj.calculate_midpts()[1]
    midpts_symb = obj.calculate_midpts()[2]

    an_arc = Arc()
    arc_list = an_arc.prog_date(nat_pts,btd,btm,bty,Year,tday,tmonth,tyear)
    arc_name = nat_name

    #pr_planets = [(11, 1, 40), (18, 4, 38), (1, 1, 38), (25, 11, 14), (9, 7, 51), (8, 8, 20),
    #              (19, 7, 29), (4, 9, 24), (27, 9, 3), (25, 7, 56), (18, 4, 22), (18, 10, 58), (24, 7, 35)]
    #pr_planets = prog_planets()
    #print('pr_planets = ',pr_planets)
    #pr_plnt_name = (('prsun'), ('prmoon'), ('prmerc'), ('prven'), ('prmars'), ('prjup'), ('prsat'), ('prura'),
    #               ('prnep'), ('prplu'), ('prnod'), ('prasc'), ('prmc'))

    #pr_moon = [prog_planets()[1]]
    #pr_name = [('prmoon')]
    
    transit_arc = []
    
    #checking aspects
    def aspects_now(nat_pts, arc, nat_name, arc_name,aspect,tipe,call):
        
        n = 0
        while n != len(nat_pts):
            #run code
            planet = nat_pts[n] #(26, 1, 4)
            planet_name = nat_name[n] #mars
            planet_deg = planet[0]
            planet_sigh = planet[1]
            #planet_min = planet[2]
            
            d = 0
            while d != len(arc):
                #run another code
                arc_1 = arc[d]
                arc_name_1 = arc_name[d]#mars
                arc_deg = arc_1[0]
                arc_sigh = arc_1[1]
                #arc_min = arc_1[2]
                
                asp_deg = aspect(planet_deg,planet_sigh)[0]
                
                if call == 'midpts':
                    if arc_deg == asp_deg and arc_sigh == aspect(planet_deg,planet_sigh)[1]:
                        ns =  f'{arc_name_1}_{planet_name}' #jup_moon/plu
                        #print(ns)
                        #print(midpts_symb[n])
                        if ns in describe:
                            transit_arc.append((f'{to_symbol(arc_name_1)} {aspect_to_symbol(tipe)} {midpts_symb[n]}',f'{describe[ns]}'))
                        else:
                            transit_arc.append(f'{to_symbol(arc_name_1)} {aspect_to_symbol(tipe)} {midpts_symb[n]}')
                            
                    elif arc_deg == asp_deg and arc_sigh == aspect(planet_deg,planet_sigh)[2]:
                        ns =  f'{arc_name_1}_{planet_name}'
                        #print(ns)
                        #print(midpts_symb[n])
                        if ns in describe:
                            transit_arc.append((f'{to_symbol(arc_name_1)} {aspect_to_symbol(tipe)} {midpts_symb[n]}',f'{describe[ns]}'))
                        else:
                            transit_arc.append(f'{to_symbol(arc_name_1)} {aspect_to_symbol(tipe)} {midpts_symb[n]}')
                else:
                    if arc_deg == asp_deg and arc_sigh == aspect(planet_deg,planet_sigh)[1]:
                        ns =  f'{arc_name_1}_to_nat{planet_name}'
                        if ns in describe:
                            transit_arc.append((f'{to_symbol(arc_name_1)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}',f'{describe[ns]}'))
                        else:
                            transit_arc.append(f'{to_symbol(arc_name_1)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}')
                            
                    elif arc_deg == asp_deg and arc_sigh == aspect(planet_deg,planet_sigh)[2]:
                        ns =  f'{arc_name_1}_to_nat{planet_name}'
                        if ns in describe:
                            transit_arc.append((f'{to_symbol(arc_name_1)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}',f'{describe[ns]}'))
                        else:
                            transit_arc.append(f'{to_symbol(arc_name_1)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}')
                
                d += 1
            n += 1
        
    #print(transit_arc)
    #return transit_arc

#aspects_now(nat_pts,arc)#prog_planets()) ,sqareAct,conj,sesquaAct,semiquaAct

    aspects_now(nat_pts,arc_list,nat_name, arc_name,conj,'conj','natpts')
    aspects_now(nat_pts,arc_list,nat_name, arc_name,semiquaAct,'semiqua','natpts')
    aspects_now(nat_pts,arc_list,nat_name, arc_name,sqareAct,'square','natpts')
    aspects_now(nat_pts,arc_list,nat_name, arc_name,sesquaAct,'sesqua','natpts')
    aspects_now(nat_pts,arc_list,nat_name, arc_name,oppoAct,'opp','natpts')

    aspects_now(midpts,arc_list,midpts_name, arc_name,conj,'conj','midpts')
    aspects_now(midpts,arc_list,midpts_name, arc_name,semiquaAct,'semiqua','midpts')
    aspects_now(midpts,arc_list,midpts_name, arc_name,sqareAct,'square','midpts')
    aspects_now(midpts,arc_list,midpts_name, arc_name,sesquaAct,'sesqua','midpts')
    aspects_now(midpts,arc_list,midpts_name, arc_name,oppoAct,'opp','midpts')
    
    return transit_arc

#k = cal_aspects_now()
