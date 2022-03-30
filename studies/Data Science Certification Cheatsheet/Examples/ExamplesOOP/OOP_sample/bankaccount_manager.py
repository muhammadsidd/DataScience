#**Bank Account Manager** - Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. Manage credits and debits from these accounts through an ATM style program.
'''
Created on Jul 18, 2018

@author: SummitWorks
'''




class Account:
    def __init__(self, cust_id):
        self.cust_id = cust_id


class CheckingAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        Account.__init__(self, cust_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_whole = int(self.numstr[:self.numstr.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_part = int(self.numstr[self.numstr.find('.') + 1:])

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # debugging purposes only
        # print "self whole", self.amount_whole
        # print "self part", self.amount_part

        # separates the whole number from decimal number of the amount to withdraw
        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        numstr = str(withdraw_amount)
        self.withdraw_part = int(numstr[numstr.find('.') + 1:])

        # debugging purposes only
        # print "whole", self.withdraw_whole
        # print "part", self.withdraw_part

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal value of requested amount is greater than the
            # decimal value of the amount in the account, then 1 dollar is taken out
            # and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_whole) + "." + str(self.amount_part)

            # debugging purposes only
            # print "\nnew whole", self.amount_whole
            # print "new part", self.amount_part
            # print "new amount", new_amount

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount


class SavingsAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        Account.__init__(self, cust_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_whole = int(self.numstr[:self.numstr.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_part = int(self.numstr[self.numstr.find('.') + 1:])

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # debugging purposes only
        # print "self whole", self.amount_whole
        # print "self part", self.amount_part

        # separates the whole number from decimal number of the amount to withdraw
        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        numstr = str(withdraw_amount)
        self.withdraw_part = int(numstr[numstr.find('.') + 1:])

        # debugging purposes only
        # print "whole", self.withdraw_whole
        # print "part", self.withdraw_part

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal value of requested amount is greater than the
            # decimal value of the amount in the account, then 1 dollar is taken out
            #  and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_whole) + "." + str(self.amount_part)

            # debugging purposes only
            # print "\nnew whole", self.amount_whole
            # print "new part", self.amount_part
            # print "new amount", new_amount

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount


class BusinessAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        Account.__init__(self, cust_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_whole = int(self.numstr[:self.numstr.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_part = int(self.numstr[self.numstr.find('.') + 1:])

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # debugging purposes only
        # print "self whole", self.amount_whole
        # print "self part", self.amount_part

        # separates the whole number from decimal number of the amount to withdraw
        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        numstr = str(withdraw_amount)
        self.withdraw_part = int(numstr[numstr.find('.') + 1:])

        # debugging purposes only
        # print "whole", self.withdraw_whole
        # print "part", self.withdraw_part

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal value of requested amount is greater than the
            # decimal value of the amount in the account, then 1 dollar is taken out
            #  and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_whole) + "." + str(self.amount_part)

            # debugging purposes only
            # print "\nnew whole", self.amount_whole
            # print "new part", self.amount_part
            # print "new amount", new_amount

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount


if __name__ == '__main__':
    isSessionOn = True
    isCustomer = False

    def initialise_objects():
        global sally_checking, paolo_business, paolo_savings, master_list

        sally_checking = CheckingAccount(1, 2567.50)
        paolo_savings = SavingsAccount(2, 12890.01)
        paolo_business = BusinessAccount(2, 14500.40)

        master_list = [[sally_checking, 1, 1], [paolo_savings, 2, 2], [paolo_business, 2, 3]]

        return None

    initialise_objects()

    while isSessionOn is True:
        print("Welcome to 24-hour ATM service.")
        print("Insert your card.")

        # Card reading the customer info representation
        customerID = int(input("Enter your customer id number: "))
        print("\n")

        cust_accounts = []
        for i in master_list:
            if i[1] == customerID:
                cust_accounts.append(i[2])
                isCustomer = True

        if isCustomer is True:
            isAccountSelected = False

            while isAccountSelected is False:
                print("Enter 1 for checking account")
                print("Enter 2 for savings account")
                print("Enter 3 for business account")
                account_type = int(input("Enter which account to use: "))

                if account_type in cust_accounts:
                    for x in master_list:
                        if account_type == x[2]:
                            objectName = x[0]

                    isAccountSelected = True
                    isAccountSessionOn = True

                    while isAccountSessionOn is True:
                        print("\nHow may I help you?")
                        print("Press 1 for balance view.")
                        print("Press 2 for withdrawals")
                        print("Press 3 to exit.")

                        action_value = int(input("Please enter your choice: "))

                        if action_value == 1:
                            objectName.display_amount()
                            print("\n")

                        if action_value == 2:
                            amnt_to_withdraw = int(input("Enter the amount to withdraw: "))
                            #temp_str = str(amnt_to_withdraw)

                            adjusted_amount = "%.2f" % amnt_to_withdraw
                            # print "adjusted_amount:", adjusted_amount
                            objectName.withdraw(adjusted_amount)

                            print("current balance is", objectName.get_amount())
                            print("\n")

                        if action_value == 3:
                            isAccountSessionOn = False
                            print("Thank for using the 24-hour ATM service.")
                            print("Have a pleasant day.")
                            print("\n\n")
                            print("##########################################")
                else:
                    print("Error. You don't have that account.")
                    print("Please try again.\n")

        else:
            print("Cannot find your record.")
            print("Please get your card.")
            print("Exiting this session...")