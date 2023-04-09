import csv
import sys

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, 'r') as csv_input_file:
        # read the CSV file
        csv_reader = csv.reader(csv_input_file)
        # skip the header row
        next(csv_reader)

        # prepare the header row for the output CSV file
        header = ['first', 'last', 'house']

        with open(output_file, 'w', newline='') as csv_output_file:
            # create a writer object for the output CSV file
            csv_writer = csv.writer(csv_output_file)
            # write the header row to the output CSV file
            csv_writer.writerow(header)

            for row in csv_reader:
                # split the name into first name and last name
                name_parts = row[0].split(", ")
                first_name = name_parts[1]
                last_name = name_parts[0]
                house = row[1]
                # write the row to the output CSV file
                csv_writer.writerow([first_name, last_name, house])
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")