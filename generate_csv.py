import os
import glob
import pandas as pd
import re

APPLICATION_DIR = "./applications/2025-1/"
GITHUB_BASE = "https://github.com/CosmosContracts/delegations/blob/main/applications/2025-1/"
OUTPUT_CSV = "juno_delegation_review_template.csv"

COLUMNS = [
    "Validator Name",
    "dAPP Points", "dAPP Reasoning",
    "Mainnet Infra Points", "Mainnet Infra Reasoning",
    "Testnet Infra Points", "Testnet Infra Reasoning",
    "Governance Points", "Governance Reasoning",
    "Community Points", "Community Reasoning",
    "Open Points", "Open Reasoning",
    "Notes",
    "Markdown File URL"
]

def extract_moniker_from_table(content):
    # Search for the Validator details table and extract moniker
    validator_details_section = False
    for line in content.splitlines():
        if line.strip().lower().startswith("## validator details"):
            validator_details_section = True
            continue
        if validator_details_section:
            if "moniker" in line.lower():
                match = re.search(r"\|\s*\*\*Moniker\*\*\s*\|\s*(.*?)\s*\|", line, re.IGNORECASE)
                if match:
                    return match.group(1).strip()
            elif line.strip().startswith("## "):  # end of section
                break
    return None

def build_review_rows():
    rows = []

    for filepath in glob.glob(os.path.join(APPLICATION_DIR, "*.md")):
        filename = os.path.basename(filepath)
        if filename.lower() == "_template.md":
            continue

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        moniker = extract_moniker_from_table(content)
        if not moniker or moniker.lower() == "your moniker":
            moniker = os.path.splitext(filename)[0]  # fallback to filename

        markdown_url = GITHUB_BASE + filename

        row = {
            "Validator Name": moniker,
            "Markdown File URL": markdown_url,
            "dAPP Points": "", "dAPP Reasoning": "",
            "Mainnet Infra Points": "", "Mainnet Infra Reasoning": "",
            "Testnet Infra Points": "", "Testnet Infra Reasoning": "",
            "Governance Points": "", "Governance Reasoning": "",
            "Community Points": "", "Community Reasoning": "",
            "Open Points": "", "Open Reasoning": "",
            "Notes": ""
        }

        rows.append(row)

    return rows

def main():
    rows = build_review_rows()
    df = pd.DataFrame(rows, columns=COLUMNS)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"✅ CSV generated: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
