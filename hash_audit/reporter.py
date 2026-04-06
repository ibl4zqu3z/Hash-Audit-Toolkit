import json
from pathlib import Path

def save_report(data: dict, output_path: str) -> None:
    Path(output_path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
