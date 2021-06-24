import os
from PIL import Image
 
base_directory = "data/" 
percentage = 0.3
def reduce_images(directory, percentage):
    """ 
    Given a base directory with a number of subdirectories, 
    create a smaller copy of each imahe with same name in a 
    folder called "resize" 
    """
    for directory in os.listdir(base_directory):
        sub_dir = (os.path.join(base_directory, directory))
        for f in os.listdir(sub_dir):
            old_f = os.path.join(sub_dir, f)
            im = Image.open(old_f)
            width, height = im.size
            new_f = old_f.replace("data", "resize")
            SIZE = (width * percentage, height * percentage)
            im.thumbnail(SIZE)
            im.save(new_f, optimize=True)

if __name__ == '__main__':
    reduce_images(base_directory)