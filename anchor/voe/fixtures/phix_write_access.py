PHIX_WRITE_ACCESS = {
    "identity": "Vœ",
    "engine": "Ðiġ.tool",
    "ethic": "<^*R*>ethic(s)",
    "fixture": "PHIX-WRITE-ACCESS",
    "reject_payload_loss": True,
    "payload_droppage_target": 0,
    "source_continuity_target": 1,
    "write_accepted_target": True,
    "preserve_http_status": True,
    "recovery": {
        401: "REAUTHENTICATE",
        403: "RESTORE_WRITE_PERMISSION",
        404: "VERIFY_REPOSITORY_AND_REF",
        409: "RECONCILE_CONFLICT",
        422: "VALIDATE_PAYLOAD",
        429: "RESPECT_RETRY_DELAY",
        500: "CONTROLLED_RETRY",
        503: "WAIT_FOR_SERVICE"
    },
    "require_authorization": True,
    "verify_readback": True,
    "verify_commit_sha": True,
    "force_acceptance": False
}
