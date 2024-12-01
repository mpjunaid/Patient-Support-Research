import json
from llm import M_LLM


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
    for entry in data["entry"]:
        resource_type = entry["resource"]["resourceType"]
        resource_counts[resource_type] = resource_counts.get(resource_type, 0) + 1
    return resource_counts


file_path = "./fhir.json"
data = read_json_file(file_path)

if data:
    # Print the second entry in a formatted way
    # print(json.dumps(data["entry"][1], indent=4))

    # Count the resource types and print the results
    resource_counts = count_resource_types(data)
    print("Resource Type Counts:")
    for resource_type, count in resource_counts.items():
        print(f"{resource_type}: {count}")
s = ""
count = 0

for entry in data["entry"]:
    if count == 6:
        break
    resource_type = entry["resource"]["resourceType"]
    if resource_type == "MedicationRequest":
        count += 1
        # print(json.dumps(entry, indent=4))
        # print("---------------------------------------------------------------")
        s += str(entry)
print(len(str(data)))
print(f"Length of String:{len(s)}")
prompt = f""" Tabulate following Medical requests with status, medicine name, start date,dosage and reason for each of the entry and remove the rest of the infromation\n {s}

"""
print("---------------------------------------------------------------")
print(prompt)
print("---------------------------------------------------------------")
summary = M_LLM(prompt)
print(summary)
# for data_ in data["entry"]:
#     print(json.dumps(data_, indent=4))
#     medicine = data_["medicationCodeableConcept"]["text"]
#     reason = data_["resource"]["reasonReference"][0]["display"]
#     dosage = f"{data_['resource']['dosageInstruction'][0]['doseAndRate'][0]['doseQuantity']['value']} {data_['resource']['medicationCodeableConcept']['text'].split()[-1]}"  # Get last word for unit
#     start_date = data_["resource"]["authoredOn"].split("T")[0]
#     status = data_["resource"]["status"]
#     requested_by = data_["resource"]["requester"]["display"]
#     print(f"{medicine}\t{reason}")
