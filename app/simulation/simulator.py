# app/simulation/simulator.py

import random
import string

from app.simulation.mock_apis import (
    mock_kyc_api,
    mock_gst_api,
    mock_fraud_api
)


# 🔥 Helper functions to generate dynamic data

def generate_name():
    first_names = ["John", "Amit", "Rahul", "Priya", "Sneha"]
    last_names = ["Doe", "Sharma", "Kumar", "Das", "Singh"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"


def generate_pan():
    letters = ''.join(random.choices(string.ascii_uppercase, k=5))
    digits = ''.join(random.choices(string.digits, k=4))
    last = random.choice(string.ascii_uppercase)
    return f"{letters}{digits}{last}"


def generate_gstin(pan):
    state_code = str(random.randint(10, 35))
    return f"{state_code}{pan}1Z5"


def generate_dummy_input():
    pan = generate_pan()
    return {
        "Name": generate_name(),
        "PAN": pan,
        "GSTIN": generate_gstin(pan)
    }


def simulate_integration(config):
    results = []

    dummy_input = generate_dummy_input()

    for integration in config["integrations"]:
        service = integration["service"]
        mapping = integration["mapping"]

        # 🔥 Dynamic dummy input
        

        # 🔹 Apply mapping
        transformed_data = {}
        for src, tgt in mapping.items():
            if src in dummy_input:
                transformed_data[tgt] = dummy_input[src]

        # 🔹 Call mock APIs
        if service == "KYC":
            response = mock_kyc_api(transformed_data)

        elif service == "GST":
            response = mock_gst_api(transformed_data)

        elif service == "Fraud":
            response = mock_fraud_api(transformed_data)

        else:
            response = {"error": "Unknown service"}

        # 🔹 Debug logs
        print(f"\n🔹 Service: {service}")
        print("Input:", transformed_data)
        print("Response:", response)

        results.append({
            "service": service,
            "input": dummy_input,
            "transformed_data": transformed_data,
            "response": response
        })

    # Success logic
    success = True

    for r in results:
        service = r["service"]
        response = r["response"]

        if service == "KYC":
            if response.get("status") != "verified":
                success = False

        elif service == "GST":
            if not response.get("gst_valid", False):
                success = False

        elif service == "Fraud":
            if response.get("risk_level") == "HIGH":
                success = False

        elif "error" in response:
            success = False

    return {
        "results": results,
        "overall_status": "SUCCESS" if success else "FAILED"
    }