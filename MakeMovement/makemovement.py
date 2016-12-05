import time
import subprocess
import os
from subprocess import Popen
import vert_to_horizontal
import logging
import json
import argparse
from lib.utils import processDirectory

logger = logging.getLogger(__name__)


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
    logging.basicConfig(filename='makemovement.log',level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    logging.getLogger('develop').setLevel(logging.INFO)
    print "log working"
    logging.info("loggin.info dice oye")
    logger.info("logger.info dice dime")
    print "log logging"

    logger.info("arrancando parser para los argumentos")
    parser = argparse.ArgumentParser(description='resolve a video with images')
    parser.add_argument('--ifolder',dest='ifolder', help='image folder')
    parser.add_argument('--iext', dest='iext', help='image format extension file')

    args = parser.parse_args()
    print args.ifolder

    if args.ifolder:
        logger.info("entrar en:" + args.ifolder)
        if processDirectory(args):
            logger.info("procesamiento OK")
        else:
            logger.info("procesamiento de directorio fallido")

        #gifecator = Gifecator("C:\\PragaBudapest")

    else:
        logger.debug("imposible entrar en none imagefolder")

        #logger.info("select: " + args.IF)
    #logger.info("Done. elapsed:%ss" % (int(time.time() - start_time)))

    #print os.getcwd()
    #print os.getcwd() + "\\Resources\\"
    #processDirectory("C:\\PragaBudapest")
    #gifecator.takeGif()
