import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def print_chars():
    width = 0

    while True:
        try:
            width = int(input("Enter width of rectangle (max 25): "))

            if width > 25:
                print(f"Error: ", width, " is too high. Please enter 25 or lower.")
            elif width <= 0:
                print("Error: please enter a positive number.")
            else:
                # if valid, break out of the loop
                break

        except ValueError:
            print("Invalid input. Please enter a whole number")
        
    for i in range(5):
        print("O" * width)

# Run function1
print_chars()