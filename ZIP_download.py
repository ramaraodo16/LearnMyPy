import wget
import shutil

import datetime
dt = datetime.datetime.now().date()
 
dnum = dt.day
mname = dt.strftime("%b").upper()
mnum = dt.month
year = dt.year
ymdnum = year*10000+(mnum*100)+dnum
ymnum= year*100+mnum

files = []
#files1 = []
for k in range(2017,2023):
    #print(k)
    
    #monts= ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    #montnum = [1,2,3,4,5,6,7,8,9,10,11,12]
    monkey_it = {'JAN' : 1,'FEB': 2,'MAR': 3,'APR': 4,'MAY': 5,'JUN': 6,
                'JUL': 7,'AUG': 8,'SEP': 9,'OCT': 10,'NOV': 11,'DEC' : 12}
    if (k <= year ):
            pass
    else:
            break
    for key,val in monkey_it.items():
        if (ymnum >= k*100+val):
            pass
        else:
            break
        for i in range(1,31):
            if (ymdnum >= k*10000+val*100+i):
            
                filename= 'cm'+str(i).zfill(2)+key+str(k)+'bhav'
                #print('\n'+filename)
                
                url = 'https://www1.nseindia.com/content/historical/EQUITIES/'+str(k)+'/'+key+'/'+filename+'.csv.zip'
                #print(url)
                try:
                    #print("enter try in loop")
                    wget.download(url)
                    files.append(filename+'.csv.zip')
                    #files1.append(filename+'.csv')
                except:
                    pass
            else:
                break
    monkey_it.clear
print(files)

import zipfile

for fw in files:
 print(fw)
 with zipfile.ZipFile(fw, 'r') as zip_ref:
    zip_ref.extractall('C:\\Users\\talla\\Desktop\\Files')
 shutil.move(fw,'C:\\Users\\talla\\Desktop\\FIles')
  