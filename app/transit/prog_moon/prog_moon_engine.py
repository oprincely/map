from __future__ import print_function, division
from ..utils.tob_new import oppoAct,sqareAct,conj,sextile,trine,sesquaAct,semiquaAct,to_symbol,aspect_to_symbol
from ..utils.Planet_position import planet_pos
from ..utils.grade_transit import rate_transit
from ..utils.mid_pts_new import mid_pts
from ..utils.describept import describe
from ..utils.Orb_range_prog_moon import orb_applying


month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')

def cal_prog_moon(btd,btm,bty,geo,birth_time,tday,tmonth,tyear,prog_moon,asc,mc,transit_to,calculate_with,what_is_transit):
    
    aspects = [(conj,'conj'),(sqareAct,'square'),(oppoAct,'opp'),(sesquaAct,'sesqua'),(semiquaAct,'semiqua')]

      
    if what_is_transit == 'prog' and transit_to == 'natal':
        #Get the natal points
        transit_to = planet_pos(btd,btm,bty,geo, birth_time)
        
        #Get you progressed moon = arc b/c of our iteration down
        arc = [prog_moon]#[calculate_prog_pts(btd,btm,bty,tday,tmonth,tyear)]
    
    elif what_is_transit == 'prog' and transit_to == 'mid_pts':
        '''Get mid points'''
        transit_to = mid_pts(btd,btm,bty,geo,birth_time,asc,mc) #from mid_pts_new module

        #Get you progressed moon = arc b/c of our iteration down
        arc = [prog_moon]#[calculate_prog_pts(btd,btm,bty,tday,tmonth,tyear)]
        #print('prog_moon = ',arc)


    impotant_transit = []
    
    def perform_iteration():
        '''Get the natal points'''
        planet_deg = npoint[0]
        planet_min = npoint[1]
        planet_sign = npoint[2]
        planet_name = npoint[3]
        
        
        '''we use this for arc or progressed'''
        uradeg = tpoint[0]
        uramin = tpoint[1]
        urasign = tpoint[2]
        uraname = tpoint[3]
        aspect_date = tday
        
        describe_index = ['started','40"','20"','12"','exact']
        #describe_index = ['exact']
        
        
        for aspect,tipe in aspects:
            
            '''Generate the static(natal or midpoint) aspect point pass it to orb range'''
            upper_aspect_point = (aspect(planet_deg,planet_sign)[0],planet_min,aspect(planet_deg,planet_sign)[1])
            lower_aspect_point = (aspect(planet_deg,planet_sign)[0],planet_min,aspect(planet_deg,planet_sign)[2])
            
            
            '''range of aspect to the exact starting interval 15min=>'''
            upper_range_list = orb_applying(upper_aspect_point)           
            
            lower_range_list = orb_applying(lower_aspect_point)
                          
            
            '''Generate the transit point'''
            transit_point = (uradeg,uramin,urasign)
            
            
            '''anything external (transit or arc or prog) to natal or midpts'''
            
            
            if calculate_with == 'natal':
                
                nat_to_symbol = f"{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}:"
                nat_describe = f"{describe.get(f'{uraname}_to_nat{planet_name}')}"
                nat_date = f"{aspect_date} {month_to_num[tmonth-1]} {tyear}"
                
                
                #upper sq
                if transit_point in upper_range_list[0]:
                    
                    #if rate_transit(uraname,tipe,planet_name) == 4:
                    if f'{uraname}_to_nat{planet_name}' in describe:
                        impotant_transit.append(f"{nat_to_symbol} {nat_describe} {nat_date}")
                        
                #lower sq        
                elif transit_point in lower_range_list[0]:
                    
                    #if rate_transit(uraname,tipe,planet_name) == 4:
                    if f'{uraname}_to_nat{planet_name}' in describe:
                        impotant_transit.append(f"{nat_to_symbol} {nat_describe} {nat_date}")
           
            else:
                '''It means we want that of mid points'''
                
                midpt_to_symbol = f"{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(npoint[3])}/{to_symbol(npoint[4])}:"
                
                midpt_date = f"{aspect_date} {month_to_num[tmonth-1]} {tyear}"
                
                #upper sq
                if transit_point in upper_range_list:
                    
                    midpt_zone_upper = describe_index[upper_range_list.index(transit_point)]
                    
                    #if rate_transit(uraname,tipe,planet_name) == 4:
                    if f'{uraname}_{npoint[3]}/{npoint[4]}' in describe:
                        midpt_describe = f"{describe.get(f'{uraname}_{npoint[3]}/{npoint[4]}')}"
                        impotant_transit.append(f"{midpt_to_symbol} {midpt_describe} {midpt_date} {midpt_zone_upper}")
                #lower sq        
                elif transit_point in lower_range_list:
                    midpt_zone_lower = describe_index[lower_range_list.index(transit_point)]
                    
                    #if rate_transit(uraname,tipe,planet_name) == 4:
                    if f'{uraname}_{planet_name}/{npoint[4]}' in describe:
                        midpt_describe = f"{describe[f'{uraname}_{npoint[3]}/{npoint[4]}']}"
                        impotant_transit.append(f"{midpt_to_symbol} {midpt_describe} {midpt_date} {midpt_zone_lower}")

    
    for npoint in transit_to: #
        for tpoint in arc: #arc or progression moon
            perform_iteration()
    
    
    return impotant_transit
