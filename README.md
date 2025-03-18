# MATH441_Project_2

#### Data Generation
The `DataGenereation.ipynb` pulls the `data/used_cars.csv` file, cleans it, assigns new columns `Buying Price`, `Profit`, `size` and `imported`, then export the dataframe as `data/complete_data.csv` for analysis

#### Data Analysis
The `analysis2.0.ipynb` analyzes the data, applies CVXPY algorithm and greedy algorithm, and produces optimized buying and selling strategy for car dealership. To genereate the same result as shown in the report, run the `analysis2.0.ipynb` only, as the data generation script would assign random value and generate new datasets.
