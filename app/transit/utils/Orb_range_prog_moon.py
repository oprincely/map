from .convert_time import time_to_sec,int_to_time,get_hour_or_min

def orb_applying(point): #(25,10,41)
    
    p_orbs = []
    n_orbs = []
    
    orbs_p = ((
            get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 2, 0))[0],
            get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 2, 0))[1],
            point[2]
            ),
            (
            get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 4, 0))[0],
            get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 4, 0))[1],
            point[2]),
            (get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 6, 0))[0],
            get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 6, 0))[1],
            point[2]),
            (get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 8, 0))[0],
            get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 8, 0))[1],
            point[2]),
            (get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 0, 0))[0],
            get_hour_or_min(time_to_sec(point[0], point[1], 0) + time_to_sec(0, 0, 0))[1],
            point[2])
        )
    
    orbs_n = (
        (get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 2, 0))[0],
        get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 2, 0))[1],
        point[2]),
        (get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 4, 0))[0],
        get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 4, 0))[1],
        point[2]),
        (get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 6, 0))[0],
        get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 6, 0))[1],
        point[2]),
        (get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 8, 0))[0],
        get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 8, 0))[1],
        point[2]),
        (get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 0, 0))[0],
        get_hour_or_min(time_to_sec(point[0], point[1], 0) - time_to_sec(0, 0, 0))[1],
        point[2])
        )
    #print('orbs = ',int_to_time(orbs))
    n_orbs.append(orbs_n)
    p_orbs.append(orbs_p)
        
    return n_orbs[0],p_orbs[0]

#print((orb_applying((21, 56, 4, 'nod'))))

#print(aspect_list)


