#A Python program that tracks a farmer's harvest across 5 fields. You will calculate the total and average yield, pack the harvest into 25 kg bags, find the leftover grain, compare this year's harvest with last year's, and update the total with a bonus crop and seed reserve.
a=12467
b=34114
c=452492
d=415418
e=416257
bonuspoints=1461



print('the value of 5 teams yields respectively are',a,b,c,d,e,)
average=a+b+c+d+e/5
print('the average team score=',average)
divide=a+b+c+d+e/25
print('the stars in the bags =',divide,'stars ')

lastyear=586963
if a+b+c+d+e>lastyear:
 print('this year score is better than lastyear')
if a+b+c+d+e<lastyear:
 print('this year scoreg is not better than lastyear')
updatedversion=a+b+c+d+e+bonuspoints
print(updatedversion,'this is the updated version of score') 

