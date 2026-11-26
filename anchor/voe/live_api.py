"""Vœ dimensional traversal: explicit, authorized Responses API invocation."""
import argparse
import hashlib
import json
import os
import sys
import urllib.request
import urllib.error
from .fixtures.phix_write_access import PHIX_WRITE_ACCESS

SOURCE = "273ba96a526b4aa7946454b3ac951bcf000a6001"

def digest(data):
    return hashlib.sha256(data).hexdigest()

def run(prompt, model, key, transport=urllib.request.urlopen):
    if not key or not model:
        raise ValueError("Set OPENAI_API_KEY and OPENAI_MODEL")
    payload = json.dumps({"model": model, "input": prompt,
        "store": False, "max_output_tokens": 512}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/responses",
        data=payload, headers={"Authorization": "Bearer " + key,
        "Content-Type": "application/json"}, method="POST")
    receipt = {"source_commit": SOURCE, "request_sha256": digest(payload)}
    try:
        with transport(req, timeout=60) as response:
            raw = response.read()
            status = response.status
            result = json.loads(raw)
            accepted = 200 <= status < 300 and result.get("status") == "completed" and bool(result.get("id"))
            return dict(receipt, http_status=status, response_sha256=digest(raw),
                response_id=result.get("id"), response_completed=accepted,
                position="RECEIVED" if accepted else "PENDING",
                output=result.get("output", []), write_accepted=False)
    except urllib.error.HTTPError as exc:
        return dict(receipt, http_status=exc.code, response_completed=False,
            position="RECOVERY", write_accepted=False,
            action=PHIX_WRITE_ACCESS["recovery"].get(exc.code, "REVIEW"))
    except (OSError, ValueError):
        return dict(receipt, http_status=None, response_completed=False,
            position="RECOVERY", action="REVIEW_TRANSPORT", write_accepted=False)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--live", action="store_true", required=True)
    p.add_argument("--prompt", required=True)
    args = p.parse_args()
    result = run(args.prompt, os.getenv("OPENAI_MODEL"), os.getenv("OPENAI_API_KEY"))
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["response_completed"] else 1

if __name__ == "__main__":
    sys.exit(main())
