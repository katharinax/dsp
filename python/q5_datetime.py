# Hint:  use Google to find python function

import pandas as pd

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'  

date_start_dt = pd.to_datetime(date_start)
date_stop_dt = pd.to_datetime(date_stop)
print((date_stop_dt - date_start_dt).days) # 937

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start_dt = pd.to_datetime(date_start, format = "%m%d%Y")
date_stop_dt = pd.to_datetime(date_stop, format = "%m%d%Y")
print((date_stop_dt - date_start_dt).days) # 513

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_start_dt = pd.to_datetime(date_start)
date_stop_dt = pd.to_datetime(date_stop)
print((date_stop_dt - date_start_dt).days) # 7850
