import thingspeak
import json
import time, sys

channel_id = 1850502 # put here the ID of the channel you created before
write_key = 'U22K59XZQ3MDYUOT' # update the "WRITE KEY"
read_key = '3ZEF0QV0PHCA8TAC'


channel2 = thingspeak.Channel(id=channel_id, api_key=read_key, fmt = 'json')

str=channel2.get_field_last(field=2)
dic=json.loads(str)
status=dic["field2"]

colors = "12345"

for color in colors:
    print(color)

print(status)