import requests
import os
import time
import shutil
import soundfile as sf
import io
from scipy.io.wavfile import write
import subprocess

# this function is used to send an audio to a specific service
def send_audio():
    
    overall_start = time.time()
    # set url for desired service
    url = 'http://172.16.0.211:6969/upload'
    # add file location below where the audio from mic is saved
    file_location = '/home/techresearch/furqan/Projects/Allison_on_device/audio_data/downsampled/furqan_ahmed_1.wav'
    # we are setting the post body key to file as our flask service will see whether this key is present or not    
    files = {'file': open(file_location, 'rb')}
    values = {'file': 'furqan_ahmed_testing1.wav', 'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
    # using python requests library to send a post call to a service
    r = requests.post(url, files=files, data=values)
    
    print(r.status_code)
    print(type(r.headers['content-type']))
    if r.status_code == 200 and (r.headers['content-type']) == 'audio/x-wav':
        # add the path of file where you need to store the file sent coming in response in our case it is mentioned below
        data, samplerate = sf.read(io.BytesIO(r.content))
        print(samplerate)
        print(data)
        write('/home/techresearch/furqan/Projects/Allison_on_device/files/raw_response.wav',samplerate,data)
        command = "ffmpeg  -hide_banner -nostats -loglevel fatal -y -i '/home/techresearch/furqan/Projects/Allison_on_device/files/raw_response.wav' -ar 22050 /home/techresearch/furqan/Projects/Allison_on_device/files/response_audio.wav"
        subprocess.call(command, shell=True)
    
    print(r)
    
    overall_end= time.time()
    print ("Total time: {}".format(overall_end-overall_start))
    

    
    return r


# To send the audio
s = send_audio()

import IPython.display as ipd
ipd.Audio('/home/techresearch/furqan/Projects/Allison_on_device/files/response_audio.wav', rate= 22050)
