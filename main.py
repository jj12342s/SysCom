from threading import Thread 
import csv 

def print_diff(current, previous):
    if current != previous:
        
            for i in reversed(range(len(current) - len(previous))):
                if not i:
                    continue
                if not current[-i -1][0] == user:
                    print(current[-i -1][0] )
                    print(current[-i -1][1] + "\n")
def refresh_incomming():
    global user
    previous_text = []
    while True:
        current_text = []
        with open("room.csv", "r") as file:
            file = csv.reader(file)
            for line in file:
                current_text.append(line)

            print_diff(current_text, previous_text)
            previous_text = current_text

def take_input():
    global user 
    while True:
        with open("room.csv", "a") as file:
            file = csv.writer(file)
            message = input()
            file.writerow([user, message])
            


if __name__ == "__main__":
    global user
    user = input("What is your name?")
    t1 = Thread(target=refresh_incomming)
    t2 = Thread(target=take_input)
    
    t2.start()
    t1.start()
    