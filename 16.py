class Time:
    """Represents the time of day.
    
    attibutes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(T):
    print(str('%.2d' % T.hour) + ':' + str('%.2d' % T.minute) + ':' + str('%.2d' % T.second))

print_time(time)

camels = 42
print('%d' % camels)

# print('%.2d' % time.minute)
# print(type(time.minute))
# print(type(time.hour))

def increment(time, seconds):
    time.second += seconds

    while time.second >= 60:
        if time.second >= 60:
            time.second -= 60
            time.minute += 1

        if time.minute >= 60:
            time.minute -= 60
            time.hour += 1

increment(time, 100)
print_time(time)

increment(time, 50)
print_time(time)

increment(time, 120)
print_time(time)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    # print(minutes, time.second)
    time.hour, time.minute = divmod(minutes, 60)
    # print(time.hour, time.minute)
    return time

print(time_to_int(int_to_time(43660)) == 43660)
print(time_to_int(int_to_time(2)) == 2)
print(time_to_int(int_to_time(108000)) == 108000)

t = int_to_time(108000)
print_time(t)

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

time1 = Time()
time1.second = 4
time1.minute = 8
time1.hour = 10

time2 = Time()
time2.second = 4
time2.minute = 8
time2.hour = 10

# print(time_to_int(time1))
# print(time_to_int(time2))
# seconds = time_to_int(time1) + time_to_int(time2)
# print(seconds)

print_time(add_time(time1, time2))
