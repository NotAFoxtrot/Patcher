#imports
from rembg import remove
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
from duckduckgo_search import ddg_images
from fastcore.all import *
from time import sleep
from fastdownload import download_url
from fastai.vision.all import *
from time import sleep

def patch_parser(file_name, desired_file_name):
    #takes path of unparsed_data || this is complete
    #all images of unparsed_data will have backgrounds removed and will ask for a name
    #all parsed_data will be put in the available folder
    #unparsed_data will be purged - to be completed among last steps for testing purposes
    input = Image.open(file_name).to_thumb(254,254)
    input.save(file_name)
    output = remove(input)
    imageBox = output.getbbox()
    output_boxed = output.crop(imageBox)
    output_boxed.save(desired_file_name)

def debugger():
    #unsure of how to implement, will ask for instruction later
    #once a day will go over the patchadex and see if any entries are the same and try to reconcile it
    pass



if __name__ == "__main__":
    patch_parser('data/unparsed_data/20230718_103348.jpg', 'data/parsed_data/chimera_patch.png')