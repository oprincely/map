from __future__ import print_function, division
from .tob_new import oppoAct,sqareAct,conj,sextile,trine,sesquaAct,semiquaAct,to_symbol,aspect_to_symbol
from .webscrapping_extended_new import planet_points
from .grade_transit import rate_transit
from .mid_pts_new import mid_pts
from .describept import describe
from .arc_new import prog_date
from .progress_pts import calculate_prog_pts

month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')

def cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,prog_moon,asc,mc,transit_to,calculate_with,what_is_transit):
    aspects = [(conj,'conj'),(sqareAct,'square'),(oppoAct,'opp'),(sesquaAct,'sesqua'),(sextile,'setai'),
               (trine,'trin'),(semiquaAct,'semiqua')]
    
    #aspects = [(conj,'conj'),(sqareAct,'square'),(oppoAct,'opp')]#,(sesquaAct,'sesqua'),(semiquaAct,'semiqua')]
    
    if transit_to == 'mid_pts':
        #Get mid points
        transit_to = mid_pts(btd,btm,bty, asc, mc) #from mid_pts_new module
    else:
        #Get the natal points
        transit_to = planet_points(btd, btm-1, bty,asc,mc,'natal') #from webscrapping_extended_new module
        #print("transit_to = ",transit_to)
        
    #Get the transit points
    transit = planet_points(tday, tmonth-1, tyear,asc,mc,'transit')
    
    #Get the arc
    arc = prog_date(btd,btm,bty,Year,tday,tmonth,tyear,asc,mc)
        
    transit_filter = []
    transit_starts = []
    rating = []
    impotant_transit = []
    
    
    def perform_iteration():
        ########
        #Get values for natal points
        planet_deg = npoint[0]
        planet_sigh = npoint[1]
        planet_min = npoint[2]
        planet_name = npoint[3]
        
        
        # 1 degree in and out for transit => 3 = (3,4,5,6)
        exact_range = (planet_min,planet_min+1,planet_min+2,planet_min+3)
        
        if what_is_transit == 'transit':
            #Get values for transit points
            uradeg = a_point[0]
            urasigh = a_point[1]
            uramin = a_point[2]
            uraname = a_point[3]
            aspect_date = a_point[4]
        else:
            #Else use this
            uradeg = tpoint[0]
            urasigh = tpoint[1]
            uramin = tpoint[2]
            uraname = tpoint[3]
            aspect_date = tday
        
        #aspect like square returns sdeg,2,8,'square'
        for aspect,tipe in aspects:
            asp_deg = aspect(planet_deg,planet_sigh)[0]
            #print(f"{uraname} {tipe} {planet_name}")
            
            if calculate_with == 'natal':
                
                #upper sq
                if uradeg == asp_deg and uramin not in exact_range and urasigh == aspect(planet_deg,planet_sigh)[1]:
                    
                    if f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact' not in transit_filter:
                        transit_filter.append(f'{uraname} {aspect_to_symbol(tipe)} \
{planet_name} in deg but not exact')
                        transit_starts.append(f'{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}')
                        if rate_transit(uraname,tipe,planet_name) == 4:
                            impotant_transit.append(f"{to_symbol(uraname)} {aspect_to_symbol(tipe)} \
{to_symbol(planet_name)}: {describe[f'{uraname}_to_nat{planet_name}']} {aspect_date} {month_to_num[tmonth-1]} {tyear}")
                        
                #lower sq        
                elif uradeg == asp_deg and uramin not in exact_range and urasigh == aspect(planet_deg,planet_sigh)[2]:
                    if f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact' not in transit_filter:
                        transit_filter.append(f'{uraname} {aspect_to_symbol(tipe)} \
{planet_name} in deg but not exact')
                        transit_starts.append(f'{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}')
                        if rate_transit(uraname,tipe,planet_name) == 4:
                            impotant_transit.append(f"{to_symbol(uraname)} {aspect_to_symbol(tipe)} \
{to_symbol(planet_name)}: {describe[f'{uraname}_to_nat{planet_name}']} {aspect_date} {month_to_num[tmonth-1]} {tyear}")
                
            else:
                #upper sq
                if uradeg == asp_deg and uramin not in exact_range and urasigh == aspect(planet_deg,planet_sigh)[1]:
                    if f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact' not in transit_filter:
                        transit_filter.append(f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact')
                        transit_starts.append(f'{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}')
                        
                        if rate_transit(uraname,tipe,planet_name) == 4:
                            if f'{uraname}_{npoint[3]}/{npoint[4]}' in describe:
                                impotant_transit.append(f"{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(npoint[3])}/{to_symbol(npoint[4])}: {describe[f'{uraname}_{npoint[3]}/{npoint[4]}']} {aspect_date} {month_to_num[tmonth-1]} {tyear}")
                        
                #lower sq        
                elif uradeg == asp_deg and uramin not in exact_range and urasigh == aspect(planet_deg,planet_sigh)[2]:
                    if f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact' not in transit_filter:
                        transit_filter.append(f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact')
                        transit_starts.append(f'{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}')
                        
                        if rate_transit(uraname,tipe,planet_name) == 4:
                            if f'{uraname}_{planet_name}/{npoint[4]}' in describe:
                                impotant_transit.append(f"{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(npoint[3])}/{to_symbol(npoint[4])}: {describe[f'{uraname}_{planet_name}/{npoint[4]}']} {aspect_date} {month_to_num[tmonth-1]} {tyear}")
########
    
    if what_is_transit == 'transit':
        '''Transit points have some complex format'''
        for npoint in transit_to:
            for tpoint in transit:
                for a_point in tpoint:
                    perform_iteration()
    else:
        for npoint in transit_to:
            for tpoint in arc: #arc or progression_now
                ##########
                perform_iteration()
    
    #Lets see all aspect before filtering
    #print('transit_filter = ',transit_filter)
    
    return impotant_transit
    
'''cal_transit_planet(btd,btm,bty,tday,tmonth,tyear,transit_to,calculate_with,what_is_transit)'''
#cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,prog_moon,asc,mc,'natal','natal','arc')