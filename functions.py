# easy function for updating the status
def Update_EV():
    global counter_EV 
    counter_EV = 1
def Update_Import():
    global counter_import
    counter_import = 1


def Downdate_EV():
    global counter_EV 
    counter_EV = 0
def Downdate_Import():
    global counter_import
    counter_import = 0

def check_price(i, fuel, imported, profit, EV_fee, license_fee):
    fuel_type = fuel[i]
    status = imported[i]
    i_profit = profit[i]
    # fuel deduction:
    if ((fuel_type == 'Hybrid') or (fuel_type == "Plug-In Hybrid")):
        if (counter_EV == 1):
            return i_profit
        else: 
            i_profit -= EV_fee
            return i_profit
    # import deduction
    elif (status == 1):
        if (counter_import == 1):
            return i_profit
        else:
            i_profit -= license_fee
            return i_profit
    else:
        return i_profit