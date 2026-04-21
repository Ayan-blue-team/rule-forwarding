import requests
import json
import os
import urllib3

urllib3.disable_warnings()

# ═══════════════════════════════════════
#  QRadar Configuration
# ═══════════════════════════════════════
QRADAR_IP = "18.212.3.25"
TOKEN = "57e4bbc2-e588-4577-9904-0bc16beb7793"
VERSION = "12.0"

HEADERS = {
    "SEC": TOKEN,
    "Content-Type": "application/json",
    "Version": VERSION,
    "Accept": "application/json"
}

BASE_URL = f"https://{QRADAR_IP}/api"

# ═══════════════════════════════════════
#  Deploy Function
# ═══════════════════════════════════════
def deploy_rule(rule_data, filename):
    url = f"{BASE_URL}/analytics/rules"
    try:
        response = requests.post(
            url,
            headers=HEADERS,
            json=rule_data,
            verify=False
        )
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✅ SUCCESS: {rule_data['name']} (ID: {result.get('id', 'N/A')})")
        else:
            print(f"❌ FAILED: {filename} → {response.status_code}: {response.text[:200]}")
    except Exception as e:
        print(f"❌ ERROR: {filename} → {str(e)}")

# ═══════════════════════════════════════
#  Main
# ═══════════════════════════════════════
def main():
    rules_dir = os.path.join(os.path.dirname(__file__), '..', 'rules')
    rule_files = sorted([f for f in os.listdir(rules_dir) if f.endswith('.json')])

    print("=" * 50)
    print("  QRadar Custom Rules Deployment")
    print("=" * 50)
    print(f"  Target: {QRADAR_IP}")
    print(f"  Rules found: {len(rule_files)}")
    print("=" * 50)

    for filename in rule_files:
        filepath = os.path.join(rules_dir, filename)
        with open(filepath, 'r') as f:
            rule_data = json.load(f)
        deploy_rule(rule_data, filename)

    print("=" * 50)
    print("  Deployment Complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()