

## 📂 Folder Structure & Explanation

---

## 📌 Project Overview

This project is an **AI-driven system** that converts a **Business Requirement Document (BRD)** into API integration configurations and simulates execution.

---

## 🔄 Pipeline

```text
BRD → Parser → Registry → Config Generator → Simulation → UI
```

---

## 📁 Folder Structure

```text
AI_orchestrator/
│
├── app/
│   ├── parser/
│   │   ├── brd_parser.py
│   │   ├── prompt_templates.py
│   │   └── __init__.py
│   │
│   ├── registry/
│   │   ├── adapters.json
│   │   ├── registry_loader.py
│   │   └── __init__.py
│   │
│   ├── engine/
│   │   ├── config_generator.py
│   │   ├── mapping_engine.py
│   │   └── __init__.py
│   │
│   ├── simulation/
│   │   ├── mock_apis.py
│   │   ├── simulator.py
│   │   └── __init__.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── ui/
│   └── app.py
│
├── data/
│   ├── sample_brd.txt
│   ├── sample_config_output.json
│   └── sample_output.json
│
├── test_parser.py
├── test_registry.py
├── test_config.py
├── test_simulation.py
│
├── .env
└── README.md
```

---

## 🧠 Detailed Explanation

---

## 🔹 1. `app/` (Core Backend Logic)

This folder contains the **main logic of the system**.

---

### 🔸 1.1 `parser/`

**Purpose:** Convert BRD (natural language) into structured JSON.

**Files:**

* **`brd_parser.py`**

  * Uses LLM (Gemini)
  * Extracts:

    * Services (KYC, GST, Fraud)
    * Field mappings

* **`prompt_templates.py`**

  * Contains prompts for LLM
  * Ensures structured output

---

### 🔸 1.2 `registry/`

**Purpose:** Store available APIs and configurations.

**Files:**

* **`adapters.json`**

  * Stores:

    * Services
    * Versions (v1, v2)
    * Endpoints

* **`registry_loader.py`**

  * Loads registry into Python dictionary

---

### 🔸 1.3 `engine/`

**Purpose:** Convert parsed BRD into executable configuration.

**Files:**

* **`config_generator.py`**

  * Selects services
  * Chooses API version
  * Builds integration config

* **`mapping_engine.py`**

  * Creates field mappings (source → target)
  * Handles schema transformation

---

### 🔸 1.4 `simulation/`

**Purpose:** Simulate real API behavior.

**Files:**

* **`mock_apis.py`**

  * Simulates:

    * KYC verification
    * GST validation
    * Fraud detection

* **`simulator.py`**

  * Applies mappings
  * Calls mock APIs
  * Aggregates results
  * Determines SUCCESS / FAILED

---

### 🔸 1.5 `main.py`

**Purpose:** Backend API using FastAPI.

* Exposes endpoints (e.g., `/simulate`)
* Connects:

  * Parser → Config → Simulation

---

## 🖥️ 2. `ui/`

**Purpose:** User Interface (Frontend)

**Files:**

* **`app.py`**

  * Built using Streamlit
  * Allows user to:

    * Enter BRD
    * Run pipeline
    * View:

      * Parsed output
      * Config
      * Simulation results

---

## 📂 3. `data/`

**Purpose:** Sample data for testing and debugging.

**Files:**

* `sample_brd.txt` → Example BRD input
* `sample_config_output.json` → Example config
* `sample_output.json` → Example simulation result

---

## 🧪 4. Test Files

**Purpose:** Unit testing each module.

* `test_parser.py` → Tests parsing
* `test_registry.py` → Tests registry
* `test_config.py` → Tests config generation
* `test_simulation.py` → Tests simulation

---

## 🔐 5. `.env`

**Purpose:** Store environment variables.

**Example:**

```text
GEMINI_API_KEY=your_api_key_here
```

⚠️ Should NOT be pushed to GitHub.

---

## 📘 6. `README.md`

**Purpose:** Project documentation.

Includes:

* Problem statement
* Architecture
* Setup instructions
* Usage guide

---

## 🔄 System Flow Summary

```text
1. User enters BRD in UI
2. Parser extracts services and mappings
3. Registry provides APIs
4. Config Generator builds configuration
5. Simulator executes mock APIs
6. Results displayed in UI
```

---

## ⭐ Key Highlights

* 🤖 AI-driven requirement understanding
* ⚙️ Automated API configuration
* 🧪 Mock API simulation
* 🧱 Modular architecture
* 🔌 Easily extendable with real APIs

---

## 🏁 End of Document

---
