import os
import json
import urllib.parse

GITHUB_BASE_URL = "https://github.com/timosarkar/kql"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/timosarkar/kql/refs/heads/main"

# Repo root (one level up from Frontend/)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_DIR = os.path.dirname(__file__)  # Frontend/

# Top-level folders to include in URLs (relative to ROOT_DIR)
TOP_FOLDERS = ["Sentinel", "XDR"]  # Add more if needed

queries = []

for folder_name in TOP_FOLDERS:
    folder_path = os.path.join(ROOT_DIR, folder_name)
    if not os.path.exists(folder_path):
        continue

    for dirpath, _, filenames in os.walk(folder_path):
        for f in filenames:
            if f.endswith(".kql"):
                # path relative to the folder itself
                rel_path = os.path.relpath(os.path.join(dirpath, f), ROOT_DIR)
                github_path = urllib.parse.quote(rel_path.replace("\\", "/"))

                github_url = f"{GITHUB_BASE_URL}/blob/main/{github_path}"
                raw_url = f"{GITHUB_RAW_BASE}/{github_path}"

                # optional description from first comment line
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

# Write queries.json inside Frontend/
output_path = os.path.join(OUTPUT_DIR, "queries.json")
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(queries, out, indent=2)

print(f"✅ Generated queries.json with {len(queries)} queries.")
