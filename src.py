#imports
from rembg import remove
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np


def database_checker(picture):
    #will be run in patch_parser
    #takes a picture and asks database if it looks like any of the pictures within
    #if not, looks at the name and does the same
    #either creates new patch in 'Patchadex' or is put in the same folder as a 'Patchadex' entry
    pass

def patch_parser(file_name, desired_file_name):
    #takes path of unparsed_data
    #all images of unparsed_data will have backgrounds removed and will ask for a name
    #all parsed_data will be put in the available folder
    #unparsed_data will be purged
    input_perfect = file_name
    output_perfect = desired_file_name
    input = Image.open(input_perfect)
    print(input)
    input.save(r'data/unparsed_data/20230718_091148.png')
    output = remove(input)
    output.save(output_perfect)

def debugger():
    #unsure of how to implement, will ask for instruction later
    #once a day will go over the patchadex and see if any entries are the same and try to reconcile it
    pass



if __name__ == "__main__":
    patch_parser('data/unparsed_data/20230718_091148.jpg', 'data/parsed_data/chimera_patch.png')