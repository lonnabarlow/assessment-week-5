log_file = open("um-server-01.txt") 
# this is opening a file that and giving us access to data that we will use and adjust. We will be looping over the file. 


def sales_reports(log_file): #this is the loop over the file.
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon": #This us looping the file for the Monday orders.
            print(line)

sales_reports(log_file)
#returning the log file for Mondat the 19th.