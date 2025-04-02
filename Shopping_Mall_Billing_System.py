import random
import mysql.connector
try:
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Shopping"
       )
    if connection.is_connected():
        mycursor=connection.cursor()
    else:
        print("Connection Error...Kindly check")
except:
    print("Database Error....")

def C_Product():
    try:
        mycursor.execute('''create table Product (P_id int primary key,
        p_name varchar(30), p_category varchar(30), un_price float, Qnt int, discount int)''')
    except Exception as e:
        print("Error....",e)
    

def C_Customer():
    try:
        mycursor.execute('''create table Customer (cust_id varchar(20) primary key,
        F_Name varchar(30),L_Name varchar(40),Location varchar(40),Mob_No varchar(30))''')
    except Exception as e:
        print("Error....",e)



def load_tables():
    try:
        mycursor.execute("show tables")
        data=mycursor.fetchall()
        for i in data:
            if i[0]!="Customer":
                C_Customer()
        for i in data:
            if i[0]!="Product":
                C_Product()
    except Exception as e:
        print("Error....",e)



def view_products():
    try:
        print('='*90)
        print("\t\t\t\tAVAILABLE STOCKS")
        print('='*90)
        print("*"*90)
        mycursor.execute("select * from Product")
        data=mycursor.fetchall()
        print("*","\tP_id\t","P_Name\t\t","P_category\t","Unit_Price\t","Qnt\t","Discount"," "*6,"*")
        for i in data:
            print("*\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4],"\t",i[5]," "*12,"*")
        print("*"*90)
    except Exception as e:
        print("Error....",e)

def view_customer():
    try:
        print('='*90)
        print("\t\t\t\tREGISTERED CUSTOMERS")
        print('='*90)
        mycursor.execute("select * from customer")
        data=mycursor.fetchall()
        print("*"*90)
        print("*","Cust_Id\t","First_Name\t","\tLast_Name\t","Location\t","Mobile_No"," "*5,"*")
        for i in data:
            print("*",i[0],"\t",i[1],"\t\t",i[2],"\t\t",i[3],"\t\t",i[4]," "*4,"*")
        print("*"*90)
    except Exception as e:
        print("Error....",e)
    
    

def Add_P():
    try:
        print('='*90)
        print("\t\t\t\tADD PRODUCT")
        print('='*90)
        print("*"*90)
        while True:
            p_id=int(input("Enter Product Id:"))
            p_name=input("Enter Product Name:")
            p_category=input("Enter Product Category:")
            un_price=float(input("Enter Unit Price:"))
            Qnt=int(input("Enter Quantity:"))
            dis=int(input("Enter discount(%) on Product:"))
            mycursor.execute('''insert into product values (
             {},"{}","{}",{},{},{})'''.format(p_id,p_name,p_category,un_price,Qnt,dis))
            connection.commit()
            print("*"*90)
            print("Product with id {} is Successfully Added".format(p_id))
            ch=input("Want to Add More Products(Y/N):")
            if ch in 'nN':
                break
    except Exception as e:
        print("Error....",e)

def Remove_P():
    try:
        print('='*90)
        print("\t\t\t\tRemove PRODUCT")
        print('='*90)
        print("*"*90)
        while True:
            p_id=int(input("Enter Product id:"))
            mycursor.execute("Delete from Product where P_id= {}".format(p_id))
            print("*"*90)
            print("Product with id {} is Successfully Removed".format(p_id))
            ch=input("Want to Remove More Products(Y?N):")
            if ch in 'nN':
                break
    except Exception as e:
        print("Error....",e)

def Modify_P():
    try:
        print('='*90)
        print("\t\t\t\tMODIFY PRODUCTS")
        print('='*90)
        while True:
            print("\t\t1.Change Product's Name")
            print("\t\t2.Change Product's Quantity")
            print("\t\t3.Change Product's Category")
            print("\t\t4.Change Product's Unit Price")
            print("\t\t5.Exit")

            ch=input("Enter Your choice(1-6):")
            if ch not in '123456':
                print("\tPlz Enter Numbers Only...")
            elif ch=='1':
                try:
                    print("*"*90)
                    p_id=input("Enter P_id:")
                    N_Name=input("Enter New Name:")
                    mycursor.execute("update Product set p_name= '{}' where P_id= '{}'".format(N_Name,p_id))
                    connection.commit()
                    print("Name Changed Successfully...")
                    print("*"*90)
                    print("\n")
                except Exception as e:
                    print("Error....",e)
                
            elif ch=='2':
                try:
                    print("*"*90)
                    p_id=input("Enter P_id:")
                    Quantity=input("Enter Product' Quantity:")
                    mycursor.execute("update Product set Qnt= {} where P_id= '{}'".format(Quantity,p_id))
                    connection.commit()
                    print("*"*90)
                    print("Quantity Changed Successfully...")
                    print("\n")
                except Exception as e:
                    print("Error....",e)

            elif ch=='3':
                try:
                    print("*"*90)
                    p_id=input("Enter P_id:")
                    category=input("Enter Product' Category:")
                    mycursor.execute("update Product set p_category= '{}' where P_id= '{}'".format(category,p_id))
                    connection.commit()
                    print("*"*90)
                    print("Category Changed Successfully...")
                    print("\n")
                except Exception as e:
                    print("Error....",e)
            elif ch=='4':
                try:
                    print("*"*90)
                    p_id=input("Enter P_id:")
                    unprice=input("Enter Unit Price:")
                    mycursor.execute("update Product set un_price= '{}' where P_id= '{}'".format(unprice,p_id))
                    connection.commit()
                    print("*"*90)
                    print("Unit Price Changed Successfully...")
                    print("\n")
                except Exception as e:
                    print("Error....",e)   
            elif ch=='5':
                break

    except Exception as e:
        print("Error....",e)
            
            
            
        

  
def Editor():
    try:
        while True:
            pas=input("Enter Your Password:")
            if pas.lower()!='rj9884':
                print("Wrong Password")
            else: break
        while True:
            print('='*90)
            print("\t\t\t\tEDIT MENU")
            print('='*90)
            print("\t\t\t\t1.Add Product")
            print("\t\t\t\t2.Remove Product")
            print("\t\t\t\t3.Modify Product")
            print("\t\t\t\t4.Customer Details")
            print("\t\t\t\t5.Main Menu")
           
            ch=input("Enter Your choice(1-5):")
            if ch not in '12345':
                print("Plz Enter Numbers Only...")
            elif ch=='1':
                Add_P()
            elif ch=='2':
                Remove_P()
            elif ch=='3':
                Modify_P()
            elif ch=='4': 
                view_customer()
            else: break
    except Exception as e:
        print("Error....",e)



def cust_id_generetor():
    try:
        print("*"*90)
        F_name = input("Enter your First name:")
        L_name = input("Enter your Last name:")
        Location= input("Enter Your City:")
        while True:
            mobile =input("Enter your mobile number:")
            if len(mobile)!=10:
                print("Invalid Mobile Number..Enter 10 digits only")
            else: break
        cust_id=F_name[:1] + L_name[:1] + str(mobile[6:11])
        print("Your Customer ID is: ",cust_id)
        print("*"*90)
        return cust_id,F_name,L_name,Location,mobile
    except Exception as e:
        print("Error....",e)

def cust_id_exist():
    try:
        print("*"*90)
        mycursor.execute("select cust_id from customer")
        result=mycursor.fetchall()
        global cust_id
        cust_id=input("Enter Your Customer id:")
        Lower=cust_id.lower()
        final=0
        for i in result:
            if i[0].lower()==Lower:
                print("Welcome back, your customer ID is:", cust_id)
                print("*"*90)
                final=1
        if final==0:
            print("Customer id does not exist...kindly register...")
            registor()
    except Exception as e:
        print("Error....",e)
def registor():
    try:
        print("Start Your Registration...")
        cust_id,F_name,L_name,Location,mobile=cust_id_generetor()
        mycursor.execute('''insert into customer (cust_id,F_name,L_name,Location,mob_no)
        values ("{}","{}","{}","{}","{}")'''.format(cust_id,F_name,L_name,Location,mobile))
        connection.commit()
        print("Sign up successful! Your customer ID is:", cust_id)
        print("*"*90)
    except Exception as e:
        print("Error....",e)
    
        
        

def customers():
    try:
        print('='*90)
        print("\t\t\t\tCUSTOMER DETAILS")
        print('='*90)
        ask=input("Do you have the Customer_id(Y/N):")
        if ask in "Yy":
            cust_id_exist()
            shopping=input("Do you want to shop now(Y/N):")
            if shopping in "yY":
                purchase()
        if ask in "Nn":
            registor()     
    except Exception as e:
        print("Error....",e)



    

def purchase():
    try:
        view_products()
        cust_id_exist()
        while True:
            print('='*90)
            print("\t\t\t\tPURCHASE")
            print('='*90)
            print("\t\t\t\t1.Place Your Order")
            print("\t\t\t\t2.Main Menu")
            ch=input("Enter Your Choice(1-2):")
            if ch not in '12':
                print("Plz Enter Numbers Only...")
            elif ch=='1':
                buyprod()
            elif ch=='2':
                break
            
    except Exception as e:
        print("Error....",e)

from datetime import*
def buyprod():
    try:
        print("*"*90)
        a=random.randint(100000,999999)
        global table_name,prod_quant,price
        table_name=cust_id+'PLASSIO'
        def Bill_Table():
            try:
                mycursor.execute(f'''create table {table_name}
                (prod_name varchar(20),prod_quant int,Discount_Percentage int,price int)''')
            except Exception as e:
                print("Error....",e)
        Bill_Table()

        while True:
            Id=input("Enter the Id of the product:")
            mycursor.execute(f"select p_name from product where p_id ='{Id}'")
            result4=mycursor.fetchone()
            prod_name=result4[0]
       
     
            #To check availability of the product
            prod_quant=int(input("Enter the quantity of the product:"))
            mycursor.execute(f"select Qnt from product where p_name = '{prod_name}'")
            result=mycursor.fetchone()
   
       
            if result[0]>=prod_quant:
           
       
                #fetching the price of the product
                mycursor.execute(f"select un_price from product where p_name='{prod_name}'")
                result=mycursor.fetchone()
                price=result[0]
           
        
                #Applying the discount on the product
                mycursor.execute(f"select discount from product where p_name = '{prod_name}'")
                result2=mycursor.fetchone()
                discount=result2[0]
                netper=100-discount
           
                #Creating the Bill Table
                
                total_price=((prod_quant*price)*netper)/100
                #Inserting the Data in Bill Table
                mycursor.execute(f"insert into {table_name} values('{prod_name}',{prod_quant},{discount},{total_price})")
                connection.commit()
               #Updating the new quantity of the Product
           
                mycursor.execute(f"select Qnt from product where P_id = '{Id}'")
                result=mycursor.fetchone()
                newQuant=int(result[0])-prod_quant
                mycursor.execute(f"UPDATE product SET Qnt = {newQuant} WHERE P_id = '{Id}'")
                connection.commit()
                print("*"*90)
                choice=input('\nPress Y for continue purchasing and N for quit shopping:')
                #Generating the bill
                if choice in 'Nn':
                    print('\t\t\t\tYour bill is generated\n\n')
                    mycursor.execute(f"select sum(price) from {table_name}")
                    result1=mycursor.fetchone()
                    print("*"*90)
                    print("\t\t\tTHE GREAT INDIAN MALL \n \t\t\tINDIRA NAGAR LUCKNOW ")
                    print("\t\t#Favourite Brands And Hottest Trends #")
                    print("*"*90)
                    print("\t\t\tINVOICE NO:",a)
                    today = date.today()
                    d1 = today.strftime("%d/%m/%Y")
                    now = datetime.now()
                    a = now.strftime("%H:%M:%S")
                    print( d1,"\t\t\t\t\t\t\t",a)
                    print("*"*90)          
                    mycursor.execute("SELECT CUST_ID,F_NAME,L_NAME,LOCATION,MOB_NO FROM CUSTOMER where CUST_ID='{cust_id}'")
                    data = mycursor.fetchall()            
                    for i in data:
                        print("    ","CUSTOMER_ID:",i[0],"\t")
                        print("    ","CUSTOMER_NAME:",i[1],i[2],"\t")
                        print("    ","ADDRESS:",i[2],"\t")
                        print("    ","PHONE_NO:",i[3],"\t")
                    mycursor.execute(f'select* from {table_name}')
                    myresult=mycursor.fetchall()
                    print("*","\tP_Name\t\t","Quantity\t","Discount%\t","Total Price"," "*19,"*")
                    for i in myresult:
                        print("*","\t",i[0],"\t",i[1],"\t\t",i[2],"\t\t",i[3]," "*27,"*")
                    print("*"*90)
                    print(" "*69,"Grand Total:",result1[0])
                    print("*"*90)
                    print("THE GREAT INDIAN MALL")
                    print("INDIRA NAGAR LUCKNOW")
                    print("011915221234567")
                    print("thegreatindianmall@gmail.com")
                    print("*"*90)
                    print("\t\t\t THANK YOU!!")
                    print("\t\t\t SEE YOU SOON ☺")
                    print("*"*90)
                    break       
            else:
                print("Product out of stock")
                print("*"*90)
                X=input('Press Y To Continue purchasing:')
                z='yY'
                if X not in z:
                    break
        mycursor.execute(f'drop table {table_name}')
    except Exception as e:
        print("Error....",e)
        mycursor.execute(f'drop table {table_name}')
  


    
#load_tables()  
while True:
    print("\n")
    print("❤"*52)
    print("\t\t\t\tTHE GREAT INDIAN MALL")
    print("\t\t\t\tINDIRA NAGAR LUCKNOW")
    print('='*90)
    print("\t\t\t\tMAIN MENU")
    print('='*90)
    print("\t\t\t\t1.VIEW PRODUCTS")
    print("\t\t\t\t2.CUSTOMER MENU")
    print("\t\t\t\t3.PURCHASE MENU")
    print("\t\t\t\t4.EDITOR MENU")
    print("\t\t\t\t5.EXIT")
    print('='*90)

    ch=input("Enter Task No: ")
    print("❤"*52)
    if ch not in '12345':
        print("\tPlz Enter Numbers Only...")
    elif ch=='1':
        view_products()
    elif ch=='2':
        customers()
    elif ch=='3':
        purchase()
    elif ch=='4':
        Editor()
    elif ch=='5':
        break
