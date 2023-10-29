import sys

#We have created a class 'Contact' which consists of all the list for storing details & it also helps us to reduce duplication.
class Contact:
    #Function below contains all the required lists
    def __init__(self,Contact_Name,Contact_Id,Contact_Number):
        self.Contact_Name = Contact_Name
        self.Contact_Id = Contact_Id
        self.Contact_Number = Contact_Number

    def __str__(self):
        Info = self.Contact_Name + ","
        Info += self.Contact_Id + ","
        Info += self.Contact_Number + ""
        return Info

#Class 'TelephoneDirectory' contains all the required code for operating Telephone Directory.
class ContactManager:

    #Function read_stripped_str is created for stripped inputs, it will also help us to reduce duplication.
    def read_stripped_str(self,prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        entered_stripped_str = sys.stdin.readline().strip()
        return entered_stripped_str

    #Function  read_stripped_non_empty_str is created for stripped input and we are also checking that input should not be empty.
    def read_stripped_non_empty_str(self,prompt):
        entered_stripped_non_empty_str = self.read_stripped_str(prompt)
        while( len(entered_stripped_non_empty_str) == 0 ):
            entered_stripped_non_empty_str = self.read_stripped_str("Input Cannot Be Empty! " + prompt)
        return entered_stripped_non_empty_str

    #Function read_int is created for inputs of numbers, it will also help us to reduce duplicstion.
    def read_int(self,prompt):
        entered_int = int( self.read_stripped_non_empty_str(prompt) )
        return entered_int


    #In the function __init__,we have created a single list for all the details. 
    def __init__(self):
        Contacts = []
        self.Contacts = Contacts
        
        

        Menu_Choice = ""
        while(Menu_Choice!= "X"):
            Menu="\n"
            Menu+="===================" '\n' #Main Menu
            Menu+="Telephone Directory" '\n'
            Menu+="===================" '\n'
            Menu+="[A]dd Contact Details" '\n'
            Menu+="[S]earch Contact Details" '\n'
            Menu+="[L]oad a file" '\n'
            Menu+="E[x]it" '\n'
            Menu+='\n'
            Menu+="Enter Your Choice: "#Choice

            Menu_Choice = self.read_stripped_str(Menu).upper()#Menu_Choice

            #The if statements below are used to check and perform operations
            #based on what the user has selected from the menu.
            if (Menu_Choice == "S"): #Search Contact Details            
                sys.stdout.write("============================================" '\n')
                sys.stdout.write("Search Contact Details - Telephone Directory" '\n')
                sys.stdout.write("============================================" '\n')
                
                #name_search is used to search the contact according to user's choice from the other added contacts.
                name_search = self.read_stripped_str("Enter a name to search: ")

                sys.stdout.write("S.No." + "\t\t")
                sys.stdout.write("Name " +"\t\t")
                sys.stdout.write("Id " + "\t\t")
                sys.stdout.write("Number " + "\n")
                
                num_search_results = 0
                i=0
                while(i<len(Contacts)):
                    if (name_search.upper() in Contacts[i].Contact_Name.upper() ):
                        Contact_Name = Contacts[i].Contact_Name
                        Contact_Id = Contacts[i].Contact_Id
                        Contact_Number = Contacts[i].Contact_Number
                        
                        sys.stdout.write(str(i+1)+ ". "+ "\t\t")
                        sys.stdout.write(Contacts[i].Contact_Name + "\t\t")
                        sys.stdout.write(Contacts[i].Contact_Id + "\t\t")
                        sys.stdout.write(Contacts[i].Contact_Number + "\n")
                        num_search_results+=1
                    i+=1
                    
                if (num_search_results == 0):
                    sys.stdout.write("No matches for: \"" + name_search + "\"\n")

                else:
                    search_sub_menu_choice_record_number = self.read_int("Enter contact record number: ")-1
                    
                    search_sub_menu_operation="[E]dit" '\n'
                    search_sub_menu_operation+="[R]emove" '\n'
                    search_sub_menu_operation+="Any other key to go back to the Main Menu: "
                    search_sub_menu_choice_operation = self.read_stripped_str(search_sub_menu_operation).upper()

                    if (search_sub_menu_choice_operation == "E"):
                        sys.stdout.write('\n' + "Entering contact " + str(search_sub_menu_choice_record_number+1) + " details.." '\n')

                        #The loop is needed to validate the contact name to ensure it is not blank.
                        #The length of the input is checked based on the stripped input so that
                        #white spaces are excluded from the length calculation. Alternatively, we can also
                        #compare against an empty string "".
                        Contact_Name = self.read_stripped_non_empty_str("Contact Name: ")

                        #The Contact_Id is checked to see if it is empty using the same criteria used for
                        #the Contact_Name above. We are also checking to see if the contact id starts with
                        #an uppercase R. Alternatively, the contact id input can be converted to uppercase
                        #at the time of taking input so the check for starting with a "R" becomes case
                        #insensitive.
                        Contact_Id = self.read_stripped_non_empty_str("Contact Id: ").upper()
                        while ( Contact_Id[0] != "R"):
                            Contact_Id = self.read_stripped_non_empty_str("Invalid!, Id must start with R: ")

                        #The Contact_Number is checked to see if it is empty using the same criteria used for
                        #the Contact_Name above.
                        Contact_Number = self.read_stripped_non_empty_str("Contact Number: ")
                        while ( len(Contact_Number[0]) == 0):
                            Contact_Number = self.read_stripped_non_empty_str("Inavlid!, Re-enter Number: ")

                        
                        Contacts[search_sub_menu_choice_record_number].Contact_Name = Contact_Name
                        Contacts[search_sub_menu_choice_record_number].Contact_Id = Contact_Id
                        Contacts[search_sub_menu_choice_record_number].Contact_Number = Contact_Number
                            
                    elif (search_sub_menu_choice_operation == "R"):
                        del(Contacts[search_sub_menu_choice_record_number])

            #This choice is for adding contact details.        
            elif (Menu_Choice == "A"):         
                sys.stdout.write("=================================" '\n')
                sys.stdout.write("Add Contact - Telephone Directory" '\n')
                sys.stdout.write("=================================" '\n')

                sys.stdout.write("How many contacts would you like to add? ")
                sys.stdout.flush()
                Max_Num_Contacts = int( sys.stdin.readline().strip() )

                #The looop must repeat Max_Num_contacts times. An alternative is to start
                #counting from Max_Num_Contacts and to count down instead. However, as
                #we might need to use Max_Num_Contacts later, a separate counter 'a' is used.
                #Also, the separate counter 'a' allows us to show which contact is currently
                #being created.
                a=0
                while (a<Max_Num_Contacts):
                    sys.stdout.write( '\n' + "Entering Contact " + str(a+1) + " details..." '\n')

                    sys.stdout.write("Enter Contact Name: ")
                    sys.stdout.flush()
                    Contact_Name = sys.stdin.readline().strip()
                    #The loop is needed to validate the contact name to ensure it is not blank
                    #The length of the input is checked based on the stripped input so that
                    #white spaces (tabs, space characters, new lines, etc.) are excluded from the
                    #length calculation. Alternatively, we can also compare against an empty string "".
                    while( len(Contact_Name) ==0 ):
                        sys.stdout.write("Invalid; Re-enter name: ")
                        sys.stdout.flush()
                        Contact_Name = sys.stdin.readline().strip()


                    sys.stdout.write("Enter Contact Id: ")
                    sys.stdout.flush()
                    Contact_Id = sys.stdin.readline().strip().upper()
                    #The Contact_Id is checked to see if it is empty using the same criteria used for 
                    #the Contact_Name above. We are also checking to see if the contact id starts with
                    #an uppercase R. Alternatively, the Contact_Id input can be converted with a "R" becomes case
                    #insensitive.
                    while( len(Contact_Id) == 0 or Contact_Id[0] != "C"):
                        sys.stdout.write("Invalid; Re-enter Id, Contact Id should start with C: ")
                        sys.stdout.flush()
                        Contact_Id = sys.stdin.readline().strip().upper()


                    sys.stdout.write("Enter Contact Number: ")
                    sys.stdout.flush()
                    Contact_Number = sys.stdin.readline().strip()
                    #The Contact_Number is checked to see if it is empty using the same criteria used for
                    #the Contact_Name above.
                    while( len(Contact_Number) == 0):               
                       sys.stdout.write("Invalid; Re-enter Contact Number: ")
                       sys.stdout.flush()
                       Contact_Number = sys.stdin.readline().strip()
                   
                    #A new variable 'All_New_Contacts' is created which helps us to append all the contact details easily without so many lines of code,
                    #it also helps us to reduce duplication.
                    All_New_Contacts = Contact(Contact_Name,Contact_Id,Contact_Number)
                    Contacts.append( All_New_Contacts )
             
                    a=a+1 # Alternatively, a+=1
                    #add_sub_menu_choice is created so that a user wants to save there details in a file then they can.
                add_sub_menu_choice = self.read_stripped_str("Do you want to [S]ave these details(or press any other key to go back to main menu): ").upper()
                if (add_sub_menu_choice == "S"):
                    File_Name = self.read_stripped_str("Enter name of the file in which you want to save these details: ")
                    Write_File = open(File_Name,"w")
                    i=0
                    while(i<len(self.Contacts)):
                        Write_File.write(str(self.Contacts[i]) + "\n")
                        i+=1
                    Write_File.close()

            elif (Menu_Choice == "L"):
                File_Name = self.read_stripped_str("Enter name of the file: ")
                Load_File = open(File_Name,"r")

                User_Entry = Load_File.readline()
                while(len(User_Entry)>0):
                    Details_Sections = User_Entry.split(",")
                    Name = Details_Sections[0]
                    Id = Details_Sections[1]
                    Num = Details_Sections[2]

                    sys.stdout.write("\n")
                    sys.stdout.write("Contact_Name: " + Name + "\n")
                    sys.stdout.write("Contact_Id: " + Id + "\n")
                    sys.stdout.write("Contact_Number: " + Num + "\n")
                    sys.stdout.write("\n")


                    User_Entry = Load_File.readline()

                Load_File.close()

ContactManager()
