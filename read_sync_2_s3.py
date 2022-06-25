import boto3
import os

path = 'C:\\Users\\talla\\Desktop\\BI\\Sample_Data_BI\\PractFiles\\S3_json_sync\\'
dir_list = os.listdir(path)
print(dir_list)
ffile = []
s3 = boto3.client('s3')
for fn in dir_list:
    #print(fn,"************")
    ffile.append(path + fn)
    print(ffile)
    print("--------------------------------------------------")
for i in range(0,len(dir_list)):    
    s3.upload_file(ffile[i],'my-sf-buk','snowfilesload/{}'.format(str(os.path.basename(ffile[i]))))