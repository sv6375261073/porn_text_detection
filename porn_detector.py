import keyboard
import os
import psutil
import pickle
from tensorflow.keras.models import load_model
new_model = pickle.load(open('porn_detection_model.pkl','rb'))
print('model_loaded')
def firewall(text):
    p=new_model.predict([text])
    process_ids=[proc.pid for proc in psutil.process_iter() if 'chrome' in proc.name()]
    if p=='porn':
        keyboard.write('inappropriate',1)
        for pr_id in process_ids: 
            try:
                os.kill(pr_id,2)
            except Exception as e:
                print(e)
    else:
        print(text,p)
def generate_events():
    while True:
        yield keyboard.read_event()   # yield is used to return a value while didn't terminate execution of function 
strings = keyboard.get_typed_strings(generate_events())
while True:
    try:
        text=next(strings)
        if text=='exit':
            break
        else:
            firewall(text)
    except Exception as e:
        print(e)