planet_speed = {'asc':0,'mc':0,'sun':2,'moon':1,'merc':3,'ven':4,'mars':5,'jup':6,'sat':7,'ura':8,'nep':9,'plu':10,'nod':11,'vtx':12}
aspect_rating = {'sesqua':1,'semiqua':1,'setai':1,'square':2,'trin':2,'conj':3,'opp':3}

def rate_transit(t_planet_name,t_aspect,natal_point_name):
    
    transit_planet,aspect,natal_point = planet_speed[t_planet_name],aspect_rating[t_aspect],planet_speed[natal_point_name]
    if natal_point > transit_planet and aspect == 3:
        rating = 1
    elif natal_point == 0 and natal_point < transit_planet and aspect == 1: #7 < 0 and 1 == 1
        rating = 2
    elif natal_point < transit_planet and aspect == 1: #5 < 9 and 1 == 1 or 2
        rating = 3
    elif natal_point < transit_planet and aspect in [2,3]: #5 < 9 and 1 == 1 or 2
        rating = 4
        return rating
    return 'NA'
