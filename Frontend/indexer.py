import os
import json
import urllib.parse

GITHUB_BASE_URL = "https://github.com/timosarkar/kql/blob/main"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/timosarkar/kql/main"

ROOT_DIR = ".."

queries = []

for dirpath, _, filenames in os.walk(ROOT_DIR):
    for f in filenames:
        if f.endswith(".kql"):
            rel_path = os.path.relpath(os.path.join(dirpath, f), ROOT_DIR)
            github_path = urllib.parse.quote(rel_path.replace("\\", "/"))
            
            github_url = f"{GITHUB_BASE_URL}/{github_path}"
            raw_url = f"{GITHUB_RAW_BASE}/{github_path}"

            # Extract optional description from first comment line
            description = ""
            try:
                with open(os.path.join(dirpath, f), "r", encoding="utf-8") as infile:
                    for line in infile:
                        line_stripped = line.strip()
                        if line_stripped.startswith("//") or line_stripped.startswith("#"):
                            description = line_stripped.lstrip("/#").strip()
                            break
            except Exception:
                pass

            queries.append({
                "name": f,
                "file": github_url,
                "raw": raw_url,
                "description": description
            })

output_path = os.path.join("Frontend", "queries.json")
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(queries, out, indent=2)

print(f"✅ Generated queries.json with {len(queries)} queries.")

