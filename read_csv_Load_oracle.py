import os
import cx_Oracle
from numpy import append
import sqlalchemy
import config
import pandas as pd

path = "C:\\Users\\talla\Desktop\\Files\\"
engin = sqlalchemy.create_engine('oracle://Rept_user:Rept_user@localhost:1521/orcl12c')
def read_file_local_dir():
    
    loc = os.listdir(path)
    print("count of files in the dir is",len(loc))
    arr_csv = []
    for a1 in loc:
        if(len(a1.split('.')) ==2 ):
            arr_csv.append(a1)
    print("CSV files count is ",len(arr_csv))   
    return arr_csv

def oracle_conn():
    con_ora= None
    try:
        con_ora = cx_Oracle.connect(config.username,
                                    config.password,
                                    config.dsn,
                                    encoding=config.encoding)
        print(con_ora.version)
    except cx_Oracle.Error as error:
        print(error)
    finally:

        if con_ora:
            con_ora.close()

def read_csv_write_oracle():
    i =0
    for f1 in read_file_local_dir():
        i =i+1
        #print( path+f1)
        df = pd.read_csv(path+f1)
        df_rd =pd.read_sql_table('nse_stock_daily_f',engin)
        df.to_sql(name= 'nse_stock_daily_f',con= engin ,index=False,if_exists='append')
    print("Done sucess",i)
#oracle_conn()
#read_file_local_dir()
print("write function will starts=========================")
read_csv_write_oracle()