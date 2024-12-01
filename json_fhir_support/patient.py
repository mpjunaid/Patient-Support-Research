from json_fhir_support.read_json import read_json_file
import json


def patient_data(file_path):
    data = read_json_file(file_path)
    if not data:
        return "Error: Could not process FHIR data."

    result_str = "\t\t**Patient meta details**\n"
    for entry in data["entry"]:
        resource_type = entry["resource"]["resourceType"]
        if resource_type == "Patient":
            # result_str += json.dumps(entry, indent=4) + "\n\n"

            # Extract and format patient information
            race = entry["resource"]["extension"][0]["extension"][0]["valueCoding"][
                "display"
            ]
            marital_status = entry["resource"]["maritalStatus"]["coding"][0]["display"]
            address_components = entry["resource"]["address"][0]
            street = (
                address_components.get("line", [])[0]
                if address_components.get("line")
                else ""
            )
            city = address_components["city"]
            state = address_components["state"]
            postal_code = address_components["postalCode"]
            country = address_components["country"]
            full_address = f"{street}, {city}, {state} {postal_code}, {country}"
            date_of_birth = entry["resource"]["birthDate"]
            gender = entry["resource"]["gender"]
            name_components = entry["resource"]["name"][0]
            prefix = " ".join(name_components.get("prefix", []))
            given_names = " ".join(name_components["given"])
            family_name = name_components["family"]
            full_name = f"{prefix} {given_names} {family_name}"

            result_str += f"Race: {race}\n"
            result_str += f"Marital Status: {marital_status}\n"
            result_str += f"Address: {full_address}\n"
            result_str += f"Date of Birth: {date_of_birth}\n"
            result_str += f"Gender: {gender}\n"
            result_str += f"Name: {full_name}\n"
    return result_str
