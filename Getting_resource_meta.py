import json
import csv


def read_json_file(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: 1 Invalid JSON data in '{file_path}'.\n{e}")
    return None


def count_resource_types(data):
    resource_counts = {}
    char_counts = {}
    for entry in data["entry"]:
        resource_type = entry["resource"]["resourceType"]
        resource_counts[resource_type] = resource_counts.get(resource_type, 0) + 1
        char_counts[resource_type] = char_counts.get(resource_type, 0) + len(str(entry))
    return resource_counts, char_counts


def save_to_csv(resource_counts, char_counts, output_file):
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["Resource Type", "Count", "Character Count"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for resource_type, count in resource_counts.items():
            print(resource_type, count)
            writer.writerow(
                {
                    "Resource Type": resource_type,
                    "Count": count,
                    "Character Count": char_counts[resource_type],
                }
            )


file_path = "./fhir.json"  # Replace with your actual file path
data = read_json_file(file_path)
# print(data)

if data:
    resource_counts, char_counts = count_resource_types(data)
    output_file = "resource_counts.csv"  # Replace with your desired output file name
    save_to_csv(resource_counts, char_counts, output_file)
    print(f"Results saved to {output_file}")
