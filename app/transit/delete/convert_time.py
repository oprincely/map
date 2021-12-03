def time_to_int(hour,minute,second):
    minutes = hour * 60 + minute
    seconds = minutes * 60 + second
    return seconds

def int_to_time(seconds):
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return f'{round(hour)}:{round(minute)}:{round(second, 1)}'

def get_hour_or_min(seconds):
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return hour,minute
	
def time_to_sec(hour,minute,second):
    minutes = hour * 60 + minute
    seconds = minutes * 60 + second
    return seconds