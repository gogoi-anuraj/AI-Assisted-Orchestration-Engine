# 📄 BRD Prompts and Their Essence

## 📌 Overview

This document contains sample **Business Requirement Document (BRD)** prompts to test the **AI Integration Orchestrator**.

Each prompt demonstrates different scenarios such as:

* ✅ Successful integration
* ⚠️ Partial mapping
* ❓ Ambiguity handling
* ❌ Failure cases

---

## 🟢 1. Standard Successful Case

### BRD

```
The system must integrate with KYC and GST verification services for onboarding users. 
Fraud detection should also be included for risk assessment.

The customer's Name should map to full_name. 
The PAN number should map to pan_id. 
The GSTIN should map to gst_number.
```

### Essence

* Complete and clear requirements
* Multiple services (KYC, GST, Fraud)
* Proper mappings

**Expected Result:** ✅ SUCCESS

---

## 🟢 2. Natural Language Variation

### BRD

```
We need to verify users using KYC and validate their GST details. 
Fraud checks should also be performed.

Customer Name corresponds to full_name, PAN corresponds to pan_id, 
and GST ID corresponds to gst_number.
```

### Essence

* Same intent, different wording
* Tests NLP flexibility

**Expected Result:** ✅ SUCCESS

---

## 🟡 3. Partial Mapping Case

### BRD

```
The system must integrate with KYC and GST.

Name should map to full_name.
```

### Essence

* Missing PAN and GST mappings
* Incomplete definition

**Expected Result:** ⚠️ PARTIAL FAILURE

---

## 🔴 4. Missing Required Field Case

### BRD

```
The system must integrate with KYC.

User Name should be mapped to full_name.
```

### Essence

* PAN missing
* KYC requires PAN

**Expected Result:** ❌ FAILURE

---

## 🟡 5. Ambiguous Requirement Case

### BRD

```
The system should integrate identity verification and tax validation services. 
Fraud checks are optional.

User Name should be used for full_name. 
User ID should be mapped appropriately.
```

### Essence

* Ambiguous service names
* Unclear mapping

**Expected Result:** ⚠️ Depends on parser

---

## 🟡 6. Unknown Service Case

### BRD

```
The system must integrate with Credit Score and KYC services.

Name maps to full_name. 
PAN maps to pan_id.
```

### Essence

* Unknown service (Credit Score)
* Partial processing

**Expected Result:** ⚠️ PARTIAL SUCCESS

---

## 🟢 7. Fraud-Only Case

### BRD

```
The system must perform fraud detection on all users.

Name maps to full_name.
```

### Essence

* Single service
* Minimal mapping

**Expected Result:** ✅ SUCCESS (if low risk)

---

## 🟢 8. Stress Test Case

### BRD

```
The system must integrate KYC, GST, and Fraud detection.

Customer Name maps to full_name. 
PAN maps to pan_id. 
GSTIN maps to gst_number. 
Email maps to email_id.
```

### Essence

* Extra fields included
* Tests flexibility

**Expected Result:** ✅ SUCCESS

---

## 🔴 9. Failure Scenario (Invalid Logic)

### BRD

```
The system must integrate with GST.

Only Name should be mapped.
```

### Essence

* Missing GSTIN
* Invalid configuration

**Expected Result:** ❌ FAILURE

---

## 🟢 10. Realistic Enterprise Case

### BRD

```
For customer onboarding, the system must integrate KYC verification, 
GST validation, and fraud detection services.

Customer Name maps to full_name. 
PAN number maps to pan_id. 
GST number maps to gst_number.

Fraud detection should be used to flag high-risk users.
```

### Essence

* Real enterprise workflow
* Clear mappings
* Risk logic included

**Expected Result:** ✅ SUCCESS

---

## 📊 Summary

These prompts help evaluate:

* 🧠 NLP parsing capability
* 🔄 Mapping accuracy
* ⚠️ Error handling
* 📈 System robustness
* 🏢 Real-world applicability

---

## 🏁 Conclusion

These BRD scenarios demonstrate how the system handles:

* Structured vs unstructured input
* Complete vs incomplete data
* Valid vs invalid configurations

They are ideal for:

* 🎤 Demo presentations
* 🧪 Testing
* 📂 Documentation

---
