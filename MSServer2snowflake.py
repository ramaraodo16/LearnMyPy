# sql server data to snowflake create
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pyodbc as pyo
print("opening sql sever database")
con_mssql = (r"Driver={SQL Server};Server=LAPTOP-857D9LHD;"
            "Database=AdventureWorks2017;UID=INFA_DOM;PWD=INFA_DOM;")
conn = pyo.connect(con_mssql)
print("opened  Sql Server database")

sql = "select * from  [Person].[Address]"
df = pd.read_sql(sql,conn)
print(df)
conn.close()
print("Sql server connection closed")
print("start Snoflake connection")
sql_sf = 'CREATE OR REPLACE TABLE ADDRESS ("AddressID" int , "AddressLine1" varchar(60) NOT NULL, "AddressLine2" varchar(60) NULL,"City" varchar(30) NOT NULL,"StateProvinceID" int NOT NULL,"PostalCode" varchar(15) NOT NULL, "SpatialLocation"  varchar(95) NULL, "rowguid"  varchar(150)  NOT NULL,"ModifiedDate" datetime NOT NULL);'

scnn = snowflake.connector.connect(
    user='ramaraodo16',
    password='Tarak#0504',
    account='px02993.us-east-2.aws',
    warehouse='COMPUTE_WH',
    database='AdventureWorks2022',
    schema='person'
)
consf = scnn.cursor()
print("connected to snowflake")
consf.execute(sql_sf)
print("snowflake table created")
print("writing to snowflake table")
sql_dbu = "Use database AdventureWorks2022;"
consf.execute(sql_dbu)
print("database used")
sql_dbs = "Use Schema person;"
consf.execute(sql_dbs)
print("Schema used")
sql_getdb = "select * from AdventureWorks2022.person.Address;"
consf.execute(sql_getdb)
#df_results1 = consf.fetch_pandas_all()
#print(df_results1)
print("===================================",consf.execute(sql_getdb))
#success, nchunks, nrows, _ = write_pandas(scnn,df,'Address', schema = 'person', database='AdventureWorks2022')
    #success, nchunks, nrows, _  = write_pandas(scnn, df, 'Address')   
success, nchunks, nrows, _ = write_pandas(scnn,df,'ADDRESS', chunk_size = 300, schema = 'PERSON')     
print("copied data sucessfully")
print("snowflake data available")
sql_n2 = "select * from ADDRESS limit 19;"
consf.execute(sql_n2)
df_results = consf.fetch_pandas_all()

scnn.close()
print(df_results)
print("Operation sucessful")