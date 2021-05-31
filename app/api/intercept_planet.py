import csv
from app.transit.webscrapping_extended_new import convert_to_csv
from datetime import date

#btd = 22
#btm = 2
#bty = 1982

def intercept_planet_starts(day,month,yr,planet_deg,planet_position):
    #natal = planet_points(day,month-1,yr,'natal')
    def plt_pos(position):
        #planet name
        name = ('sun','moon','merc','ven','mars','jup','sat','ura','nep','plu','nod','asc','mc')
        sdeg = int(row[position][0:2])
        ssigh = row[position][2:4]
        smin = int(row[position][4:6])
        return sdeg,ssigh,smin,name[position - 3]
    
    month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')
    try:
        #Open csv
        with open(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.csv') as f:
            csv_f = csv.reader(f)
            for row in csv_f:
                #Get the natal points and note f'{str(day).zfill(2)}' = 22 = btd
                if row != [] and plt_pos(planet_position)[0] == planet_deg: #to convert 1 to 01 str(1).zfill(2)
                    non_intercept_date = int(row[1][0:2])
    except:
        convert_to_csv(month, yr)
        #Open csv
        with open(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.csv') as f:
            csv_f = csv.reader(f)
            for row in csv_f:
                #Get the natal points and note f'{str(day).zfill(2)}' = 22 = btd
                if row != [] and plt_pos(planet_position)[0] == 1: #to convert 1 to 01 str(1).zfill(2)
                    non_intercept_date = int(row[1][0:2])
                
    birth_date = date(yr, month, day)
    non_intercept_date_starts = date(yr, month+1, non_intercept_date)
    delta = non_intercept_date_starts - birth_date
    advise = f'Your relationships and money related issues will be fine starting at the age of {delta.days}, \
that is from {delta.days + yr}'
                
    return {'age':delta.days,'year':delta.days + yr}

#print(intercept_planet_starts(22,2,1982,3,8))
