dur = int(input())

hour = int(dur/(60*60))
dur_res = dur % (60*60)
minu = int(dur_res/60)
seg = dur_res % 60

print(str(hour)+ ":" + str(minu) + ":" + str(seg))