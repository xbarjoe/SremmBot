import tweepy
from PIL import Image
import os
import numpy as np
import math
from datetime import datetime
import time

#global values
idx = 0
pix = 255,255,255

if __name__ == "__main__":
    main()
    
def set_authentication():
    auth = tweepy.OAuthHandler(auth_keys.oAuthH, auth_keys.oAuthH2)
    auth.set_access_token(auth_keys.access, auth_keys.access2)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
def post():
    media = api.media_upload("sremm"+str(idx)+".png")
    tweet = ""
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])
def main():
	set_authentication()
    for i in range(0,5):
        im = Image.open("sremm"+str(idx)+".png")
        pixels = im.load()
        width, height = im.size
        list_of_pixels = list(im.getdata())
        if str(idx) != "0":
            os.remove("sremm"+str(idx)+".png") 
        for j in range(0,height-1):
            list_of_pixels.insert(int(math.ceil(((width+1)*j)+(width/2))),pix)
        newsize = (im.size[0]+1,im.size[1])
        im2 = Image.new(im.mode, newsize)
        im2.putdata(list_of_pixels)  
        #im2.show()                            
        idx+=1
        im2.save("sremm"+str(idx)+".png","PNG")
    post()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Posted at: ", current_time)
    time.sleep(14400)
	