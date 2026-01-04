import logging

logging.basicConfig(filename = "cats_log.log", level = logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s" )

logging.debug(" *** Start of Program *** ")
cat_names = []

while True:
    name = input('Enter the name of cat ' + str(len(cat_names) + 1) + 
        " (Or enter nothing to stop.):")
    logging.debug("User entered cat name of:" + name)
    if name == "":
        break
    
    cat_names = cat_names + [name] # List concatenation

    print("The cat names are:")
    for name in cat_names:
        print(" " + name)
        

      
