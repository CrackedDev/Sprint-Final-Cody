# Sprint week Project 1
# One Stop Insurance Company
# Author: Cody Barrett
# Date: 12/07/2021

# Function Definitions:

def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z"
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True


def As_Dollars_Pad(Number):
    """Format Dollars amounts to strings & Pad Right 10 Spaces"""
    Number_Display = f"${Number:,.2f}"
    Number_Display = f"{Number_Display:>10}"
    return Number_Display


def Write(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with ,"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')},")
        else:
            Variable = round(Variable, 2)
            return f.write(f"{str(Variable)},")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)},")

def Write_Space(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with Space"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            Variable = round(Variable, 2)
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")

def Monthly_Start(Today):
    """Function design for next month payments that start at the beginning of the month.
    If the date is > than the 25th of the month it skips to the next month.
    IE: 25th of December would have a First payment Feb 1st. Less than the 25th day would be Jan 1st"""
    Day = Today.day
    # Code is written to add so many days to get to next month then replaces that day with the first day of the month
    if Day >= 25:
        Next_Month = (Today + datetime.timedelta(days=45)).replace(day=1)
    elif Day < 25:
        Next_Month = (Today + datetime.timedelta(days=32)).replace(day=1)
    return Next_Month.strftime('%d-%m-%Y')

# Program Start

while True:
    print("One Stop Insurance Company")
    print("'For Life's unexpected, Stops...'")
    print("--------------------------------")
    print()

    # Customer Info Inputs:
    while True:
        CustFirstName = input("Enter Customer First Name: ")
        if CustFirstName == "":
            print("First Name cannot be blank: Please Re-Enter")
        elif Name_Validation(CustFirstName) == False:
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') No Spaces")
        else:
            break

    while True:
        CustLastName = input("Enter Customer Last Name: ")
        if CustLastName == "":
            print("Last Name cannot be blank: Please Re-Enter")
        elif Name_Validation(CustLastName) == False:
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') No Spaces")
        else:
            break

    Address = input("Enter Street Address: ")
    City = input("Enter City: ")
    Province = input("Enter Province (XX): ")
    PostalCode = input("Enter Postal Code (X#X #X#): ")
    while True:
        Phone = input("Enter Phone Number: (##########)")
        if len(Phone) != 10:
            print("Invalid phone number. Must equal 10 digits!")
        elif Phone.isdigit() == False:
            print("Invalid phone number. Must equal 10 digits!")
        else:
            break
    PhonePad = "(" + Phone[0:3] + ") " + Phone[3:6] + "-" + Phone[6:10]

    # Claim Information:
    while True:
        NumCars = int(input("Enter the number of Cars to be Insured: "))
        if NumCars < 1:
            print("Number of insured cars must be greater than 0!")
        elif NumCars == "":
            print("Number of Cars cannot be blank!")
        else:
            break

    while True:
        ExtraLiab = input("Add extra Liability? (Y/N): ")
        if ExtraLiab == "":
            print("Cannot be Blank! Must Enter Y/N!")
        elif ExtraLiab.upper() == "Y" or ExtraLiab.upper() == "N":
            break
        else:
            print("Must Enter Y/N!")

    while True:
        OptGlass = input("Add Glass Coverage? (Y/N): ")
        if OptGlass == "":
            print("Must Enter Y/N!")
        elif OptGlass.upper() == "Y" or OptGlass.upper() == "N":
            break
        else:
            print("Must Enter Y/N!")
    while True:
        OptLoaner = input("Add a loaner car rental? (Y/N): ")
        if OptLoaner == "":
            print("Must Enter Y/N!")
        elif OptLoaner.upper() == "Y" or OptLoaner.upper() == "N":
            break
        else:
            print("Must Enter Y/N!")

    while True:
        PayPlan = input("How is the Customer Paying? (M/F): ")
        if PayPlan == "":
            print("Must Enter M/F!")
        elif PayPlan.upper() == "M" or PayPlan.upper() == "F":
            break
        else:
            print("Must Enter M/F!")

    if PayPlan.upper() == "M":
        PayPlanPad = "Monthly"
    elif PayPlan.upper() == "F":
        PayPlanPad = "Paid in Full"

    # Default Variables:

    f = open("OSICDef.dat", "r")
    PolNum = int(f.readline())
    BasicRate = float(f.readline())
    MultiDiscRate = float(f.readline())
    ExtraLiabRate = float(f.readline())
    OptGlassRate = float(f.readline())
    OptLoanerRate = float(f.readline())
    HST = float(f.readline())
    MonthProcFee = float(f.readline())
    f.close()

    # Calculations

    # Extra Charges
    if NumCars == 1:
        NumCarsCost = BasicRate
    if NumCars > 1:
        NumCarsCost = BasicRate + (NumCars - 1) * (BasicRate - (BasicRate * MultiDiscRate))

    if ExtraLiab.upper() == "Y":
        ExtraLiabCost = ExtraLiabRate * NumCars
    else:
        ExtraLiabCost = 0

    if OptGlass.upper() == "Y":
        OptGlassCost = OptGlassRate * NumCars
    else:
        OptGlassCost = 0

    if OptLoaner.upper() == "Y":
        OptLoanerCost = OptLoanerRate * NumCars
    else:
        OptLoanerCost = 0

    TotalExtraCost = ExtraLiabCost + OptGlassCost + OptLoanerCost

    CustInitals = "{}{}".format(CustFirstName.title()[0], CustLastName.title()[0])

    # Total Cost

    TotalInsurancePremium = NumCarsCost + TotalExtraCost
    Tax = TotalInsurancePremium * HST
    TotalCost = TotalInsurancePremium + Tax
    MonthlyPay = (TotalCost + MonthProcFee) / 12
    import datetime
    Today = datetime.datetime.today()
    # Receipt Output
    print()
    print()
    print("         One Stop Insurance Company")
    print("         'We care so don't have to! ☻'")
    print()
    print("              Customer Invoice")
    print()
    print("Policy Number: {}-{}".format(PolNum, CustInitals))
    print("Policy Date: {}".format(Today.strftime('%d-%m-%Y')))
    print()
    print("Customer Information:")
    print("Name: ", CustFirstName, CustLastName)
    print("City:", City)
    print("Province:", Province)
    print("Postal Code:", PostalCode)
    print("Phone:", PhonePad)
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("Number of Cars Insured:                          {}".format(NumCars))
    print("Insurance Base Cost Total:              {}".format(As_Dollars_Pad(NumCarsCost)))
    print("Total Extra Costs:                      {}".format(As_Dollars_Pad(TotalExtraCost)))
    print("Total Insurance Premium:                {}".format(As_Dollars_Pad(TotalInsurancePremium)))
    print("Tax (HST)                               {}".format(As_Dollars_Pad(Tax)))
    print("                                       -----------")
    print("Total Cost:                             {}".format(As_Dollars_Pad(TotalCost)))
    print()
    print("Payment Plan:                           {:>10}".format(PayPlanPad))
    if PayPlan.upper() == "M":
        print("Monthly Payment Amount:                 {}".format(As_Dollars_Pad(MonthlyPay)))
        print("Payment Date:                           {}".format(Monthly_Start(Today)))
    print()

    AnyKey = input("Press Any Key to Save Record...")
    with open('Policies.dat', 'a') as f:
        Write(PolNum, f)
        Write(CustFirstName, f)
        Write(CustLastName, f)
        Write(Address, f)
        Write(City, f)
        Write(Province, f)
        Write(PostalCode, f)
        Write(PhonePad, f)
        Write(NumCars, f)
        Write(ExtraLiab.upper(), f)
        Write(OptGlass.upper(), f)
        Write(OptLoaner.upper(), f)
        Write(PayPlan.upper(), f)
        Write_Space(TotalInsurancePremium, f)
        f.close()

    import time

    print("Saving to file... ", end="")
    for wait in range(1, 11):
        print('*', end=' ')
        time.sleep(.2)
    print()
    print("Policy processed and saved!")
    PolNum = PolNum + 1

    while True:
        Return = input("Do you want to enter another policy? (Y/N): ")
        if Return == "":
            print("Must Enter Y/N!")
        elif Return.upper() == "Y" or Return.upper() == "N":
            with open('OSICDef.dat', "w") as f:
                Write_Space(PolNum, f)
                Write_Space(BasicRate, f)
                Write_Space(MultiDiscRate, f)
                Write_Space(ExtraLiabRate, f)
                Write_Space(OptGlassRate, f)
                Write_Space(OptLoanerRate, f)
                Write_Space(HST, f)
                Write_Space(MonthProcFee, f)
                f.close()
            break
        else:
            print("Must Enter Y/N!")
    if Return.upper() == "N":
        break
#--------------------------------------------------------------------------------------
#Reports:

#Detailed Report:



while True:
    PrintReport = input("Would you like to print a Detailed Report(Y/N): ")
    if PrintReport == "":
        print("Must Enter Y/N!")
    elif PrintReport.upper() == "Y" or PrintReport.upper() == "N":
        break
    else:
        print("Must Enter Y/N!")

if PrintReport.upper() == "Y":

    print("ONE STOP INSURANCE COMPANY")
    print("POLICY LISTING AS OF {}".format(Today.strftime('%d-%m-%Y')))
    print()
    print("POLICY   CUSTOMER         INSURANCE    EXTRA      TOTAL")
    print("NUMBER   NAME              PREMIUM     COSTS     PREMIUM")
    print("========================================================")
    f = open("OSICDef.dat", "r")
    PolNum = int(f.readline())
    BasicRate = float(f.readline())
    MultiDiscRate = float(f.readline())
    ExtraLiabRate = float(f.readline())
    OptGlassRate = float(f.readline())
    OptLoanerRate = float(f.readline())
    HST = float(f.readline())
    MonthProcFee = float(f.readline())
    f.close()

    CustCtr = 0
    InsPremAcc = 0
    ExtraCostAcc = 0
    TotPremAcc = 0

    f = open("Policies.dat", "r")

    for CustLine in f:
        CustData = CustLine.split(",")
        Policy = CustData[0].strip()
        CustName = CustData[1].strip() + " " + CustData[2].strip()
        NumCars = int(CustData[8])
        if CustData[9] == "Y":
            ExtraLiab = ExtraLiabRate * NumCars
        else:
            ExtraLiab = 0

        if CustData[10] == "Y":
            OptGlass = OptGlassRate * NumCars
        else:
            OptGlass = 0

        if CustData[11] == "Y":
            OptLoaner = OptLoanerRate * NumCars
        else:
            OptLoaner = 0

        if NumCars == 1:
            Premium = BasicRate
        if NumCars > 1:
            Premium = BasicRate + (NumCars - 1) * (BasicRate - (BasicRate * MultiDiscRate))

        TotalExtra = ExtraLiab + OptGlass + OptLoaner
        TotalPremium = float(CustData[13].strip())
        print("{:<5}    {:<15} {:>10}{:>10} {:>10}".format(Policy, CustName,As_Dollars_Pad(Premium),As_Dollars_Pad(TotalExtra), As_Dollars_Pad(TotalPremium)))
        CustCtr += 1
        InsPremAcc += Premium
        ExtraCostAcc += TotalExtra
        TotPremAcc += TotalPremium
    f.close()
    print("========================================================")
    print("Total Policies: {:<3}      {:>10}{:>10} {:>10}".format(CustCtr, As_Dollars_Pad(InsPremAcc), As_Dollars_Pad(ExtraCostAcc), As_Dollars_Pad(TotPremAcc)))
    print()
    print("                     END OF RECORD")
    print()

#Exception Report:

while True:
    PrintReport2 = input("Would you like to print an Exception Report(Y/N): ")
    if PrintReport2 == "":
        print("Must Enter Y/N!")
    elif PrintReport2.upper() == "Y" or PrintReport2.upper() == "N":
        break
    else:
        print("Must Enter Y/N!")

if PrintReport2.upper() == "Y":

    print("ONE STOP INSURANCE COMPANY")
    print("MONTHLY PAYMENT LISTING AS OF:",Today.strftime('%d-%m-%Y'))
    print()
    print("POLICY CUSTOMER         TOTAL               TOTAL     MONTHLY")
    print("NUMBER NAME            PREMIUM      HST     COST      PAYMENT")
    print("=============================================================")

    f = open("OSICDef.dat", "r")
    Defaults = f.readlines()
    HST = float(Defaults[6])
    f.close()

    CustExCtr = 0
    TotPremExAcc = 0
    HSTExAcc = 0
    TotCostExAcc = 0
    MonPayExAcc = 0

    f = open("Policies.dat", "r")

    for CustLine in f:
        CustData = CustLine.split(",")
        Policy = CustData[0].strip()
        CustName = CustData[1].strip() + " " + CustData[2].strip()
        PayPlan = CustData[12].strip()
        TotalPremium = float(CustData[13].strip())
        HSTAmt = TotalPremium * HST
        TotCost = (TotalPremium * HST) + TotalPremium
        MonthPay = TotCost / 12
        if PayPlan == "M":
            print("{:<5} {:<15}{:>10}{:>8}{:>10}{:>8}".format(Policy, CustName,As_Dollars_Pad(TotalPremium),As_Dollars_Pad(HSTAmt), As_Dollars_Pad(TotCost),As_Dollars_Pad(MonthPay)))
            CustExCtr += 1
            TotPremExAcc += TotalPremium
            HSTExAcc += HSTAmt
            TotCostExAcc += TotCost
            MonPayExAcc += MonthPay
    f.close()
    print("=============================================================")
    print("Total Policies: {:<3}  {:>10}{:>9}{:>10}{:>9}".format(CustExCtr, As_Dollars_Pad(TotPremExAcc), As_Dollars_Pad(HSTExAcc), As_Dollars_Pad(TotCostExAcc), As_Dollars_Pad(MonPayExAcc)))
    print()
    print("                     END OF RECORD")
