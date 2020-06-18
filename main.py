import requests
import datetime
import os
try:
    os.mkdir("files")
except FileExistsError:
    pass
VHBB_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
r = requests.get('https://rinnegatamante.it/vitadb/list_hbs_json.php',headers={"user-agent":VHBB_UA}).json()

for entry in r:
    titleid = entry["titleid"]
    name = entry["name"]
    count = entry["downloads"]
    idd = entry["id]
    date = datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    l = (titleid,name,count,date,idd)
    try:
        f = open(f"files/{titleid}.csv","x")
    except:
        f = open(f"files/{titleid}.csv","a")
    for i in list(l):
        try:
            f.write(str(i))
        except UnicodeEncodeError:
            f.write("unicode sucks")
        if l.index(i) != len(l) -1:
            f.write(",")
    f.write("\n")
    f.close()
