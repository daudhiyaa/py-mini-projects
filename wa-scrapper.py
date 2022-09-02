import pywhatkit as pw

list_name = ['Cassandra', 'Alex']
list_number = ['+62812376213390', '+6281237561800']
img = '/Users/macbook/py-mini-projects/pywhatkit.jpg' # path through your image

for i, j in zip(list_name, list_number):
    txt = "Happy Gradution " + i

    # Send message in 20s, then close the tab after 5s
    pw.sendwhatmsg_instantly(j, txt, 20, True, 5)

    # Send image without caption in 30s, then close the tab after 5s
    pw.sendwhats_image(j, img, '', 30, True, 5)