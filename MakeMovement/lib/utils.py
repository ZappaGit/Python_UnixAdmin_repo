
import logging


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
