import json
from datetime import datetime

def log_audit(data):
    entry = {
        "timestamp": str(datetime.now()),
        "analysis": data
    }

    with open("audit_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
