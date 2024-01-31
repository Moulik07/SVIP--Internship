import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
sales_data = pd.read_csv('sales_data.csv')

# Function to perform data exploration
def explore_sales_data(data):
    print("-------------------------------------------------")
    print("           SALES DATA EXPLORATION                ")
    print("-------------------------------------------------")

    # Task 1: Initial Overview
    print("\nTask 1: Initial Overview")
    print("-------------------------------------------------")
    print(f"Dataset shape: {data.shape}")
    print(data.head())

    # Task 2: Data Types
    print("\nTask 2: Data Types")
    print("-------------------------------------------------")
    print(data.dtypes)

    # Task 3: Summary Statistics for Numerical Columns
    print("\nTask 3: Summary Statistics for Numerical Columns")
    print("-------------------------------------------------")
    print(data.describe())

    # Task 4: Unique Values in Categorical Columns
    categorical_columns = ['Product_Category', 'Sub_Category', 'Age_Group', 'Customer_Gender']
    print("\nTask 4: Unique Values in Categorical Columns")
    print("-------------------------------------------------")
    for col in categorical_columns:
        unique_values = data[col].unique()
        print(f"Unique values in {col}: {', '.join(map(str, unique_values))}")

    # Task 5 (Optional): Visualize Sales by Product Category
    if 'Product_Category' in data.columns and 'Revenue' in data.columns:
        print("\nTask 5 (Optional): Visualize Sales by Product Category")
        print("-------------------------------------------------")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Product_Category', y='Revenue', data=data, ci=None)
        plt.title('Total Revenue by Product Category')
        plt.xlabel('Product Category')
        plt.ylabel('Total Revenue')
        plt.xticks(rotation=45)
        plt.show()

    # Task 6: Correlation Matrix and Heatmap
    print("\nTask 6: Correlation Matrix and Heatmap")
    print("-------------------------------------------------")
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()

    # Task 7: Histograms for Numerical Columns
    print("\nTask 7: Histograms for Numerical Columns")
    print("-------------------------------------------------")
    numerical_columns = data.select_dtypes(include='number').columns
    for col in numerical_columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(data[col], bins=30, kde=True)
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.show()

    print("\nData Exploration Complete.")

# Perform data exploration
explore_sales_data(sales_data)
