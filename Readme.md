# 🚀 AI Integration Orchestrator

## 📌 Project Overview

The **AI Integration Orchestrator** is an intelligent system that automates the process of converting a **Business Requirement Document (BRD)** into:

* Structured service requirements
* API integration configurations
* Simulated execution results

👉 It eliminates manual integration effort and enables rapid onboarding of enterprise systems.

---

## ❗ Problem Statement

In enterprise environments:

* Business teams provide requirements in natural language (BRDs)
* Developers manually:

  * Interpret requirements
  * Identify services (KYC, GST, Fraud)
  * Map fields
  * Build integrations
  * Test APIs

### 🔴 Challenges

* Time-consuming ⏳
* Error-prone ❌
* Requires domain expertise 🧠
* Hard to scale 📈

---

## 💡 Proposed Solution

We built an **AI-driven orchestration platform**:

```text
BRD → AI Parsing → Config Generation → Simulation → UI Output
```

---

## 🧠 System Architecture

```text
          ┌──────────────┐
          │   BRD Input  │
          └──────┬───────┘
                 ↓
        ┌──────────────────┐
        │   AI Parser      │
        └──────┬───────────┘
               ↓
    ┌──────────────────────┐
    │ Integration Registry │
    └──────┬───────────────┘
           ↓
   ┌────────────────────────┐
   │ Config Generator       │
   └──────┬─────────────────┘
          ↓
   ┌────────────────────────┐
   │ Simulation Engine      │
   └──────┬─────────────────┘
          ↓
   ┌────────────────────────┐
   │ UI (Streamlit)         │
   └────────────────────────┘
```

---

## 🧱 Development Phases

---

### 🔹 Phase 0: Planning & Setup

* Defined problem scope
* Designed system architecture
* Created folder structure
* Setup environment and dependencies

---

### 🔹 Phase 1: BRD Parsing Engine (AI Layer)

**Goal:** Convert natural language into structured data

#### Implementation:

* Used Gemini API for NLP parsing
* Designed prompt templates
* Extracted:

  * Services (KYC, GST, Fraud)
  * Field mappings

#### Output Example:

```json
{
  "services": [{"name": "KYC"}, {"name": "GST"}],
  "mappings": [
    {"source": "Name", "target": "full_name"}
  ]
}
```

---

### 🔹 Phase 2: Integration Registry

**Goal:** Maintain a catalog of available APIs

#### Implementation:

* Created `adapters.json`
* Stored:

  * Services
  * Versions
  * Endpoints

#### Example:

```json
"KYC": {
  "v1": {"endpoint": "/kyc/v1"},
  "v2": {"endpoint": "/kyc/v2"}
}
```

---

### 🔹 Phase 3: Auto-Configuration Engine

**Goal:** Generate integration configs automatically

#### Implementation:

* Built `config_generator.py`

* Selected:

  * Service
  * Latest version
  * Endpoint

* Used `mapping_engine.py` for field mapping

#### Output:

```json
{
  "service": "KYC",
  "version": "v2",
  "mapping": {...}
}
```

---

### 🔹 Phase 4: Simulation & Testing Framework

**Goal:** Simulate real API behavior

#### Implementation:

* Created mock APIs:

  * KYC validation
  * GST verification
  * Fraud scoring

* Built `simulator.py`:

  * Applies mapping
  * Calls APIs
  * Aggregates results

#### Features:

* Validation logic
* Failure scenarios
* Risk scoring

---

### 🔹 Phase 5: Backend APIs (FastAPI)

**Goal:** Expose system as API

#### Implementation:

* Built `/simulate` endpoint
* Connected:

  * Parser
  * Registry
  * Config generator
  * Simulation

---

### 🔹 Phase 6: UI Development (Streamlit)

**Goal:** Build interactive frontend

#### Features:

* Input BRD
* Run pipeline
* Display:

  * Parsed output
  * Config
  * Simulation results

---

## 📂 Project Structure

```text
AI_orchestrator/
├── app/
│   ├── parser/
│   ├── registry/
│   ├── engine/
│   ├── simulation/
│   └── main.py
├── ui/
│   └── app.py
├── data/
├── test_*.py
├── .env
└── README.md
```

---

## ⚙️ Installation Guide

### 1. Clone Repository

```bash
git clone <repo-url>
cd AI_orchestrator
```

---

### 2. Create Environment

```bash
conda create -n ai_env python=3.10
conda activate ai_env
```

---

### 3. Install Dependencies

```bash
pip install streamlit fastapi uvicorn python-dotenv google-generativeai
```

---

### 4. Setup API Key

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 🚀 Running the Project

### Run UI

```bash
streamlit run ui/app.py
```

---

### Run Backend (Optional)

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Example Input

```text
The system must integrate with KYC and GST.
Name maps to full_name. PAN maps to pan_id.
```

---

## ✅ Example Output

```json
{
  "overall_status": "SUCCESS"
}
```

---

## 🔄 Real-World Applicability

This system can be used for:

* Fintech onboarding
* API orchestration platforms
* Enterprise integration systems
* Low-code automation tools

---

## 🔥 Key Features

* AI-driven requirement understanding
* Automated configuration generation
* API simulation framework
* Modular architecture
* Scalable design

---

## 🚀 Future Enhancements

* Real API integration
* Authentication & security
* Multi-tenant support
* Config diff comparison
* Workflow orchestration (n8n)

---

## 🏆 Conclusion

The AI Integration Orchestrator demonstrates how AI can transform natural language requirements into executable integration pipelines, significantly improving efficiency and scalability in enterprise systems.

---

## 👨‍💻 Author

Anuraj Gogoi

---

## 📜 License

MIT License
