def build_mapping(mappings_list):
    mapping = {}

    for m in mappings_list:
        mapping[m["source"]] = m["target"]

    
    if "PAN" not in mapping:
        mapping["PAN"] = "pan_id"

    if "GSTIN" not in mapping:
        mapping["GSTIN"] = "gst_number"

    if "Name" not in mapping:
        mapping["Name"] = "full_name"

    return mapping