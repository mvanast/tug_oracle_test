import os
import cx_Oracle
import logging
from datetime import datetime

if __name__ == "__main__":
    '''
    Just a little script to quickly test a connection to an Oracle DB.
    Get the coonection string and sql to test with from environment variables (increase server security/portability)
    Uses python 3, could easily be changed to older version (change print statement, maybe something else)
    '''
    print('testing oracle conn...')
    try:     
        #Connection string format: dbuser/password:dns_or_ip:port/DB (eg. my_user/my_nice_passwd:x.x.x.x:1521/my_db_name)
        connect_info = os.getenv('tug_voyagerdb')
        dt_start = datetime.now()   
        con = cx_Oracle.connect(connect_info)
        cur = con.cursor()

        #arraysize -> This read-write attribute specifies the number of rows to fetch at a time internally and is the default number of rows to fetch with the fetchmany() call.
        # can adjust the setting to decrease network round trips, currently perform test with less than 10 rows
        cur.arraysize = 10

        location_sql =  os.getenv('tug_oracle_sql')
        cur.execute(location_sql)
        row_list = cur.fetchmany()
        dt_end = datetime.now()

        #determine the time delta from start to finish
        delta = (dt_end - dt_start).total_seconds()
        print("Oracle connection time: " + str(delta) + " seconds")
        for row in row_list:
            print(row)
     
        cur.close()
        con.close()
          
    except Exception as e:
        logging.exception(e)      
    finally:
        print('ending conn test')