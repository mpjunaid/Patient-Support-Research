import json
from json_fhir_support.read_json import read_json_file


def medical_request_data(file_path, count_limit=3, status_check=True):
    data = read_json_file(file_path)
    if not data:
        return "Error: Could not process FHIR data."

    result_str = "\n--------------------------------------------------------\n\t \t **Medicine Report**\n| Status | Medicine | Reason | Requested_by | start_date |\n"
    result_str += "|-----|-----|-----|-----|-----|-----|"

    count = 0
    for data_ in reversed(data["entry"]):
        resource_type = data_["resource"]["resourceType"]
        if resource_type == "MedicationRequest":
            # print(json.dumps(data_["resource"], indent=4))
            medicine = data_["resource"]["medicationCodeableConcept"]["text"]
            reason = data_["resource"]["reasonReference"][0]["display"]
            start_date = data_["resource"]["authoredOn"]
            status = data_["resource"]["status"]
            requested_by = data_["resource"]["requester"]["display"]
            if status_check:
                if status == "active":
                    result_str += f"\n{status} | {medicine} | {reason} | {requested_by} | {start_date}\n"

            else:
                result_str += f"\n{status} | {medicine} | {reason} | {requested_by} | {start_date}\n"
            count += 1
            if count >= count_limit:
                break

    return result_str


# # Example usage:
# file_path = "./fhir.json"
# result = medical_request_data(file_path, count_limit=5)  # Adjust count_limit as needed
# print(result)
