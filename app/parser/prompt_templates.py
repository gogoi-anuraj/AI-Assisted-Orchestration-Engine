# app/parser/prompt_templates.py

BRD_PARSER_PROMPT = """
You are an AI system that extracts structured data from a Business Requirement Document (BRD).

Extract:
1. Services (KYC, GST, Fraud, etc.)
2. Whether each service is mandatory or optional
3. Field mappings (source → target)

Return ONLY valid JSON in this format:

{{
  "services": [
    {{"name": "KYC", "mandatory": true}}
  ],
  "mappings": [
    {{"source": "Name", "target": "full_name"}}
  ]
}}

Rules:
- Do not add explanations
- Do not add extra text
- Output strictly JSON

Use ONLY these service names:
- KYC
- GST
- Fraud

BRD:
{brd_text}
"""