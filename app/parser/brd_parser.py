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
model = genai.GenerativeModel("gemini-3-flash-preview")  # stable + fast


def parse_brd(brd_text):
    prompt = BRD_PARSER_PROMPT.format(brd_text=brd_text)

    response = model.generate_content(prompt)

    raw_output = response.text.strip()

    try:
        # Clean markdown if present
        if raw_output.startswith("```"):
            raw_output = raw_output.replace("```json", "").replace("```", "").strip()

        return json.loads(raw_output)

    except Exception as e:
        print("⚠️ JSON parsing failed:", e)
        print("Raw output:", raw_output)
        return raw_output