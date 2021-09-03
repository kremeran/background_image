from PIL import Image, ImageDraw, ImageFont
import socket

width = 1920
height = 1080

try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
except:
    print("Unable to get Hostname and IP")

img = Image.new('RGB', (width, height), color='#000000')

# get a font
fnt = ImageFont.truetype("FreeMono.ttf", 40)
# get a drawing context
d = ImageDraw.Draw(img)

# draw multiline text
d.multiline_text((100,100), host_name + "\n" + host_ip, font=fnt, fill=(255, 255, 255))

img.save("background.jpg")
