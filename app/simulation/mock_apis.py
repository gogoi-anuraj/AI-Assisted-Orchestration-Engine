# # app/simulation/mock_apis.py

# def mock_kyc_api(data):
#     if "full_name" in data and "pan_id" in data:
#         return {"status": "verified"}
#     return {"status": "failed", "reason": "missing fields"}


# def mock_gst_api(data):
#     if "gst_number" in data:
#         return {"gst_valid": True}
#     return {"gst_valid": False}


# def mock_fraud_api(data):
#     return {"risk_score": 0.2}


# app/simulation/mock_apis.py

import random
import re


# 🔹 KYC API (PAN + Name validation)
def mock_kyc_api(data):
    required_fields = ["full_name", "pan_id"]

    # Check missing fields
    for field in required_fields:
        if field not in data:
            return {
                "status": "failed",
                "reason": f"{field} missing"
            }

    pan = data["pan_id"]

    # PAN format check (ABCDE1234F)
    if not re.match(r"[A-Z]{5}[0-9]{4}[A-Z]{1}", pan):
        return {
            "status": "failed",
            "reason": "Invalid PAN format"
        }

    return {
        "status": "verified",
        "kyc_score": round(random.uniform(0.8, 1.0), 2),
        "name_match": True
    }


# 🔹 GST API (GSTIN validation)
def mock_gst_api(data):
    if "gst_number" not in data:
        return {
            "gst_valid": False,
            "reason": "GSTIN missing"
        }

    gst = data["gst_number"]

    # Simple GST format check
    if len(gst) != 15:
        return {
            "gst_valid": False,
            "reason": "Invalid GSTIN length"
        }

    return {
        "gst_valid": True,
        "business_name": "ABC Pvt Ltd",
        "status": "active"
    }


# 🔹 Fraud Detection API (risk scoring)
def mock_fraud_api(data):
    score = round(random.uniform(0, 1), 2)

    if score < 0.3:
        risk = "LOW"
    elif score < 0.7:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return {
        "risk_score": score,
        "risk_level": risk,
        "flagged": risk == "HIGH"
    }