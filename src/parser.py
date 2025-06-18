def build_nested_dict(flat: dict) -> dict:
    result = {}
    for key, value in flat.items():
        parts = key.split("__")
        current = result
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value
    return result
