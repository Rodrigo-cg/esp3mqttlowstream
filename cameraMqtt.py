from PIL import Image
import requests
from io import BytesIO
import os, sys
import datetime
import base64

import paho.mqtt.publish as publish
MQTT_SERVER = "www.mqtt-dashboard.com"
MQTT_PATH = "image_2021"

output = "asd.jpg"

#Cambiar la direccion IP segun su configuracion



url = "http://192.168.0.144/cam-lo.jpg"

while(1):
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))
	buffer = BytesIO()
	img.save(buffer, format="JPEG")
	base64_img = base64.b64encode(buffer.getvalue())
	publish.single(MQTT_PATH, base64_img, hostname=MQTT_SERVER)
	try:
		img.save(output)
	except IOError:
		print("cannot convert", infile)

