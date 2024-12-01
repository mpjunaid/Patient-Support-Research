from json_fhir_support.patient import patient_data
from json_fhir_support.condition import condition_data
from json_fhir_support.diagnosticReport import diagnostic_report_data
from json_fhir_support.encounter import encounter_data
from json_fhir_support.medical_request import medical_request_data

count = 10
# Example usage:
file_path = "./fhir.json"

result = ""
result += patient_data(file_path)
result += condition_data(
    file_path, count_limit=count
)  # -1 for all the values to be returned
# Future add options to think about active and resolved scenarios to the gpt

result += diagnostic_report_data(
    file_path, count_limit=count
)  # Adjust count_limit as needed


result += encounter_data(
    file_path,
    count_limit=count,
)  # Adjust count_limit as needed
# print(result)
result += medical_request_data(
    file_path, count_limit=count, status_check=True
)  # Adjust count_limit as needed
# status check True or False   True means only active is considered  False means everthing else is considered tooo


print(result)
print("Length of context:", len(result))
