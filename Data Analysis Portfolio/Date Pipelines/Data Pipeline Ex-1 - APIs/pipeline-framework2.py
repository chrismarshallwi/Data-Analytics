#GET REQUEST --> POSTGRES DATABASE
#INGEST DATA

#PART 2: USING PSYCOPG2 TO INSERT DATA INTO DATABASE

#This file performs a get request with the mock API created in part 1
#After getting the data, it is uploaded into a Postgres database
#The following script demonstrates the following:

#1 Get requests
#2 Psycopg2
#3 Inserting data acquired from API into Postgres
#4 Data Pipelines

import psycopg2 as pg2
import requests

with requests.get('http://127.0.0.1:5000/very_large_request/10', stream=True) as r:
    
    conn = pg2.connect(dbname='postgres',user='postgres',password='Packers1')
    cur = conn.cursor()
    sql = "INSERT INTO transactions (txid, uid, amount) VALUES (%s,%s,%s)"

    buffer = ''
    for chunk in r.iter_content(chunk_size=1):
        if chunk.endswith(b'\n'):
            t = eval(buffer)
            print(t)
            cur.execute(sql, (t[0],t[1],t[2]))
            conn.commit()
            buffer = ''
        else:
            buffer += chunk.decode()

