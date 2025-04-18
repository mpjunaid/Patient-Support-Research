# FHIR JSON Parser for RAG Applications

This project provides a lightweight Python library designed to parse healthcare data stored in JSON format according to the FHIR (Fast Healthcare Interoperability Resources) standard. The goal is to convert complex and verbose FHIR structures into simplified, tabular, and human-readable formats, making them suitable for use in Retrieval-Augmented Generation (RAG) systems powered by large language models (LLMs).

## 🚀 Purpose

FHIR data is extensive and difficult for LLMs to understand directly. This library focuses on preprocessing FHIR-compliant data into an experimental structured format that is more digestible for LLMs. Our preliminary tests using **LLaMA 3.2 1B** model showed a **100% QA accuracy** using manually evaluated true/false question-answering tasks.

Currently, the parser supports the following FHIR resource types:

- `Condition`
- `DiagnosticReport`
- `Encounter`
- `MedicalRequest`
- `Patient`

Anyone futher intrested to continue with this work please reach out to me. Thank you.

