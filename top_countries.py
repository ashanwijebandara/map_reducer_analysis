import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the output file (Hadoop MapReduce result)
output_file = 'gtd_output.txt'

if not os.path.exists(output_file):
    print(f"Error: {output_file} not found.")
    exit(1)

# Read and parse the data
data = []
with open(output_file, 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            country, count = parts
            try:
                data.append((country, int(count)))
            except ValueError:
                continue  # skip invalid lines

# Create a DataFrame and sort
df = pd.DataFrame(data, columns=["Country", "Attacks"])
top10 = df.sort_values(by="Attacks", ascending=False).head(10)

# Save to CSV
top10.to_csv("top10_countries.csv", index=False)

# Print in terminal
print("\nTop 10 Countries by Number of Terrorist Attacks:")
print(top10.to_string(index=False))

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(top10["Country"][::-1], top10["Attacks"][::-1], color="skyblue")
plt.title("Top 10 Countries by Number of Terrorist Attacks")
plt.xlabel("Number of Attacks")
plt.tight_layout()

# Save plot
plt.savefig("top10_countries.png")
plt.show()

