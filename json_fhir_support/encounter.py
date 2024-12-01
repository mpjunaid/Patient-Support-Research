import json
from json_fhir_support.read_json import read_json_file


def encounter_data(file_path, count_limit=3):
    data = read_json_file(file_path)
    if not data:
        return "Error: Could not process FHIR data."
    result_str = "\n-----------------------------------------------------------\n \t \t**Encounter data**\n"
    result_str += "| Status | Participant Type | Participant | Start Date | End Date | Reason Code | Service Provider | Subject |\n"
    result_str += "|---|---|---|---|---|---|---|---|"

    count = 0
    for entry in reversed(data["entry"]):
        resource_type = entry["resource"]["resourceType"]
        if resource_type == "Encounter":
            status = entry["resource"]["status"]
            participant_type = entry["resource"]["participant"][0]["type"][0]["text"]
            participant = entry["resource"]["participant"][0]["individual"]["display"]
            start_date = entry["resource"]["period"]["start"]
            end_date = entry["resource"]["period"]["end"]
            reason_code = (
                entry["resource"]["reasonCode"][0]["coding"][0]["display"]
                if "reasonCode" in entry["resource"]
                else ""
            )
            service_provider = entry["resource"]["serviceProvider"]["display"]
            # subject = entry["resource"]["subject"]["display"]
            result_str += f"\n| {status} | {participant_type} | {participant} | {start_date} | {end_date} | {reason_code} | {service_provider}  |"
            count += 1
            if count >= count_limit:
                break

    return result_str


# # Example usage:
# file_path = "./fhir.json"
# result = encounter_data(file_path, count_limit=5)  # Adjust count_limit as needed
# print(result)
