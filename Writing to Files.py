employee_file = open("employee", "w") # if you give the file a name that doesn't exist, it'll make a new txt file

#employee_file.write("Toby - Human Resources") #adds this to the end of the text
#employee_file.write("\nKelly - Customer Service") # "\n" adds new line when adding to the text AND overwrites ".write"
employee_file.write("<p>This is HTML </p>") # Adds html variables

employee_file.close()
