import datetime
dt = datetime.datetime.now().date()
 
print("day details"+str(dt.day))
print("Month details"+str(dt.month))
print("Month details"+dt.strftime("%b").upper())
print("Year details"+str(dt.year))
dnum = dt.day
mname = dt.strftime("%b").upper()
mnum = dt.month
year = dt.year
ymdnum = year*10000+(mnum*100)+dnum
ymnum= year*100+mnum
print(ymdnum,ymnum)