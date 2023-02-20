import subprocess
# fire install req command
process = subprocess.Popen(['cmd', '/C', 'INSTALLreq.bat'], creationflags= subprocess.CREATE_NEW_CONSOLE)
exit_code = process.wait()


from PIL import Image
import os

cwd = os.getcwd()
filename = "result.png"

path = os.path.join(cwd, filename)

# Open the image file
img = Image.open(path)

# Display the image
img.show()