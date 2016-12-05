from PIL import Image
import time
import subprocess
import os
from subprocess import Popen
import vert_to_horizontal
import logging
import logging

logger = logging.getLogger(__name__)


def processDirectory(path):
    #size = (520, 360)
    if not os.path.isdir(path + "\\temp"):
        os.mkdir(path + "\\temp")
    fileGIfs = open(path + "\\temp\\temp.txt", "w+")
    for dirname, dirnames, filenames in os.walk(path):
        for file in filenames:
            if ".JPG" in file:
                name =os.path.join(dirname, file)
                print name
                #im1 = Image.open(name)
                #print(im1.size)
                #print(im1.info)
                if "v" in file:
                     print "vertical"
                     vert_to_horizontal.crop_image(name)
                     vert_to_horizontal.join(name)
                     #girada2 = im1.transpose(Image.ROTATE_90)   # Obtener imagen girada 90
                #    print(girada2.size)
                #    #girada2.show()
                #    girada2.save(os.path.join(dirname, "girada2.JPG"))
                #im1 = im1.resize(size)
                #nameOUT = name.replace('bmp', 'png')
                #im1.save(nameOUT)
                fileGIfs.write("file '" + name +"'\n")
                fileGIfs.write("duration 0.18\n")
                #os.remove(name)
                #im1.close()
    fileGIfs.close()
    print "directory %s processed" % os.path.dirname(path)

class Gifecator(object):

    def __init__(self, path):
        print "iniciando"
        self.path = path + '\\temp\\temp.txt'
        resPath = path.split("\\")
        self.resPath = os.getcwd() + "\\Resources\\"

    def takeGif(self):
        print self.resPath
        print self.path
        command = self.resPath + 'ffmpeg.exe -loglevel verbose -y -f concat -safe 0 -i "' + str(self.path) + '" -s 300x200 -c:v libx264 -vf "fps=25,format=yuv420p " "' + os.path.dirname(self.path) + '\\out.mp4"'

        print command

        if os.path.exists(os.path.dirname(self.path) + '\\out.mp4'):
            os.remove(os.path.dirname(self.path) + '\\out.mp4')
        if os.path.exists(os.path.dirname(self.path) + '\\out.gif'):
            os.remove(os.path.dirname(self.path) + '\\out.gif')

        while not os.path.exists(os.path.dirname(self.path) + '\\out.mp4'):
            process = subprocess.Popen(command, shell=True,
                                       stdout=subprocess.PIPE)
            process.wait()
        #print "ahora gifacea"
        #command2 = self.resPath + 'ffmpeg.exe -loglevel quiet -r 2 -i "' + str(os.path.dirname(self.path)) + '\\out.mp4" "' + os.path.dirname(self.path) + '\\out.gif"'
        #while not os.path.exists(os.path.dirname(self.path) + '\\out.gif'):
        #    process = subprocess.Popen(command2, shell=True,
        #                               stdout=subprocess.PIPE)
        #    process.wait()
        print "fin"
        #    pictureTime = pictureTime - datetime.timedelta(seconds=1)
        #print "cool"


if __name__ == '__main__':
    print os.getcwd()
    print os.getcwd() + "\\Resources\\"
    #processDirectory("C:\\PragaBudapest")
    gifecator = Gifecator("C:\\PragaBudapest")
    gifecator.takeGif()
