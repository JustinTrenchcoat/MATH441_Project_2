import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    print("Total car value: $",np.sum(profit).round(2))
    print("Total Size of cars: ",size.round(2), "m^2")
    print("Total buying cost amount: $", sum(budget).round(2))
    print("------------------------------------------")
    print("Parking Lot Capacity: ",parkCapacity.round(2), "m^2")
    print("Available Budget Amount: $", spent.round(2))

def runOG(items, profit, size, budget):
    print("---------------------------------------------------------------")
    print("Dealership Decision Optimizer Greedy System(D-DOGS) is optimizing....")
    print("---------------------------------------------------------------")
    print(len(items), "cars sold")
    print("Profit: $", sum(profit[items]).round(2))
    print("Actual Size of cars sold: ", sum(size[items]).round(2), "m^2")
    print("Actual budget spent: $", sum(budget[items]).round(2))


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

def greedy(items,fuel, imported, 
              valList,
              profit, EV_fee, license_fee, 
              size, cost, parkCapacity,dealBudget,
              counter_EV, counter_import, should_break):
    while True:
        # Find the most valuable item
        sorted_indices = valList.sort_values(ascending=False).index.tolist() # Indices sorted in descending order
        i = sorted_indices[0]  # Index of the largest item
        j = sorted_indices[1]    
        if valList[i] == 0:
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
                valList[i] = 0  
                if(check_constraints(items, size, cost, parkCapacity, dealBudget)):
                    should_break=True
            else:
                items.append(j)
                # update the counter if necessary
                if check_EV(j, fuel):
                    Update_EV(counter_EV)
                elif check_import(j, imported):
                    Update_Import(counter_import)
                valList[j] = 0  
                if(check_constraints(items, size, cost, parkCapacity, dealBudget)):
                    should_break=True
        if (should_break):
            break
    return items


def selected(df, index,alg_name, title, feature, select_type):
    # mare sure the catagories:
    catagories = df[select_type].unique()
    # specify the summarize type
    if select_type == 'imported':
        # we are doing the import/demestic summary:
        selected = df.loc[index, select_type].map({0: 'domestic', 1: 'imported'})
    else:
        selected = pd.Categorical(df.loc[index, select_type], categories=catagories, ordered=True)  
    # continue with summary, we don't want to list up all the brands:
    if select_type != "brand":
        print(f"Summarize of profit, catagorized in {feature}:")
        for catagory in catagories:
            type_profit = df[df[select_type].isin([catagory])]['Profit'].mean().round(1)
            print(f"Mean profit for {catagory} cars: {type_profit}")
    #-----------------------------------------------------------------------------
    counts = pd.Series(selected).value_counts().sort_index()
    plt.figure(figsize=(14,5))
    counts.plot(kind="bar", color = "skyblue", edgecolor="black")
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title(f"Distribution of {title} Chosen {feature}")
    plt.xticks(rotation=45, ha="right", fontsize=10)  # Reduce font size
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.subplots_adjust(bottom=0.2)  # Add padding to prevent label cutoff
    for i, value in enumerate(counts):
        plt.text(i,value +0.5, str(value), ha="center", va="bottom", fontsize=10)
    plt.savefig(f"data/{alg_name}_{select_type}.png", dpi=300, bbox_inches="tight")
    plt.show()
