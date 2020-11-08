class Num_of_days(object):
    def numberOfDays(self, y, m):
        leap = 0
        if y % 400 == 0:
            leap = 1
        elif y % 100 == 0:
            leap = 0
        elif y % 4 == 0:
            leap = 1
        if m == 1:
            return 28 + leap
        list_ = [0,2,4,6,7,9,11]
        if m in list_:
            return 31
        return 30

#obj = Num_of_days()
#print(obj.numberOfDays(2020, 1))


'''
#('jan31 =0','feb29=1','mar31=2','apr30=3','may31=4','june30=5','july31=6','aug31=7','sept30=8','oct31=9','nov30=10','dec31')
class Num_of_days(object):
    def numberOfDays(self, y, m):
        leap = 0
        if y % 400 == 0:
            leap = 1
        elif y % 100 == 0:
            leap = 0
        elif y % 4 == 0:
            leap = 1
        if m == 2:
            return 28 + leap
        list_ = [1,3,5,7,8,10,12]
        if m in list_:
            return 31
        return 30

obj = Num_of_days()
print(obj.numberOfDays(2020, 0))
'''