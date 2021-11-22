from datetime import timedelta, datetime
# Timestamp(12h) | Action
# 8:30am | pickup
# 9:10am | dropoff
# 10:20am| pickup
# 12:15pm| pickup
# 12:45pm| dropoff
# 2:25pm | dropoff

print("2:25pm | dropoff".split(":"))
t1=timedelta(hours=8,minutes=30)
t2=timedelta(hours=12,minutes=45)
t3=timedelta(hours=14,minutes=25)
print(t2-t1)
print(t3-t2)
diff1=t2-t1
diff2=t3-t2
print(diff1+diff2)