#from __future__ import print_function, division
from .utils.tob import oppoAct,sqareAct,conj,sextile,trine,sesquaAct,semiquaAct,to_symbol,aspect_to_symbol
from .utils.Planet_position import planet_pos
from .utils.grade_transit import rate_transit
from .utils.mid_pts_new import mid_pts
from .utils.describept import describe
from .utils.Orb_range_prog_moon import orb_applying
from .utils.progress_pts import calculate_prog_pts

from .Solar_arc import solar_arc

month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')

def cal_prog_moon(btd,btm,bty,geo,birth_time,tday,tmonth,tyear,prog_moon,asc,mc,transit_to,calculate_with,what_is_transit):
    
    aspects = [(conj),(sqareAct),(oppoAct),(sesquaAct),(semiquaAct),(sextile),(trine)]
    
    if prog_moon == '':
        arc = calculate_prog_pts(btd,btm,bty,tday,tmonth,tyear)
        
    else:
        arc = [prog_moon]#[calculate_prog_pts(btd,btm,bty,tday,tmonth,tyear)]
    
    prog_sun = solar_arc(btd,btm,bty,tday,tmonth,tyear,geo, birth_time)[0]
          
    if what_is_transit == 'prog' and transit_to == 'natal':
        #Get the natal points
        transit_to = planet_pos(btd,btm,bty,geo, birth_time) + [asc,mc]
        
    elif what_is_transit == 'prog' and transit_to == 'mid_pts':
        '''Get mid points'''
        transit_to = mid_pts(btd,btm,bty,geo,birth_time,asc,mc) #from mid_pts_new module


    impotant_transit = []
    
    def perform_iteration():
        describe_index = ['started','40"','20"','12"','exact']
        
        '''Generate the prog moon point'''
        prog_moon_pt_1,prog_moon_pt_2 = arc
        
        for natpt in transit_to:
            for aspect in aspects:
                
                '''Generate the static(natal or midpoint) aspect point pass it to orb range'''
                upper_aspect_point,lower_aspect_point,tipe = aspect(natpt)
                
                '''range of aspect to the exact starting interval 15min=>'''
                upper_range_list = orb_applying(upper_aspect_point)           
        
                lower_range_list = orb_applying(lower_aspect_point)
        
        
                '''anything external (transit or arc or prog) to natal or midpts'''
                
                
                nat_to_symbol = f"{to_symbol(prog_moon_pt_1[3])} {aspect_to_symbol(tipe)} {to_symbol(natpt[3])}:"
                nat_describe = f"{describe.get(f'{prog_moon_pt_1[3]}_to_nat{natpt[3]}')}"
                nat_date = f"{tday} {month_to_num[tmonth-1]} {tyear}"
                
                if calculate_with == 'natal':
                    
                    #upper sq
                    if prog_moon_pt_1[0] == upper_range_list[0][4][0] and prog_moon_pt_1[2] == upper_range_list[0][4][2] \
                       or prog_moon_pt_2[0] == upper_range_list[1][4][0] and prog_moon_pt_2[2] == upper_range_list[1][4][2]:
                        
                        #if rate_transit(uraname,tipe,planet_name) == 4:
                        if f'{prog_moon_pt_1[3]}_to_nat{natpt[3]}' in describe:
                            impotant_transit.append(f"{nat_to_symbol} {nat_date} => {nat_describe}")
                    
                    
                else:
                    
                    midpt_to_symbol = f"{to_symbol(prog_moon_pt_1[3])} {aspect_to_symbol(tipe)} {to_symbol(natpt[3])}/{to_symbol(natpt[4])}:"
                    
                    if prog_moon_pt_1[0] == upper_range_list[0][4][0] and prog_moon_pt_1[2] == upper_range_list[0][4][2] \
                       or prog_moon_pt_2[0] == upper_range_list[1][4][0] and prog_moon_pt_2[2] == upper_range_list[1][4][2]:
                        
                        #if rate_transit(uraname,tipe,planet_name) == 4:
                        if f'{prog_moon_pt_1[3]}_{natpt[3]}/{natpt[4]}' in describe:
                            midpt_describe = f"{describe.get(f'{prog_moon_pt_1[3]}_{natpt[3]}/{natpt[4]}')}"
                            impotant_transit.append(f"{midpt_to_symbol} {nat_date} => {midpt_describe}")
                    
    perform_iteration()
    return impotant_transit

