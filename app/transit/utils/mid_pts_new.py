from .midptmodel_new import sign_num,mp_sign
from .Planet_position import planet_pos

def mid_pts(btd, btm, bty,geo,birth_time, asc, mc):
    '''save the mid points in list'''
    midpts = []
    
    '''Get the natal points [(3, 3, 12, 'sun'), (11, 3, 11, 'moon')] + [asc,mc]'''
    nat_points = planet_pos(btd,btm,bty,geo, birth_time) + [asc,mc]
    #print('nat_points = ',nat_points)
    #[(3, 3, 12, 'sun'), (11, 3, 11, 'moon'), (6, 40, 11, 'merc'), (25, 41, 10, 'ven'),
    #(19, 10, 7, 'mars'), (10, 19, 8, 'jup'), (21, 50, 7, 'sat'), (4, 30, 9, 'ura'),
    #(26, 41, 9, 'nep'), (26, 46, 7, 'plu'), (21, 56, 4, 'nod')]
    
    '''the first while loop iterates over all the mid points'''
    start_num = 0
    while start_num != len(nat_points):
        first_ele = start_num
        
        #Get first point and keep it constant
        sdeg = nat_points[first_ele][0]
        smin = nat_points[first_ele][1]
        ssign = nat_points[first_ele][2]
        sname = nat_points[first_ele][3]
        
        '''the second while loop iterates over the second point in the natal points'''
        second_ele = first_ele + 1
        while second_ele != len(nat_points):
            #Get the second point
            mdeg = nat_points[second_ele][0]
            mmin = nat_points[second_ele][1]
            msign = nat_points[second_ele][2]
            mname = nat_points[second_ele][3]
            #print(mname)
            
            '''we want to pass this: sign_num(3,12) + sign_num(10,11))/2, but it has decimal then float so int and round is introduced.
                mp_sign, takes 4 arg
            '''
            #print('from mid point = ',int(round((sign_num(sdeg,ssign) + sign_num(mdeg,msign))/2,0)))
            two_planet_midpt = mp_sign(
                                        int(round((sign_num(sdeg,ssign) + sign_num(mdeg,msign))/2,0)),
                                       int(round((smin + mmin)/2,0)),
                                       f'{sname}',f'{mname}'
                                        )
            #print('two_planet_midpt = ',two_planet_midpt)
            midpts.append(two_planet_midpt)
            
            second_ele += 1
            
        start_num += 1
    
    return midpts

#print(mid_pts(22, 2, 1982,'07E','01:35',(16,18,9,'asc'),(16,48,6,'mc')))

