from typing import Optional

from fastapi import FastAPI

import string    
import random 

app = FastAPI()


@app.get("/")
def read_root():
    return {"love": "?"}


@app.get("/first-character-of-my-soulmate-name/{my_name}")
def read_item(my_name: str):

    ran = ''.join(random.choices(string.ascii_uppercase, k = len(my_name)))    
    print("The randomly generated string is : " + str(ran))
    name =  str(ran)
    res = 'เนื้อคู่ของคุณจะมีชื่อขึ้นตัวด้วยตัว : '+ name[0]

    if my_name == 'thep' or my_name == 'เทพ':
        res = 'ไม่พบเนื้อคู่'

    return {"love": res}