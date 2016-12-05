from PIL import Image
import logging
import os

logger = logging.getLogger(__name__)

def processDirectory(args):
    print "processing"
    logger.debug("entrando en el folder")
    #size = (520, 360)
    if os.path.isdir(args.ifolder):
        logger.debug("folder existe")
    else:
        return False
    if not os.path.isdir(args.ifolder + "\\temp"):
        logger.debug("crea directorio temporal")
        os.mkdir(args.ifolder + "\\temp")
    else:
        logger.debug("existe temporal")
    if args.iext:
        logger.info("formato de las imagenes: " + args.iext)
        iext=args.iext
    else:
        iext=".jpg"
        logger.info("formato por defecto .jpg")

    fileGIfs = open(args.ifolder + "\\temp\\temp.txt", "w+")
    for dirname, dirnames, filenames in os.walk(args.ifolder):
        logger.debug("bucle en dirname: " + dirname)
        logger.debug("bucle en dirnames: %s", dirnames)
        logger.debug("bucle en filenames: %s", filenames)

        for file in filenames:
            logger.debug("procesando fichero: " + file)
            if (".JPG" in file) or (iext in file):
                logger.debug("imagen detectada")

                name = os.path.join(dirname, file)
                logger.debug(name)

                print name
                #im1 = Image.open(name)
                #print(im1.size)
                #print(im1.info)
                #if "v" in file:
                #     print "vertical"
                #     vert_to_horizontal.crop_image(name)
                #     vert_to_horizontal.join(name)
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
            else:
                logger.debug("nada que hacer con ese")
    fileGIfs.close()
    print "directory %s processed" % os.path.dirname(args.ifolder)
    return True
