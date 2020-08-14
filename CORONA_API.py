import requests
from datetime import datetime

urlLine = 'https://notify-api.line.me/api/notify'
token = '3CTWCpAWezPDnIcCWzsqOoJIZ6QqQo7ZoSYFX2Wz7aw' #ห้อง DEV
#token = 'EOdMT0lU6tBjKAP3c5umNkba78qIvMWSXkc1BGGijE2' #ห้อง BigFamily
#token = 'Lg2p0kPE1IfiMX8XdJGCnBH4AxacrHQD1yU8rWWgw7J' #ห้อง OPER
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

"""
url = 'https://corona.lmao.ninja/all'
r = requests.get(url)
j = r.json()
print(j)
"""

#country = 'thailand'
#url=f'https://corona.lmao.ninja/countries/{country}'
url = 'https://covid19.th-stat.com/api/open/today'
r = requests.get(url)
j = r.json()

"""
url=f'https://corona.lmao.ninja/all'
r = requests.get(url)
timestamp = r.json()
"""

"""
#print(j)
print('ติดเชื้อทั้งหมด : ' , j['cases'])
print('ติดเชื่อเพิ่ม : ' , j['todayCases'])
print('ตายทั้งหมด : ' , j['deaths'])
print('ตายเพิ่ม : ' , j['todayDeaths'])
print('หายแล้ว : ' , j['recovered'])
print('กำลังรักษา : ' , j['active'])
print('อาการหนัก : ' , j['critical'])
"""

#timestamp = int(timestamp['updated']) // 1000 #ตัดออกไป 3 หลัก
#DT = datetime.fromtimestamp(timestamp)
#print("dt_object =", DT)

message = '\n' + 'รายงานสถานะการ COVID 19\n'
#message += 'อัปเดตล่าสุด : ' + str(DT) + '\n'
message += 'อัปเดตล่าสุด : ' + str(j['UpdateDate']) + '\n'
message += 'พบผู้ติดเชื้อเพิ่ม : ' + str(j['NewConfirmed']) + '\n'
message += 'พบผู้เสียชีวิตเพิ่ม : ' + str(j['NewDeaths']) + '\n'
message += 'รวมจำนวนผู้ติดเชื้อทั้งหมด : ' + str(j['Confirmed']) + '\n'
message += 'รวมผู้เสียชีวิตทั้งหมด : ' + str(j['Deaths']) + '\n'
message += 'รักษาหายแล้ว : ' + str(j['Recovered']) + '\n'
message += 'กำลังรักษา : ' + str(j['Hospitalized']) + '\n'
#message += 'อาการหนัก : ' + str(j['critical']) + '\n'
message += 'ข้อมูลจาก : ' + str(j['Source']) + '\n'
#message += 'Create by Nong2 COVID_API v0.1'
#message += 'Create by Nong 2 COVID_API v0.2' #เพิ่ม อัปเดตล่าสุด
message += 'Create by Nong 2 COVID_API v1' #เปลี่ยน Source ใหม่
print(message)

r = requests.post(urlLine, headers=headers , data = {'message':message,'stickerPackageId':2,'stickerId':524,}) #ส่งไลน์
print(r)
