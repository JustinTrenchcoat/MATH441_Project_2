import numpy as np

# easy function for updating the status
def Update_EV(counter_EV):
    counter_EV = 1
def Update_Import(counter_import):
    counter_import = 1

def check_price(i, fuel, imported, profit, EV_fee, license_fee, counter_EV, counter_import):
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
    
def infoPage(N, profit, size, budget, parkCapacity, spent):
    print("Total Number of cars ready to sell: ", N)
    print("Total car value: $",np.sum(profit))
    print("Total Size of cars: ",size, "m^2")
    print("Total buying cost amount: $", sum(budget))
    print("------------------------------------------")
    print("Parking Lot Capacity: ",parkCapacity, "m^2")
    print("Available Budget Amount: $", spent)

def runOG(items, profit, size, budget):
    print("---------------------------------------------------------------")
    print("Dealership Decision Optimizer Greedy System(D-DOGS) is optimizing....")
    print("---------------------------------------------------------------")
    print(len(items), "cars sold")
    print("Profit: $", sum(profit[items]))
    print("Actual Size of cars sold: ", sum(size[items]), "m^2")
    print("Actual budget spent: $", sum(budget[items]))


# check if the car i is EV or imported
def check_EV(i, fuel):
    return ((fuel[i] == 'Hybrid') or (fuel[i] == "Plug-In Hybrid"))

def check_import(i, imported):
    return (imported[i] == 1)

def check_constraints(items, size, cost, parkCapacity, dealBudget):
    total_size = sum([size[k] for k in items])
    total_cost = sum([cost[k] for k in items])
    if ((total_size > parkCapacity) or (total_cost > dealBudget)):
        items.pop()
        return True
    else:
        return False
    
def ddog_size(items,fuel, imported, 
              value_per_size,
              profit, EV_fee, license_fee, 
              size, cost, parkCapacity,dealBudget, 
              counter_EV, counter_import, should_break):
    while True:
        # Find the most valuable item
        sorted_indices = value_per_size.sort_values(ascending=False).index.tolist() # Indices sorted in descending order
        i = sorted_indices[0]  # Index of the largest item
        j = sorted_indices[1]    
        if value_per_size[i] == 0:
            break
        else:
            if (check_price(i,fuel, imported, 
                            profit, EV_fee, license_fee, 
                            counter_EV, counter_import) >= check_price(j,fuel, imported, 
                                                                        profit, EV_fee, license_fee, 
                                                                        counter_EV, counter_import)):
                items.append(i)
                # update the counter if necessary
                if check_EV(i, fuel):
                    Update_EV(counter_EV)
                elif check_import(i, imported):
                    Update_Import(counter_import)
                value_per_size[i] = 0  
                if(check_constraints(items, size, cost, parkCapacity, dealBudget)):
                    should_break=True
            else:
                items.append(j)
                # update the counter if necessary
                if check_EV(j, fuel):
                    Update_EV(counter_EV)
                elif check_import(j, imported):
                    Update_Import(counter_import)
                value_per_size[j] = 0  
                if(check_constraints(items, size, cost,parkCapacity, dealBudget)):
                    should_break=True
        if (should_break):
            break
    return items


def ddog_budget(items,fuel, imported, 
              value_per_budget,
              profit, EV_fee, license_fee, 
              size, cost, parkCapacity,dealBudget,
              counter_EV, counter_import, should_break):
    while True:
        # Find the most valuable item
        sorted_indices = value_per_budget.sort_values(ascending=False).index.tolist() # Indices sorted in descending order
        i = sorted_indices[0]  # Index of the largest item
        j = sorted_indices[1]    
        if value_per_budget[i] == 0:
            break
        else:
            if (check_price(i,fuel, imported, 
                            profit, EV_fee, license_fee,
                            counter_EV, counter_import) >= check_price(j,fuel, imported, 
                                                                        profit, EV_fee, license_fee,
                                                                        counter_EV, counter_import)):
                items.append(i)
                # update the counter if necessary
                if check_EV(i, fuel):
                    Update_EV(counter_EV)
                elif check_import(i, imported):
                    Update_Import(counter_import)
                value_per_budget[i] = 0  
                if(check_constraints(items, size, cost, parkCapacity, dealBudget)):
                    should_break=True
            else:
                items.append(j)
                # update the counter if necessary
                if check_EV(j, fuel):
                    Update_EV(counter_EV)
                elif check_import(j, imported):
                    Update_Import(counter_import)
                value_per_budget[j] = 0  
                if(check_constraints(items, size, cost, parkCapacity, dealBudget)):
                    should_break=True
        if (should_break):
            break
    return items