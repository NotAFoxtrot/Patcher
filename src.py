#imports

def database_checker(picture):
    #will be run in patch_parser
    #takes a picture and asks database if it looks like any of the pictures within
    #if not, looks at the name and does the same
    #either creates new patch in 'Patchadex' or is put in the same folder as a 'Patchadex' entry
    pass

def patch_parser(path):
    #takes path of unparsed_data
    #all images of unparsed_data will have backgrounds removed and will ask for a name
    #all parsed_data will be put in the available folder
    #unparsed_data will be purged
    pass

def debugger():
    #unsure of how to implement, will ask for instruction later
    #once a day will go over the patchadex and see if any entries are the same and try to reconcile it
    pass



if __name__ == "__main__":
    print("hello")