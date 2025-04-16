import csv

# Step 1: Load sales.csv into a dictionary
def load_sales(file_path):
    sales_data = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_data[row['sku']] = int(row['quantity_sold'])
    return sales_data

# Step 2: Apply pricing rules to each product
def apply_rules(product, quantity_sold):
    current_price = float(product['current_price'])
    cost_price = float(product['cost_price'])
    stock = int(product['stock'])

    new_price = current_price

    # Rule 1
    if stock < 20 and quantity_sold > 30:
        new_price = current_price * 1.15
    # Rule 2
    elif stock > 200 and quantity_sold == 0:
        new_price = current_price * 0.70
    # Rule 3
    elif stock > 100 and quantity_sold < 20:
        new_price = current_price * 0.90

    # Rule 4: Minimum profit check
    min_allowed_price = cost_price * 1.2
    if new_price < min_allowed_price:
        new_price = min_allowed_price

    return round(current_price, 2), round(new_price, 2)

# Step 3: Process the products and write to output
def update_prices(products_file, sales_data, output_file):
    with open(products_file, mode='r') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['sku', 'old_price (in ₹)', 'new_price (in ₹)']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            sku = row['sku']
            quantity_sold = sales_data.get(sku, 0)
            old_price, new_price = apply_rules(row, quantity_sold)
            writer.writerow({
                'sku': sku,
                'old_price (in ₹)': f"{old_price:.2f}",
                'new_price (in ₹)': f"{new_price:.2f}"
            })


# Step 4: Run everything
def main():
    sales_data = load_sales('input/sales.csv')
    update_prices('input/products.csv', sales_data, 'output/updated_prices.csv')
    print("Done! Check output/updated_prices.csv")

if __name__ == "__main__":
    main()
