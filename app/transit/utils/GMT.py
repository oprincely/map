from .convert_time import time_to_int,int_to_time,get_hour_or_min

#geo = '95W'
#geo = '88W'
#geo = '07E' #princely


#birth_time = '00:24' #princely
#birth_time = '14:00' #use 24H time#+8sec   2:15 A.M., 8:15 A.M., 2:15 P.M., and 8:15 P.M.

def gmt(geo,birth_time):
    birth_time_secs = time_to_int(int(birth_time[0:2]),int(birth_time[3:5]),0)
    birth_time_hour = get_hour_or_min(birth_time_secs)[0]
    
    get_geo = int(geo[0:2])
    
    corr_of_4 = (4 * get_geo) * 60

    if geo[2] == 'W':
        gmt_total = birth_time_secs + corr_of_4
    elif geo[2] == 'E':
        if birth_time_secs < corr_of_4:
            gmt_total = corr_of_4 - birth_time_secs
        else:
            gmt_total = birth_time_secs - corr_of_4 #1440 - 1680
            
    minus_24h = time_to_int(24,0,0)

    def is_am_pm(gmt_total):
        if gmt_total > minus_24h:
            return (gmt_total - time_to_int(24,0,0)),'am'
        else:
            return gmt_total, 'pm'
            
    gmtt = is_am_pm(gmt_total)[0]
    am_pm = is_am_pm(gmt_total)[1]
    if gmtt > time_to_int(12,0,0):
        gmt = gmtt - time_to_int(12,0,0)
    else:
        gmt = gmtt
    #print('g_m_t = ',int_to_time(gmt),am_pm)
    
    return gmt,am_pm
    
#print(gmt(geo='07E',birth_time='01:35'))
#gmt(geo='95W',birth_time='02:00')