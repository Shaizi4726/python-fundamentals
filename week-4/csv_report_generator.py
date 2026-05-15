import csv
import os


def write_csv(file_path):
    with open(file_path, mode='w', newline='', encoding="utf-8") as csv_write:
        csv_writer = csv.writer(csv_write)
        headers = ["date", "product", "quantity", "unit_price"]
        csv_writer.writerow(headers)
        data = [
            ["02-01-2026", "Python Crash Course Book", 3, 128.5],
            ["03-01-2026", "Ergonomic Desk Chair", 2, 1285.5],
            ["15-01-2026", "GitHub Copilot 1-Year Subscription", 3, 367.3],
            ["21-01-2026", "Mechanical Keyboard(Linear Switches)", 2, 440.75],
            ["22-01-2026", "Docker & Kubernetes Video Course", 3, 165.3],
            ["24-01-2026", "Mechanical Keyboard(Linear Switches)", 2, 440.75],
            ["21-02-2026", "Raspberry Pi 5 Starter Kit", 1, 348.95],
            ["22-02-2026", "GitHub Copilot 1-Year Subscription", 2, 367.3],
            ["02-03-2026", "Ergonomic Desk Chair", 3, 1285.5],
            ["13-03-2026", "Ergonomic Desk Chair", 3, 1285.5],
            ["16-03-2026", "Docker & Kubernetes Video Course", 4, 165.3],
            ["16-03-2026", "Python Crash Course Book", 4, 128.5],
            ["24-03-2026", "Raspberry Pi 5 Starter Kit", 4, 348.95],
            ["28-03-2026", "GitHub Copilot 1-Year Subscription", 4, 367.3],
            ["29-03-2026", "GitHub Copilot 1-Year Subscription", 3, 367.3],
        ]
        csv_writer.writerows(data)


def read_and_analyse(file_path):
    with open(file_path, mode='r', newline='', encoding="utf-8") as csv_read:
        csv_reader = csv.DictReader(csv_read)

        products_data = {}
        highest_value = 0
        total_revenue = 0

        for row in csv_reader:
            product = row['product']
            try:
                quantity = int(row['quantity'])
                unit_price = float(row['unit_price'])
            except (ValueError, KeyError) as e:
                print(f"Skipping bad row {row}: {e}")
                continue

            total = quantity * unit_price
            total_revenue += total

            if total > highest_value:
                highest_value = total
                highest_value_transaction = row

            if product in products_data:
                products_data[product]['quantity'] += quantity
                products_data[product]['revenue'] += total
            else:
                products_data[product] = {
                    'quantity': quantity, 'revenue': total}

    max_quantity = max(data['quantity']
                       for data in products_data.values())

    return {'products_data': products_data, 'highest_value': highest_value, 'highest_value_transaction': highest_value_transaction, 'total_revenue': total_revenue, 'max_quantity': max_quantity}


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "assets", "sales_data.csv")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    write_csv(file_path)
    data = read_and_analyse(file_path)

    products_data = data['products_data']
    highest_value = data['highest_value']
    highest_value_transaction = data['highest_value_transaction']
    total_revenue = data['total_revenue']
    max_quantity = data['max_quantity']

    print(f"\n{'=' * 80}")
    print("Total Revenue Per Product")
    print(f"{'=' * 80}\n")

    print(f"{'Product':<50} Revenue")
    print('-' * 80)
    for key, data in products_data.items():
        if data['quantity'] == max_quantity:
            best_selling = key
        print(f"{key:<50} {data['revenue']:.2f}")

    print(f"\n{'=' * 80}")
    print("Best Selling (Quantity)")
    print(f"{'=' * 80}\n")

    print(f"Product: {best_selling}, Quantity: {max_quantity}")

    print(f"\n{'=' * 80}")
    print("Highest Value Transaction")
    print(f"{'=' * 80}\n")

    print(
        f"Date: {highest_value_transaction['date']}, Product: {highest_value_transaction['product']}, Quantity: {highest_value_transaction['quantity']}, Unit Price: {highest_value_transaction['unit_price']} Total: {highest_value}")

    print(f"\n{'=' * 80}")
    print("Overall Total Revenue")
    print(f"{'=' * 80}\n")

    print(
        f"Total Revenue: {total_revenue}")


if __name__ == "__main__":
    main()
