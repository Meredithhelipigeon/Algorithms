# calories [40, 10, 30]
# ‍‌‍‌‍‍‌‍‌‌‌‌‌‌‌‍‍‍‌‍prices [8.00, 5.00, 2.15]
# budget 20.00
import heapq as hq
def bestCal(calories,prices,budget):
    info = []
    for i in range(len(calories)):
        hq.heappush(info,(calories[i]/prices[i],prices[i],i))

    ret=0
    while budget>0 and len(info)>0:
        cur=hq.heappop(info)
        curPrice=-cur[1]
        ret+=(budget//curPrice)*calories
        budget-=(budget//curPrice)*curPrice
    return ret

print(bestCal([40, 10, 30],[8.00, 5.00, 2.15],20))