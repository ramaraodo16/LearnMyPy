from ast import Continue
from optparse import Values
import os, datetime, read_excel_file,csv
from typing import Counter
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
 
#pPATH = 'C:\\Users\\talla\\Downloads\\Compressed\\PBI BBB\\2.Power View\\'
pPATH = 'C:\\Users\\talla\\Desktop\\BI\Snowflake\\SNOWFLAKE SESSIONS\\'
#print(read_excel_file.read_xl_file())
list1 = read_excel_file.read_xl_file()
dict_w= {"Videfile Name":[],"Len_Vfile":[]}
for i in list1:
    if (i.endswith('.mp4')):
        print(i)
        pass
    else:
        Continue
    try:
        clip = VideoFileClip(pPATH+i)
        #print('C:\\Users\\talla\\Downloads\\Compressed\\PBI BBB\\2.Power View\\'+i)
        video_len = str(datetime.timedelta(seconds=clip.duration))
        dict_w["Videfile Name"].append(i)
        dict_w["Len_Vfile"].append(video_len)
        #print(video_len)
        #print("enterd loop")
        clip.reader.close()
        clip.audio.reader.close_proc()
    except:
        pass
#print(dict_w)
with open("SF file OP.csv",'w') as output:
    writer1 = csv.writer(output)
    for key,value in dict_w.items():
        writer1.writerow([key,value])
import pandas as pd
df = pd.DataFrame(data=dict_w).to_csv('mysf_OP.csv')