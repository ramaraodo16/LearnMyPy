from msilib.schema import Error
import pandas as pd
from pendulum import today
import sqlalchemy
import cx_Oracle
from datetime import datetime, timedelta
engin = sqlalchemy.create_engine('oracle://Rept_user:Rept_user@localhost:1521/orcl12c')
loaddate =  datetime.strptime('2022-06-01',"%Y-%m-%d")
print(loaddate,"-------",today)
LastSeqID  = 0
def test_data(xdate):
    loaddate =  datetime.strptime(xdate,"%Y-%m-%d")
    print()
    q1= '''select TO_CHAR( loaddate , 'YYYY') ||' Q ' ||TRUNC(TO_number( TO_CHAR(loaddate   ,'Q'))) as Data1,
        (TO_CHAR(loaddate, 'YYYY') ||' Week ') as Data2,
        Decode(TO_CHAR(loaddate ,'Q'),'1',1, decode(to_char(  loaddate,'Q'),'2',1,2)) as Data3 from dual'''
        
    tmp1 = engin.execute("select TO_CHAR(sysdate, 'YYYY') ||' Q ' ||TRUNC(TO_number( TO_CHAR(sysdate,\
        'Q')) ) from dual")
    dtp1 = pd.read_sql(q1.replace('loaddate',"to_date('2022-06-01', 'yyyy-mm-dd')"),engin)
    dtp1.to_sql(name='test1',con=engin ,index=False,if_exists='append')
    print(tmp1)
    print(dtp1)
def Date_dim_generate(xdate):
    #Load_date = loaddate
    loaddate =  datetime.strptime(xdate,"%Y-%m-%d")
    print(loaddate,"enter into the require funciton and read sql")
    #Load_date = datetime.strptime(loaddate,"%Y-%m-%d")
    LastSeqID  = 0
    try:
        query1= ''' 
               SELECT TO_CHAR(loaddate , 'YYYYMMDD') as SR_NUM, 
		Trunc(loaddate) as CALENDAR_DATE,
        Decode(TO_CHAR(loaddate ,'Q'),'1',1,decode(to_char(loaddate ,'Q'),'2',1,2)
        ) as CAL_HALF_YEAR,
        (TO_CHAR(loaddate , 'MM')) AS CAL_MONTH,
        (TO_CHAR(loaddate , 'Q')) AS CAL_QTR,
        TO_CHAR(trunc((ROUND(TO_NUMBER(to_char(loaddate ,'DDD'))) +
		ROUND(TO_NUMBER(to_char(trunc(loaddate , 'YYYY'), 'D')))+ 5) / 7)) AS CAL_WEEK,
        TO_CHAR(loaddate , 'YYYY') AS CAL_YEAR,
        (TO_CHAR(loaddate , 'DD')) as CAL_DATE_NUM,
        (TO_CHAR(loaddate , 'D')) as CAL_DATE_MONTH_NUM,
        (TO_CHAR(loaddate , 'DDD')) as CAL_DATE_YEAR_NUM,
        1 as CAL_DUMMY1,
        1 as CAL_DUMMY2,
        1 as CAL_DUMMY3,
        1 as CAL_DUMMY4,
        1 as CAL_DUMMY5,
        (TO_CHAR(loaddate , 'J')) AS CAL_JAPANIE,
        TO_CHAR(((TO_NUMBER(TO_CHAR(loaddate , 'YYYY')) + 4713) * 12)  +   TO_number(TO_CHAR(loaddate , 'MM'))) AS FY_MONTH,
        ((TO_NUMBER(TO_CHAR(loaddate , 'YYYY')) + 4713) * 4)  + (TO_CHAR(loaddate , 'Q')) AS FY_QTR,
        TO_CHAR(ROund(TO_CHAR(loaddate , 'J')/7 )) as FY_WEEK,
        TO_NUMBER(TO_CHAR (loaddate ,'YYYY')) + 4713  As FY_YEAR,
        TO_CHAR(loaddate , 'Day') AS CAL_DAY_NAME,
        TO_CHAR(loaddate , 'Month') AS CAL_MONTH_NAME,
        Decode(To_Char(loaddate ,'D'),'7','weekend','6','weekend','weekday') AS CAL_WEEK_DAY_NAME,
        Trunc(loaddate ,'DAY') + 1 AS CAL_NEXT_DAY,
        Decode(Last_Day(loaddate),loaddate ,'y','n') AS LOAD_DATE_Y_N,
        to_char(loaddate ,'YYYYMM') AS YYYYMM,
        
        to_char(loaddate ,'YYYY') || ' Half' || Decode(TO_CHAR(loaddate ,'Q'),'1',1,decode(to_char(loaddate ,'Q'),'2',1,2) ) AS YYYY_HALF,
        to_char(loaddate ,'YYYY') || ' Half' || Decode(TO_CHAR(loaddate ,'Q'),'1',1,decode(to_char(loaddate ,'Q'),'2',1,2) ) AS QTR_1_2,
        TO_CHAR(loaddate , 'YYYY / MM')   AS "YYYY / MM",
        TO_CHAR(loaddate , 'YYYY') ||' Q ' ||TRUNC(TO_number( TO_CHAR(loaddate ,'Q')) ) AS "YYYY_QQ",
        TO_CHAR(loaddate , 'YYYY') AS YYYY_WEEK,
        TO_CHAR(loaddate ,'YYYY') AS YEAR_YY FROM DUAL
            '''
    except Error:
        pass
    print("before for loop calculation")
    to_date = today() 
    #print(loaddate+1)
    d1 = datetime.strptime(xdate,"%Y-%m-%d")
    d2 = datetime.strptime(str(to_date)[:10] ,"%Y-%m-%d")
    difdays= (d2-d1).days
    #difdays = 25 
    print("Entering loop")
    LastSeqval = 0
    for i in range(1,difdays):
        #print(" inside for loop step is",i)
        #Date_dim_generate(loaddate)
        LastSeqval = LastSeqval + 1
        abc_1 = "to_date("+"\'"+str(loaddate)[:10]+"\'"+", 'yyyy-mm-dd')"
        try:
            #df = pd.read_sql(query1.replace("loaddate","to_date('2022-06-01', 'yyyy-mm-dd')"),engin)
            df = pd.read_sql(query1.replace("loaddate",abc_1),engin)
            print(df)
            df.to_sql(name='w_day_d',con= engin, schema= 'REPT_USER', index=False,if_exists='append')
            loaddate = loaddate+timedelta(days=1)
            
        except cx_Oracle.Error as error:
            #print(error)
            pass
    print("Done sucess",i)


Date_dim_generate('2000-01-01')
#test_data('2022-06-01')