import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="tiger",database="library")


 
def addbook():
       bn=input("Enter BOOK Name:")
       c=input("Enter BOOK Code:")
       t=input("Total Books:")
       s=input("Enter Subject:")
       data=(bn,c,t,s)
       sql='insert into books values(%s,%s,%s,%s)'
       c=con.cursor()
       c.execute(sql,data)
       con.commit()
       print("Data Entry:...")
       print("Data Entered Successfully")
       main()

def issueb():
       n=input("Enter Name:")
       r=input("Enter Reg No:")
       co=input("Enter BOOK Code:")
       d=input("Enter date:")
       data=(n,r,co,d)
       a="insert into issue values(%s,%s,%s,%s)"
       c=con.cursor()
       c.execute(a,data)
       con.commit()
       print("Issuing book...")
       print("Book Issued to:-",n)
       bookup(co,-1)



def submitb():
       n=input("Enter BOOK Name:")
       r=input("Enter Reg No:")
       co=input("Enter BOOK Code:")
       d=input("Enter date:")
       a='insert into submit values(%s,%s,%s,%s)'
       data=(n,r,co,d)
       c=con.cursor()
       c.execute(a,data)
       con.commit()
       print("Book Submitted...")
       bookup(co,1)
       
def bookup(co,u):
       a="select TOTAL from books where BCODE=%s"
       data=(co,)
       c=con.cursor()
       c.execute(a,data)
       myresult=c.fetchone()
       t=myresult[0]+u
       sql="update books set TOTAL=%s where BCODE=%s"
       d=(t,co)
       c.execute(sql,d)
       con.commit()
       main()

def dbook():
       ac=input("Enter Book Code:")
       a="delete from books where BCODE=%s"
       data=(ac,)
       c=con.cursor()
       c.execute(a,data)
       con.commit()
       main()

def dispbook():
       a="select * from books"
       c=con.cursor()
       c.execute(a)
       myresult=c.fetchall()
       for i in myresult:
              print("Book Name:",i[0])
              print("Book Code:",i[1])
              print("Total:",i[2])
              print("Books: ")
       main()


def main():
    print("Choose what you want to do: \n1. Add Book\n2. Issue Book\n3. Submit Book\n4. Delete Book\n5. Display Book")
    ch=input("Enter Choices from above:")
    if  (ch=='1'):
            addbook()
    elif(ch=='2'):
            issueb()
    elif(ch=='3'):
            submitb()
    elif(ch=='4'):
            dbook()
    elif(ch=='5'):
            dispbook()
    else:
          print("Wrong Choice!!!")
          main()
          

def pswd():
    ps=input("Enter Password: ")
    if ps=="simsim":
            main()
    else:
            print("Wrong ")
            pswd()
pswd()
