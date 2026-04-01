BRD_PARSER_PROMPT = """
You are an expert system that extracts structured data from a BRD.

Extract the following:

1. Services mentioned (KYC, GST, Fraud)
2. Field mappings in the format:
   source → target

IMPORTANT:
- Always extract ALL mappings explicitly mentioned
- Do NOT skip any mapping
- Ensure PAN is mapped if mentioned
- Ensure GSTIN is mapped if mentioned

Return ONLY valid JSON in this format:

{{
  "services": [
    {{"name": "KYC"}},
    {{"name": "GST"}}
  ],
  "mappings": [
    {{"source": "Name", "target": "full_name"}},
    {{"source": "PAN", "target": "pan_id"}},
    {{"source": "GSTIN", "target": "gst_number"}}
  ]
}}

BRD:
{brd_text}
"""