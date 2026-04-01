def build_mapping(parsed_mappings):
    mapping = {}

    for m in parsed_mappings:
        source = m["source"]
        target = m["target"]
        mapping[source] = target

    return mapping