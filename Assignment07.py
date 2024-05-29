# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment focusing on using Constructor, Properties, Inheritance to enhance
#       the functionality of class
# Change Log: (Who, When, What)
#   Minghsuan Liu,5/27/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json
from io import TextIOWrapper
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
Please Select:'''

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"




class Person:
    ''' Person Class
    1. Create a Person Class
    2. Add first_name and last_name properties to the constructor\n 
    3. Create a getter and setter for the first_name property\n 
    4. Create a getter and setter for the last_name property\n 
    5. Override the __str__() method to return Person data\n 
    '''

    first_nae: str = ""
    last_name: str = ""
    
    
    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name  
    
    @property
    def first_name(self):
        return self.__first_name.title()
    
    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha():
            self.__first_name = value
        elif value == "":
             raise ValueError("First Name can't be Empty input")
        else:
            raise ValueError("The First Name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()
    
    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha():
            self.__last_name = value
        elif value == "":
            raise ValueError("Last Name can't be Empty input")
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return (f'{self.first_name},{self.last_name}')
    


class Student(Person):
    ''' Student Class 
    1. Create a Student class the inherits from the Person class \n
    2. call to the Person constructor and pass it the first_name and last_name data\n
    3. add a assignment to the course_name property using the course_name parameter\n
    4. add the getter for course_name\n
    5. add the setter for course_name\n
    6. Override the __str__() method to return the Student data\n
    '''
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name= first_name, last_name= last_name)
        
        self.course_name= course_name
    
    @property
    def course_name(self):
        return self.__course_name.title()
    
    @course_name.setter
    def course_name(self, value: str):
        if value == "":
            raise ValueError("The course name can't be empty.")
            
        else:
            self.__course_name = value

    def __str__(self):
        return (f'{super().__str__()},{self.course_name}')


# Define the Data Variables and constants

menu_choice: str = ""
file: TextIOWrapper = None  
students: list = []




class FileProcessor:
    ''' FileProcessor Class\n
    1. read_file method: read info from file and convert to Student Class. Add Try/except for instruct error\n
    2. write_file method: convert info from list of Student objects to dictionary. Write dictionary to json file
    '''
    @staticmethod
    def read_file(file_name: str,  student_data: list):
        try: 
            json_data=[]
            file= open(file_name,'r')
            

            try:
                json_data = json.load(file)
                if not json_data:
                    raise Exception("No Content in the file")
                else:
                    for line in json_data:
                        student_data.append(Student(line["FirstName"],
                                            line["LastName"],
                                            line["CourseName"]))
                                                 
            except Exception as e:
                print("Please add initial content in the file")
       
            file.close()

        except FileNotFoundError as e:
            IO.output_error_message("File doesn't exist!",e)
            IO.output_error_message("Try to create a file")
        except json.JSONDecodeError as e:
            IO.output_error_message("JSON data in file isn\'t valide",e)
            IO.output_error_message("Resetting JSON file")
        except Exception as e:
            IO.output_error_message("There was an error open the document",e)
            IO.output_error_message("Unhandled exception")
        
        
        return student_data

    @staticmethod
    def write_file(file_name: str, student_data: list):
        try: 
            json_data=[]
            file= open(file_name,'w')
            
            for line in student_data:
                json_data.append({"FirstName":line.first_name,"LastName":line.last_name,"CourseName":line.course_name})

            json.dump(json_data,file,indent=2)
            print("Your Info is registered in the system\n")
                
            file.close()
    
        except FileNotFoundError as e:
            IO.output_error_message("File doesn't exist!",e)
            IO.output_error_message("Try to create a file")
        except json.JSONDecodeError as e:
            IO.output_error_message("JSON data in file isn\'t valide",e)
            IO.output_error_message("Resetting JSON file")
        except Exception as e:
            IO.output_error_message("There was an error open the document",e)
            IO.output_error_message("Unhandled exception")
        
        


class IO:
    '''
    methods
    1. output_error_message: handle File Processor\n
    2. menu_option: display menu and get input (needs to be 1~4 range)\n
    3. input_data: ask for first/last/course name and append to original data structure\n
    4. print data: print out existed and new add data\n
    '''
    @staticmethod
    def output_error_message(message: str, exception: Exception = None):
        print(message)
        if exception is not None:
            print(exception,exception.__doc__,type(exception),sep='\n')
    
    @staticmethod
    def user_choice(menu: str):
        menu_choice = input(menu)
        while menu_choice not in ["1","2","3","4"]:
            IO.output_error_message("\"Please enter between 1~4\"")
            input("Press \"Enter\" to continue...")
            menu_choice = input(menu)
            
        return menu_choice
        
    @staticmethod
    def input_data(student_data: list):
        first_name: str = '' 
        last_name: str = ''  
        course_name: str = ''  
        #input_info
        while True:
            try:
                
                first_name = input("Please Enter Student's First Name: ")
                last_name = input("Please Enter Student's Last Name: ")
                
                if not first_name.isalpha() or not last_name.isalpha():
                    raise ValueError("Name can only have alphabetic characters!")
                course_name = input("Please Enter Course Name: ")
                input_info = Student(first_name,
                                     last_name,
                                     course_name)
                student_data.append(input_info)
                input("Press \"Enter\" to continue...")
                return student_data
                
            except ValueError as e:
                IO.output_error_message("User Entered invalid information! ")
    
    @staticmethod
    def print_data(student_data: list):
        for line in student_data:
            print(f'{line.first_name} {line.last_name} is registered for course {line.course_name}\n')
        
        input("Press \"Enter\" to continue...")


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file


students = FileProcessor.read_file(FILE_NAME, students)

while students:
    menu_choice = IO.user_choice(MENU)
    if menu_choice =="1":
        IO.input_data(students)
    elif menu_choice == "2":
        IO.print_data(students)
    elif menu_choice == "3":
        FileProcessor.write_file(FILE_NAME, students)
    elif menu_choice == "4":
        break
