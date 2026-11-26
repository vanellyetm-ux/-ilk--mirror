from hashlib import sha256
from pathlib import Path
import os
import re
import tempfile
from .fixtures.phix_write_access import PHIX_WRITE_ACCESS

def evaluate(payload, status, authorized, spool, commit_sha=None, readback=None, readback_commit=None):
    digest = sha256(payload).hexdigest()
    spool = Path(spool)
    spool.mkdir(mode=0o700, parents=True, exist_ok=True)
    target = spool / digest
    with tempfile.NamedTemporaryFile(dir=spool, delete=False) as f:
        tmp = f.name
        try:
            f.write(payload)
            f.flush()
            os.fsync(f.fileno())
            os.replace(tmp, target)
        finally:
            if os.path.exists(tmp): os.unlink(tmp)
    if target.read_bytes() != payload:
        raise IOError('Payload preservation verification failed')
    accepted = bool(authorized and 200 <= status < 300 and commit_sha and re.fullmatch(r'[0-9a-f]{40}', commit_sha) and readback_commit == commit_sha and readback == payload)
    action = 'ANCHOR' if accepted else PHIX_WRITE_ACCESS['recovery'].get(status, 'VERIFY_READBACK' if authorized else 'RESTORE_WRITE_PERMISSION')
    return dict(http_status=status, sha256=digest, write_accepted=accepted, action=action, preserved_path=str(target))
