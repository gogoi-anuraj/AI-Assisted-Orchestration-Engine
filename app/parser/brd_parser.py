# # app/parser/brd_parser.py

# import os
# import json
# from dotenv import load_dotenv
# from google import genai

# from app.parser.prompt_templates import BRD_PARSER_PROMPT

# # Load API key
# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# def parse_brd(brd_text):
#     prompt = BRD_PARSER_PROMPT.format(brd_text=brd_text)

#     response = client.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents=prompt,
#     )

#     raw_output = response.text.strip()

#     try:
#         if raw_output.startswith("```"):
#             raw_output = raw_output.replace("```json", "").replace("```", "").strip()

#         return json.loads(raw_output)

#     except Exception as e:
#         print("⚠️ JSON parsing failed:", e)
#         print("Raw output:", raw_output)
#         return raw_output





# app/parser/brd_parser.py

import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

from app.parser.prompt_templates import BRD_PARSER_PROMPT

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")  # stable + fast



def fallback_parser(brd_text):
    """Simple rule-based fallback"""
    services = []
    mappings = []

    text = brd_text.lower()

    if "kyc" in text:
        services.append({"name": "KYC"})
    if "gst" in text:
        services.append({"name": "GST"})
    if "fraud" in text:
        services.append({"name": "Fraud"})

    if "name" in text:
        mappings.append({"source": "Name", "target": "full_name"})
    if "pan" in text:
        mappings.append({"source": "PAN", "target": "pan_id"})
    if "gst" in text:
        mappings.append({"source": "GSTIN", "target": "gst_number"})

    return {"services": services, "mappings": mappings}


def parse_brd(brd_text):
    prompt = BRD_PARSER_PROMPT.format(brd_text=brd_text)

    try:
        response = model.generate_content(prompt)
        raw_output = response.text.strip()

        if raw_output.startswith("```"):
            raw_output = raw_output.replace("```json", "").replace("```", "").strip()

        return json.loads(raw_output)

    except Exception as e:
        print("⚠️ Gemini failed, using fallback:", e)
        return fallback_parser(brd_text)

