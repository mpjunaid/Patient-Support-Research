from json_fhir_support.read_json import read_json_file
import json


def condition_data(file_path, count_limit=1):
    data = read_json_file(file_path)
    if not data:
        return "Error: Could not process FHIR data."
    result_str = "\n----------------------------------------------------\n\t\t**Patient Condition**\n"
    result_str += "| Code | Recorded Date | Clinical Status |\n"
    result_str += "|---|---|---|"

    count = 0
    flag = 0
    for entry in reversed(data["entry"]):
        if count_limit == -1:
            flag = 1
        if flag:
            count_limit += 1
        resource_type = entry["resource"]["resourceType"]
        if resource_type == "Condition":
            code = entry["resource"]["code"]["text"]
            recorded_date = entry["resource"]["recordedDate"]
            clinical_status = entry["resource"]["clinicalStatus"]["coding"][0]["code"]
            result_str += f"\n| {code} | {recorded_date} | {clinical_status} |"
            count += 1
            if count >= count_limit:
                break

    return result_str


# # Example usage:
# file_path = "your_fhir_file.json"
# result = condition_data(file_path, count_limit=5)  # Adjust count_limit as needed
# print(result)
