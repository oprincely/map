from .midptmodel_new import sign_num,mp_sign
from .webscrapping_extended_new import planet_points

def mid_pts(btd, btm, bty, asc, mc):
    '''save the mid points in list'''
    midpts = []
    
    '''Get the natal points'''
    nat_points = planet_points(btd, btm-1, bty, asc, mc,'natal')
    
    '''the first while loop iterates over all the mid points'''
    start_num = 0
    while start_num != len(nat_points):
        first_ele = start_num
        
        #Get first point and keep it constant
        sdeg = nat_points[first_ele][0]
        ssign = nat_points[first_ele][1]
        smin = nat_points[first_ele][2]
        sname = nat_points[first_ele][3]
        
        '''the second while loop iterates over the second point in the natal points'''
        second_ele = first_ele + 1
        while second_ele != len(nat_points):
            #Get the second point
            mdeg = nat_points[second_ele][0]
            msign = nat_points[second_ele][1]
            mmin = nat_points[second_ele][2]
            mname = nat_points[second_ele][3]
            #print(mname)
            
            '''we want to pass this: sign_num(3,12) + sign_num(10,11))/2, but it has decimal then float so int and round is introduced.
                mp_sign, takes 4 arg
            '''

            two_planet_midpt = mp_sign(int(round((sign_num(sdeg,ssign) + sign_num(mdeg,msign))/2,0)),
                                   int(round((smin + mmin)/2,0)),
                                   f'{sname}',f'{mname}')
            
            midpts.append(two_planet_midpt)
            
            second_ele += 1
            
        start_num += 1
    
    return midpts

#print(mid_pts(22, 2, 1982))

