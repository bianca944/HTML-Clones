# package init
import csv

def save_groups_to_csv(groups, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Group Number", "File Paths"])
        for i, group in enumerate(groups):
            writer.writerow([i + 1, ', '.join(group)])

def load_groups_from_csv(input_file):
    groups = []
    with open(input_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            group_files = row[1].split(', ')
            groups.append(group_files)
    return groups
