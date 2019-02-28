import os


exit =int(0)

def print_func(f_name):
    f1=open(f_name,'r')
    for lines in f1:
        print(lines)
    return 0


while exit==0:

    f3 = open("GOOD_SPEAKERS.txt", 'w')
    f3.write("********LIST OF GOOD SPEAKERS********")
    f3.close()

    f4 = open("BAD_SPEAKERS.txt", 'w')
    f4.write("********LIST OF BAD SPEAKERS********")
    f4.close()

    f5 = open("OUTPUT4_SPEAKERS.txt", 'w')
    f5.write("********LIST OF SPEAKERS WITH THE SERIAL NUMBER********")
    f5.close()

    f6 = open("OUTPUT5_SPEAKERS.txt", 'w')
    f6.write("********LIST OF SPEAKERS WITH THE ENTERED DATE********")
    f6.close()

    print("1)TO SEE A LIST OF GOOD SPEAKERS")
    print("2)TO SEE A LIST OF BAD SPEAKERS")
    print("3)ENTER SERIAL NUMBER TO SEARCH")
    print("4)ENTER DATE FOR LIST OF RESULT ON DATE")
    print("5)EXIT")
    choice=int(input("ENTER YOUR CHOICE(1-5):"))


    if choice==1:
        path = input("ENTER FILE PATH:")#file path for d directory you want to access
        #listing the files in the directory 
        for filename in os.listdir(path):
            #opening the file that is being listed
            f2 = open(filename, 'r')
            #breakind down the file into a list for string comparison
            for line in f2:
                if "GOOD" in line.split():
                    #calling the print_func() to print content of the file
                    print_func(filename)
                    #writing the good speakers into a file called GOOD_SPOEAKERS 
                    f3 = open('GOOD_SPEAKERS.txt', 'a')
                    #Cconcatenating spaeker is good with the name of the file that is being traversed
                    f3.write("\nSPEAKER IS GOOD:" + filename)
                    f3.close()
                  #breaking out of the loop if conditoned has been satisfied to avoid repetition of files in output file   
                break;
    if choice==2:
        path = input("ENTER FILE PATH:")
        for filename in os.listdir(path):
            f2 = open(filename, 'r')
            for line in f2:
                if "BAD" in line.split():
                    print_func(filename)
                    f4 = open('BAD_SPEAKERS.txt', 'a')
                    f4.write("\nSPEAKER IS NOT GOOD:" + filename)
                    f4.close()
                break;
    if choice==3:
        path = input("ENTER FILE PATH:")
        serial=input("ENTER SERIAL NUMBER OF SPEAKER:")
        for filename in os.listdir(path):
            f2 = open(filename, 'r')
            for line in f2:
                if serial in line.split():
                    print("SPEAKER FILE:" + filename)
                    print_func(filename)
                    f5 = open('OUTPUT4_SPEAKERS.txt', 'a')
                    f5.write("\nSPEAKER FILE NAME:" + filename)
                    f5.close()

    if choice==4:
        path = input("ENTER FILE PATH:")
        date=input("ENTER DATE TO SEARCH:")
        for filename in os.listdir(path):
            f2 = open(filename, 'r')
            for line in f2:
                if date in line.split():
                    print("SPEAKER FILE:"+ filename+" WITH DATE :"+date)
                    print_func(filename)
                    f6 = open('OUTPUT5_SPEAKERS.txt', 'a')
                    f6.write("\nSPEAKER FILE NAME:" + filename)
                    f6.close()
    if choice==5:
        exit=exit+1
        #exit(-1)



