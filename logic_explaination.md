

##  Logic Explanation

---

##  Overview

This project builds an AI-powered system that converts a **Business Requirement Document (BRD)** into API integrations and simulates execution.

---

##  Core Flow

```text
BRD (Natural Language)
    ↓
AI Parser
    ↓
Structured JSON (services + mappings)
    ↓
Integration Registry Lookup
    ↓
Configuration Generation
    ↓
Simulation Engine (Mock APIs)
    ↓
UI Output
```

---

##  1. BRD Parser (`app/parser/brd_parser.py`)

###  Purpose

Convert natural language BRD into structured JSON.

###  Logic

1. Takes raw BRD text as input
2. Sends it to an LLM (Gemini API) using a predefined prompt
3. Extracts:

   * Services (KYC, GST, Fraud)
   * Field mappings (Name → full_name)
4. Returns structured JSON

###  Example

**Input:**

```text
The system must integrate with KYC. Name maps to full_name.
```

**Output:**

```json
{
  "services": [{"name": "KYC"}],
  "mappings": [{"source": "Name", "target": "full_name"}]
}
```

###  Key Idea

Use AI to replace manual requirement analysis.

---

##  2. Prompt Template (`prompt_templates.py`)

###  Purpose

Guide the LLM to return structured JSON.

###  Logic

* Defines instructions for LLM
* Ensures consistent format
* Reduces ambiguity

###  Key Idea

Prompt engineering ensures reliable parsing.

---

##  3. Integration Registry (`app/registry/`)

###  Purpose

Store available APIs and their versions.

###  Logic

* `adapters.json` stores:

  * Services
  * Versions
  * Endpoints

**Example:**

```json
"KYC": {
  "v1": {"endpoint": "/kyc/v1"},
  "v2": {"endpoint": "/kyc/v2"}
}
```

* `registry_loader.py` loads JSON into Python dict

###  Key Idea

Acts as a service catalog (API marketplace).

---

##  4. Config Generator (`app/engine/config_generator.py`)

###  Purpose

Convert parsed data into executable configuration.

###  Logic

#### Step 1: Normalize Service Names

* Converts "kyc verification" → "KYC"

#### Step 2: Select Version

* Picks latest version (e.g., v2)

#### Step 3: Build Mapping

* Uses mapping engine

#### Step 4: Generate Config

Combines:

* Service
* Version
* Endpoint
* Mapping

###  Example Output

```json
{
  "service": "KYC",
  "version": "v2",
  "endpoint": "/kyc/v2",
  "mapping": {...}
}
```

###  Key Idea

Automates integration setup.

---

##  5. Mapping Engine (`app/engine/mapping_engine.py`)

###  Purpose

Map source fields to target API fields.

###  Logic

* Takes parsed mappings
* Converts into dictionary

###  Example

**Input:**

```json
[{"source": "Name", "target": "full_name"}]
```

**Output:**

```json
{
  "Name": "full_name"
}
```

###  Key Idea

Handles schema transformation.

---

##  6. Simulation Engine (`app/simulation/simulator.py`)

###  Purpose

Simulate API execution using mock APIs.

###  Logic

#### Step 1: Generate Dynamic User

* Random Name
* Valid PAN
* GSTIN

#### Step 2: Apply Mapping

* Convert input → API format

#### Step 3: Call Mock APIs

* KYC
* GST
* Fraud

#### Step 4: Collect Results

Stores:

* Input
* Transformed data
* Response

#### Step 5: Evaluate Success

Rules:

* KYC → status must be `"verified"`
* GST → `gst_valid = True`
* Fraud → risk must NOT be HIGH

###  Key Idea

Simulates real API orchestration.

---

##  7. Mock APIs (`app/simulation/mock_apis.py`)

###  Purpose

Simulate real-world API behavior.

###  Logic

* **KYC API**

  * Validates PAN
  * Returns verified/failed

* **GST API**

  * Validates GSTIN
  * Returns business details

* **Fraud API**

  * Generates risk score
  * Classifies LOW / MEDIUM / HIGH

###  Key Idea

Mimics external services without real APIs.

---

##  8. Backend (`app/main.py`)

###  Purpose

Expose system as API.

###  Logic

* Endpoint: `/simulate`
* Input: BRD
* Pipeline:

  * Parse → Config → Simulate
* Returns final results

###  Key Idea

Makes system usable as a service.

---

##  9. UI (`ui/app.py`)

###  Purpose

Provide user interface using Streamlit.

###  Logic

#### Step 1: Input BRD

* User enters text

#### Step 2: Run Pipeline

Calls:

* `parse_brd()`
* `generate_config()`
* `simulate_integration()`

#### Step 3: Display Results

* Parsed output
* Config

#### Step 4: Show User Data

* One dynamic user

#### Step 5: Show Service Results

* Transformed data
* API responses

#### Step 6: Show Status

* SUCCESS / FAILED

###  Key Idea

Visualizes full pipeline clearly.

---

##  10. Data Flow Summary

```text
1. User enters BRD
2. Parser extracts structured data
3. Registry provides API info
4. Config generator builds plan
5. Simulator executes
6. UI displays results
```

---

##  11. Design Principles

* Modular architecture
* Separation of concerns
* AI-driven automation
* Extensibility
* Realistic simulation

---

##  12. Key Innovations

* AI-based requirement parsing
* Automated config generation
* Dynamic data simulation
* End-to-end pipeline visibility

---

##  Conclusion

This system demonstrates how AI can automate complex backend workflows by converting natural language requirements into executable integration pipelines.

---
