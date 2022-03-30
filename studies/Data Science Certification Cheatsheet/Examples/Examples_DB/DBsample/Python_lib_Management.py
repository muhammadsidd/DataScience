'''
Created on Jan 25, 2018

@author: SummitWorks
'''
class Library:
    Librarians=[["Prashanth","1234"],["Swetha","4321"]]
    Students=[["RajaShekar","1111"],["Sandeep","2222"],["Manasa","3333"],["Manoj","4444"],["RamaKrishna","5555"],["Teja","6666"],["Bhavani","7777"],["Sandilya","9999"]]
    Rack_Book=[["Physics","Einstin","1000"],["Physics","Einstin","1001"],["Physics","Edison","1002"],["Physics","Einstin","1003"],["Physics","Einstin","1004"],\
      ["Chemistry","Einstin","2000"],["Chemistry","Thamos","2001"],["Chemistry","Einstin","2002"],["Chemistry","Nobel","2003"],["Chemistry","Einstin","2004"]]
    Dispatch_Book=[]
def Change_Login(self,name,pin):
    if [name,pin] not in lib.Librarians:
        Librarians=self.Librarians.append([name,pin])
        print("Successfully Changed login details")
    else:
        print("Entered same details only")
def Update_Book(self,name,author,Bid):
    if [name,author,Bid] not in lib.Rack_Book:

        Rack_Book=self.Rack_Book.append([name,author,Bid])
        #print(lib.Rack_Book)
        print("Update Successfully:",[name,author,Bid])
    else:
        print("Book already available with same details")
def Details_Books(self):
    print("--------------------------------------------------")
    print("Book name"," "*9,"Author Name"," "*9,"Book ID")
    print("--------------------------------------------------")


    for i in range(len(lib.Rack_Book)):
        print(lib.Rack_Book[i][0]," "*(20-len(lib.Rack_Book[i][0])),lib.Rack_Book[i][1]," "*(20-len(lib.Rack_Book[i][1])),lib.Rack_Book[i][2])
        print("___________________________________________________")

    print("\nNo of avaliable Books are:",len(lib.Rack_Book))

def Add_Students(self,name,pin):
    if [name,pin] not in lib.Students:
        Students=self.Students.append([name,pin])
        print("Successfully Added with details",[name,pin])
    else:
        print("Students already available with details") 
def Delete_Students(self,name,pin):
    if [name,pin] in lib.Students:
        Students=self.Students.remove([name,pin])
        print("Successfully deleted details",[name,pin])
    else:
        print("No students available with details")    
def Details_Students(self):
    print("-------------------------------")
    print("Sudent name"," "*9,"R.No")
    print("-------------------------------")

    for i in range(len(lib.Students)):
        print(lib.Students[i][0]," "*(20-len(lib.Students[i][0])),lib.Students[i][1])
        print("_______________________________")
    print("\nNo of Students are:",len(lib.Students))
def Collect_Books(self,name,author,Bid):
    if [name,author,Bid] in lib.Rack_Book:
        Dispatch_Book=self.Dispatch_Book.append([name,author,Bid])
        Rack_Book=self.Rack_Book.remove([name,author,Bid])
        print("Book collected succesfully:" ,[name,author,Bid])
    else:
        print("Enter details wrong:")    
def Return_Book(self,name,author,Bid):
    if [name,author,Bid] in lib.Dispatch_Book:
        Dispatch_Book=self.Dispatch_Book.remove([name,author,Bid])
        Rack_Book=lib.Rack_Book.append([name,author,Bid])
        print("Return Successfully:",[name,author,Bid])
    else:
        print("Enter details wrong:")


lib=Library()
print("Welcome to Library")
while(True):
    print('''Select your Option
 1:Librarian Login
 2:Student Login
 3:Exit''')

opt1=int(input("Please Enter your option:"))

if opt1==1:
    i=1
    while (i<4):
        usrlib=input("Please Enter your Name:")
        pinlib=input("Please Enter your Login PIN:")

        if [usrlib,pinlib] in lib.Librarians:
            print("Access Granted")
            i=5
            while(True):
                print('''Select your Option
                 0:Change Username or Password   
                 1:Add Books
                 2:Books Details
                 3:Add Students
                 4:Remove Students
                 5:Students details
                 6:Exit or Back''')
                opt2=int(input("Please Enter your option:"))
                if opt2==0:
                    usrlib1=input("Please Enter User Name to chane:")
                    pinlib2=input("Please Enter Login PIN to change:")
                    lib.Change_Login(usrlib1,pinlib2)

                elif opt2==1:
                    name=input("Please Enter your Book Name:")
                    author=input("Please Enter your Book Author:")
                    Bid=input("Please Enter your Book Id:")
                    lib.Update_Book(name.capitalize(),author.capitalize(),Bid)

                elif opt2==2:
                    lib.Details_Books()

                elif opt2==3:
                    name=input("Please Enter Student Name:")
                    pin=input("Please Enter Student R.No:")
                    lib.Add_Students(name.capitalize(),pin)
                elif opt2==4:
                    name=input("Please Enter Student Name:")
                    pin=input("Please Enter Student R.No:")
                    lib.Delete_Students(name.capitalize(),pin)    
                elif opt2==5:
                    lib.Details_Students()
                elif opt2==6:    
                    print("Back to Menu")
                    break
                else:
                    print("Wrong input")
                    continue


        else:
            print("Access Denied \nUser name or PIN Entered wrong")
            print("\nYou have more",(3-i),"attempts")
            i+=1
            if i==4:
                print("Failed login within 3 attempts")
elif opt1==2:
    i=1
    while (i<4):
        usrstd=input("Please Enter your Name:")
        pinstd=input("Please Enter your R.No:")

        if [usrstd,pinstd] in lib.Students:
            print("Access Granted")
            i=5
            while(True):
                print('''Select your Option
                     1:Collect Book
                     2:Return Books
                     3:Exit or Back
                     ''')
                opt2=int(input("Please Enter your option:"))
                if opt2==1:
                    print("Availablie Books are:\n")
                    lib.Details_Books()
                    name=input("Please Enter your Book Name:")
                    author=input("Please Enter your Book Author:")
                    Bid=input("Please Enter your Book Id:")
                    lib.Collect_Books(name.capitalize(),author.capitalize(),Bid)
                elif opt2==2:
                    name=input("Please Enter your Book Name:")
                    author=input("Please Enter your Book Author:")
                    Bid=input("Please Enter your Book Id:")
                    lib.Return_Book(name.capitalize(),author.capitalize(),Bid)
                elif opt2==3:
                    print("Back to Menu")
                    break

                else:
                    print("Wrong input")


        else:
            print("Access Denied \nUser name or PIN Entered wrong")
            print("\nYou have more",(3-i),"attempts")
            i+=1
            if i==4:
                print("Failed login within 3 attempts")

elif opt1==3:
    print("Exit Successfully")
    #break

else:
    print("Wrong input")