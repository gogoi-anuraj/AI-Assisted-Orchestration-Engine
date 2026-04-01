from app.engine.mapping_engine import build_mapping


def normalize_service(name):
    name = name.lower()
    
    if "kyc" in name:
        return "KYC"
    elif "gst" in name:
        return "GST"
    elif "fraud" in name:
        return "Fraud"
    
    return name


def select_version(service_data):
    # simple logic: pick latest version
    versions = list(service_data.keys())
    return sorted(versions)[-1]


def generate_config(parsed, registry):
    config = {"integrations": []}

    mapping = build_mapping(parsed["mappings"])

    for service in parsed["services"]:
        raw_name = service["name"]
        name = normalize_service(raw_name)

        if name not in registry:
            print(f"⚠️ Skipping unknown service: {raw_name}")
            continue

        service_data = registry[name]

        version = select_version(service_data)
        endpoint = service_data[version]["endpoint"]

        config["integrations"].append({
            "service": name,
            "version": version,
            "endpoint": endpoint,
            "mapping": mapping
        })

    return config


