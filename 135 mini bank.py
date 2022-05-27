#mini bank with constructor.....
import sys
class Bank:
    def __init__(self,a,b,c):
        self.account_no=a
        self.holder_name=b
        self.balance=c
    def show(self):
        print("A/c No.",self.account_no,' ',"A/h Name",self.holder_name,' ',"Balance",self.balance)
    def withdraw(self):
        amt=int(input("Enter amount to be withdraw:-"))
        if(self.balance-amt>1000):
            self.balance=self.balance-amt
            print(amt,"Amount Successfully withdrawled...")
        else:
            print("Insufficient Balance...")

    def deposit(self):
        amt=int(input("Enter amount to be deposite:-"))
        self.balance=self.balance+amt
        print(amt,"Amount Successfully deposited")

def main():
    bank_list=[]
    while (True):
        choice=int(input("1:Add Account\n2:Show Details\n3:Withdrawl\n4:Deposit\n"
                         "5:Exit\nEnter Your Choice..:-"))
        if (choice==1):
            for i in range(1):
                x=int(input("Enter Account No.:-"))
                y=str(input("Enter Account Holder name:-"))
                z=int(input("Enter Balance:"))
                b=Bank(x,y,z)
                bank_list.append(b)
        elif(choice==2):
            for data in bank_list:
                data.show()
        elif(choice==3):
            f=0
            n=int(input("Enter Account No. to Withdrawl Money:-"))
            for data in bank_list:
                if(n==data.account_no):
                    f=1
                    data.show()
                    data.withdraw()
                    break
            if(f==0):
                print("Account No. does not Exists....")
        elif(choice==4):
            f=0
            n=int(input("Enter Account no. to Deposit Money:-"))
            for data in bank_list:
                if(n==data.account_no):
                    f=1
                    data.deposit()
                    break
            if (f==0):
                print("Account No. does not Exists....")
        elif(choice==5):
            sys.exit()
        else:
            print("Wrong choice Enter....")
if __name__ == '__main__':
    main()
    #run




