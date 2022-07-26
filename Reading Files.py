# w - write, a - append (add new information to the end, r - read, r+ - read and write
employee_file = open("employee", "r")

# print(employee_file.readable()) # Gives boolean file, stating whether you can read it or not
# print(employee_file.readline()) # Reads the first line, if printed again, it would read the next line
# print(employee_file.readline()) # Reads the next line
# print(employee_file.read()) #reads the whole .txt
# print(employee_file.read()[1]) #reads the letter for index 1
# print(employee_file.readlines()[1]) #reads the line for index 1

# for employee in employee_file: #Loops through all the employees in the employee_file array
    # print(employee)
    
employee_file.close()
