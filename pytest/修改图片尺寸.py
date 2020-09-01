from PIL import Image


def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':
    file_in = 'E:\\JD\\new\\images\\123.jpg'
    width = 150
    height = 150
    file_out = 'E:\\JD\\new\\images\\new123.jpg'
    produceImage(file_in, width, height, file_out)
