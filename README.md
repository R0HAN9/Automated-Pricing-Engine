Automated Pricing Engine to Optimize Product Pricing

Build a Python-based pricing engine that automatically adjusts product prices based on current
inventory levels and recent sales performance.

    Input Files:
    products.csv: Contains the product catalog (sku, name, current price, cost price, stock).
    sales.csv: Contains the quantity of each product sold in the last 30 days.

    Output File:
    updated_prices.csv: Contains product SKUs, old price, and new adjusted price.

Problem Breakdown

    Load Data: Parse sales.csv and products.csv to get sales data and product details.

    Apply Pricing Rules: Use predefined business rules (like low stock, high demand,
    overstock, etc.) to adjust prices.

    Profit Margin Constraint: Ensure that the new price is at least 20% above the cost
    price to maintain a healthy profit margin.

    Output Results: Generate an updated_prices.csv file containing the product SKU, old
    price, and new price.

Pricing Rules
Rule 1: If stock < 20 and quantity sold > 30, increase the price by 15%.
Rule 2: If stock > 200 and quantity sold == 0, decrease the price by 30%.
Rule 3: If stock > 100 and quantity sold < 20, decrease the price by 10%.
Rule 4: The final price must always be at least 20% higher than the cost price.

DSA Concepts Used
Data Structure
Dictionary (HashMap): Used to store sales_data by SKU, allowing for constanttime lookup when applying rules to each product.

        List: Used to hold rows of products and the result rows to be written into the
        output CSV.

Why DSA
Efficiency: A dictionary allows fast lookups of sales data for each product
(constant time access).

    Scalability: For large datasets, we can ensure we access data in O(1) time for
    each product, making the solution efficient.

Solution Approach for Large Data
If the dataset is too large to fit into memory

    Streaming Data: Process the data in chunks using a streaming approach. Instead of
    loading the entire products.csv or sales.csv file into memory, read and process each
    line one at a time.

1. For example, you can use file streaming for large CSV files, processing one row at a time
   to save memory.
2. External Sorting: If the data is too large, you can use external sorting techniques
   where you store the data on disk, sort it in chunks, and merge them into a final sorted
   result.
3. Optimizing Memory: Use Python’s memory_profiler to monitor memory usage and
   optimize memory allocation, ensuring that only necessary data is loaded into memory.
4. Parallel Processing: If applicable, use Python’s multiprocessing library to parallelize
   the price computation for different products. This allows you to take advantage of
   multiple cores, speeding up the process for very large datasets.
   Code Efficiency
   The code is designed to be space-efficient by processing data line-by-line and using dictionaries
   for fast lookups. This ensures that even with large input sizes, the process will not overload
   memory.
