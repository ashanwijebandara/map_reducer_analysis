import csv

input_file = "gtd.csv"
output_file = "gtd_clean.csv"

with open(input_file, "r", encoding="utf-8", errors="replace") as infile, \
     open(output_file, "w", newline='', encoding="utf-8") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader, None)  # Skip the header row

    for row in reader:
        
        if len(row) >= 135:  # GTD has around 135 columns
            writer.writerow(row)

print(f"✅ Preprocessing complete. Output saved to {output_file}")
