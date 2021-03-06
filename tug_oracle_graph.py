import os
import cx_Oracle
import logging
from datetime import datetime


if __name__ == "__main__":
    '''
    Just a little script to quickly test a connection to an Oracle DB.
    Output the results into a csv file, so we can run this for a week and do some graphs and charts (thought up due to connection issues)
    Get the coonection string and sql to test with from environment variables (increase server security/portability)
    Uses python 3, could easily be changed to older version (change print statement, maybe something else)
    '''
    dt_end = None
    dt_start = None
    try:
        fpath = os.getenv('tug_oracle_graph_path')
        fname = ''.join([fpath,'tug_connect_graph_data.csv'])
        headers = ''
        if not os.path.isfile(fname):
            headers = 'Start Date, Execution Time, Outcome\n'
        with open(fname,"a+") as f:
            # first time in, create the headers
            if len(headers) > 0:
                f.write(headers)
           
            try:     
                #Connection string format: dbuser/password:dns_or_ip:port/DB (eg. my_user/my_nice_passwd:x.x.x.x:1521/my_db_name)
                connect_info = os.getenv('tug_oracle_db')
                dt_start = datetime.now()   
                assert connect_info != None, 'Connection environment variable not set: tug_oracle_db'

                con = cx_Oracle.connect(connect_info)
                cur = con.cursor()

                #arraysize -> This read-write attribute specifies the number of rows to fetch at a time internally and is the default number of rows to fetch with the fetchmany() call.
                # can adjust the setting to decrease network round trips, currently perform test with less than 10 rows
                cur.arraysize = 10

                location_sql =  os.getenv('tug_oracle_sql')
                assert location_sql != None, 'sql statement environment variable not set: tug_oracle_sql'
                cur.execute(location_sql)
                row_list = cur.fetchmany()
                dt_end = datetime.now()
                
                # determine field values
                start_date = str(dt_start.strftime('%a %b. %d %Y - %I:%M %p'))
                #determine the time delta from start to finish
                delta = (dt_end - dt_start).total_seconds()
                outcome = 'True'        
                f.write(''.join([start_date,',',str(delta),',',outcome,'\n']))
               
                cur.close()
                con.close()
          
            except Exception as e:
                logging.exception(e)      
            finally:
                if dt_end == None:
                    # connection time or issue
                    dt_end = datetime.now()

                    # determine field values
                    start_date = str(dt_start.strftime('%a %b. %d %Y - %I:%M %p'))
                    #determine the time delta from start to finish
                    delta = (dt_end - dt_start).total_seconds()
                    outcome = 'False'        
                    f.write(''.join([start_date,',',str(delta),',',outcome,'\n']))                     
    finally:
        f.close()