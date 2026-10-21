def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    headers = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = [field.strip() for field in line.split(",")]
        if headers is None:
            headers = fields
            continue
        if len(fields) != len(headers):
            continue
        rows.append(dict(zip(headers, fields)))
    return rows
def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind is not None:
            counts[kind] = counts.get(kind, 0) + 1
    return counts
def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row.get("тип") != kind:
            continue
        value = row.get("минуты", "")
        try:
            total += float(value.replace(",", ".").strip())
        except (ValueError, AttributeError):
            continue
    return round(total, 1)
def to_csv(counts: dict) -> str:
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
