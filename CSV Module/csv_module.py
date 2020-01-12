import csv

filepath = 'names.csv'

with open(filepath) as file:
    csv_reader = csv.DictReader(file)

    with open('new_names.csv', 'w') as f:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)

        csv_writer.writeheader() # This line writes the headers

        for row in csv_reader:
            csv_writer.writerow(row)