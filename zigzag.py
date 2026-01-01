import time, sys

indent = 0
indent_increasing = True

print(type(None))

try:
    while True:
        print(" " * indent, end='')
        print("********")
        time.sleep(0.1) # 1/10 second pause

        if indent_increasing:
            indent += 1
            if indent == 20:  
                indent_increasing = False
        
        else:
            # Decreases the number of " " before the ***
            indent = indent -1
            if indent == 0:
                # Change direction:
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()

