import sys
import time
import random
import datetime
import telepot
import time
import os

from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
ADAFRUIT_IO_USERNAME = 'Amruth_19'

chat_id=os.getenv('chat_id') 

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)
    print ("Chat Id : %s" % chat_id)
    if command == 'lighton' or command == 'lon':
       dvalue=1
       print('Publishing a new message...')
       print('Publishing {0} to lampcontrol.'.format(dvalue))
       client.publish('lampcontrol', dvalue)
       time.sleep(2)
       bot.sendMessage(chat_id, text="LIGHT TURNED ON")
       bot.sendPhoto(chat_id=chat_id, photo=open('on.png', 'rb'))
    
    elif command =='lightoff' or command =='loff' :
       dvalue=0
       print('Publishing a new message...')
       print('Publishing {0} to lampcontrol.'.format(dvalue))
       client.publish('lampcontrol', dvalue)
       time.sleep(2)
       bot.sendMessage(chat_id,text="LIGHT TURNED OFF")
       bot.sendPhoto(chat_id=chat_id, photo=open('off.png', 'rb'))
       

bot = telepot.Bot('937417273:AAGN5bAu68cCHcrF9V7aEXVX6aZYagZNfhs')
bot.message_loop(handle)
print ('I am listening...')


def connected(client):
    print('Connected to Adafruit IO!  Listening for LampControl changes...')
    client.subscribe('lampcontrol')

def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

def publishdata(dvalue):
    print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
    print('Publishing {0} to lampcontrol.'.format(dvalue))
    client.publish('lampcontrol', dvalue)


client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

client.connect()

client.loop_background()

while 1:

        time.sleep(1)
        
        
        
