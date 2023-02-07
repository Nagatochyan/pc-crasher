import keyboard
while True:
  while keyboard.is_pressed:
    keyboard.send("a")
