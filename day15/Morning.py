import time

# fullTime = int(time.strftime('%H:%M:%S'))
# print(fullTime)

HourTime = int(time.strftime('%H'))
# print(HourTime)

MinuteTime = int(time.strftime('%M'))
# print(MinuteTime)

# SecondTime = int(time.strftime('%S'))
# print(SecondTime)

if(HourTime == 5 or HourTime < 12):
    print("Good Morning")
elif(HourTime >= 12 or HourTime <= 18):
    print("Good Afternoon")
elif(HourTime >= 18 or HourTime <= 5):
    print("Good Night")