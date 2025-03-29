# MATH441_Project_2
## Knapsack Problem
### Problem Statement

We have a set of cars of different sizes and values and a parking lot at the dealership with a limited car capacity. How do we choose which cars to pack into the parking lot to maximize the total sale value?

### Define Variables and Parameters

* $N$ is the number of cars
* $s_i$ is the size of car $i$
* $v_i$ is the value of car $i$
* $x_i$ is the decision variables: $x_i = 1$ if car $i$ is chosen and $x_i = 0$ if not
* $c_i$ is the carbon tax of the car $i$
* $C$ is the total carbon tax amount the dealership paid. 
* $S$ is the capacity of the parking lot

### Identify Constraints and Make Assumptions

* Total area of the parked items is less than the parking lot capacity

#### Data Generation
The `DataGenereation.ipynb` pulls the `data/used_cars.csv` file, cleans it, assigns new columns `Buying Price`, `Profit`, `size` and `imported`, then export the dataframe as `data/complete_data.csv` for analysis

#### Data Analysis
The `analysis2.0.ipynb` analyzes the data, applies CVXPY algorithm and greedy algorithm, and produces optimized buying and selling strategy for car dealership. To genereate the same result as shown in the report, run the `analysis2.0.ipynb` only, as the data generation script would assign random value and generate new datasets.