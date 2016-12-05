import PIL
from PIL import Image
from PIL import ImageFilter

hglobal = 2304
wglobal = 3456

def join(imagePath):
    #final = Image.new("RGB",(800,600),"black")
    imagen1 = Image.open('C:\\test_VerticalToHorizontal\\sompic_rescaled.jpg')
    imagen2 = Image.open('C:\\test_VerticalToHorizontal\\sompic_rescaled2.jpg')
    #final.paste(imagen1, (0,0))
    imagen1.paste(imagen2, (1152,0))
    #imagen1.show()
    imagen1.save(imagePath)

def rescale2(image):
    basewidth = 1356
    img = image
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,2034), PIL.Image.ANTIALIAS)
    img.save('C:\\test_VerticalToHorizontal\\sompic_rescaled2.jpg')


def rescale1(image):
    basewidth = 3456
    img = image
    wpercent = (basewidth/float(img.size[0]))
    
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,2034), PIL.Image.ANTIALIAS)
    for i in range(10):
        img = img.filter(ImageFilter.BLUR)
        #img3 = img.filter(ImageFilter.MinFilter(7)) # same as MinFilter(3)
    #img = img.filter(ImageFilter.BLUR)
    #img3 = img.filter(ImageFilter.BLUR(150)) # same as MinFilter(3)
    
    #im3.show()
    #img = img.filter(ImageFilter.BLUR)
    
    img.save('C:\\test_VerticalToHorizontal\\sompic_rescaled.jpg')

def crop_image(input_image):#, output_image, start_x, start_y, width, height):
    """Pass input name image, output name image, x coordinate to start croping, y coordinate to start croping, width to crop, height to crop """
    input_img = Image.open(input_image).rotate(270)
    size_input = input_img.size
    w_output = size_input[0]
    h = size_input[1]
    start_x = 0
    start_y = h/3
    print size_input
    
    box = (start_x, start_y, start_x + w_output, start_y + start_y)
    output_img = input_img.crop(box)
    output_img.save('C:\\test_VerticalToHorizontal\\temp.jpg')
    rescale1(output_img)
    rescale2(input_img)
    #join()
    #output_img.save('C:\\test_VerticalToHorizontal\\sompic.jpg')

#def selectROI(pathImage):
    

if __name__ == '__main__':
    crop_image("C:\\test_VerticalToHorizontal\\girada2.JPG")