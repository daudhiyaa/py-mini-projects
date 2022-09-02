# src = https://pypi.org/project/pywhatkit/
import pywhatkit as pw

# Send a WhatsApp Message to a Contact at 1:30 PM
pw.sendwhatmsg("+910123456789", "Hi", 13, 30)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pw.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pw.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pw.sendwhats_image("+910123456789", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pw.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pw.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
pw.playonyt("PyWhatKit")