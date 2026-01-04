import logging
logging.basicConfig(filename = "staples_log.log", level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s" )

supplies = ['pens', 'stapler', 'flamethrowers', 'binder', 'staples']

logging.debug("Start of program")
logging.debug("Print statement, iterate of list, print index and value")

for i in range(len(supplies)):
    print("Item number: ", str(i), "is product name of: ", supplies[i])