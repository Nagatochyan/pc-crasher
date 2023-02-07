import keyboard
import mouse
while True:
    while keyboard.is_pressed:
        keyboard.send("a")
    while mouse.click('left'):
        keyboard.send("a")
    while mouse.click('right'):
        keyboard.send("a")
    while mouse.click('middle'):
        keyboard.send("a")
