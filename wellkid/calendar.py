date_str = input("какое сегодня число?--> ")
today = int(date_str)
if today == 1:
    yesterday = 31
else:
    yesterday = today - 1
if today == 31:
    tomorrow = 1
else:
    tomorrow = today + 1
print("вчера было " + str(yesterday) + " число")
print("сегодня " + date_str + " число")
print("завтра будет " + str(tomorrow) + " число")