import json
from json_fhir_support.read_json import read_json_file


def diagnostic_report_data(file_path, count_limit=3):
    data = read_json_file(file_path)
    if not data:
        return "Error: Could not process FHIR data."
    result_str = "\n----------------------------------------------\n\t\t**Dianostic Report for the patient**\n"
    result_str += "| Status | Category | Performer | date |\n"
    result_str += "|---|---|---| --|"

    count = 0
    flag = 0
    for entry in reversed(data["entry"]):
        if count_limit == -1:
            flag = 1
        if flag:
            count_limit += 1
        resource_type = entry["resource"]["resourceType"]
        if resource_type == "DiagnosticReport":
            status = entry["resource"]["status"]
            date = entry["resource"]["issued"]
            category = ""
            if "category" in entry["resource"]:
                val = entry["resource"]["category"][0]["coding"]
                for i in val:
                    category += i["display"]
                    if len(val) > 1:
                        category += ","

            performer = (
                entry["resource"]["performer"][0]["display"]
                if "performer" in entry["resource"]
                else ""
            )
            result_str += f"\n| {status} | {category} | {performer} |{date}"
            count += 1
            if count >= count_limit:
                break

    return result_str


# # Example usage:
# file_path = "./fhir.json"
# result = diagnostic_report_data(file_path, count_limit=5)  # Adjust count_limit as needed
# print(result)
