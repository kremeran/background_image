from PIL import Image, ImageDraw, ImageFont
import socket
import configparser
import os

try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
except:
    print("Unable to get Hostname and IP")

config = configparser.ConfigParser()
config.read("/home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf")
wallpaper = config["*"]["wallpaper"]

split_path = wallpaper.split("/")
split_path.pop()
wallpaper_dir = "/".join(split_path)

with Image.open(wallpaper) as img:

    # get a font
    fnt = ImageFont.truetype("FreeMono.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(img)

    # draw multiline text
    d.multiline_text((150,100), host_name + "\n" + host_ip, font=fnt, fill=(255, 255, 255))

    img.save(wallpaper_dir + "/custom.jpg")
    
config["*"]["wallpaper"] = wallpaper_dir + "/custom.jpg"
config["*"]["wallpaper_mode"] = "stretch"

with open("/home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf", "w") as configfile:
    config.write(configfile)