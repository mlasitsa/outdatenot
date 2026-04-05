import hashlib
import hmac
import json
from fastapi import APIRouter, HTTPException, Request, Response, status
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.config import settings
from app.services.installation_service import InstallationService


class GitHubService():
    def __init__(self, session: AsyncSession):
        self.installation_service = InstallationService(session)

    def _verify_github_signature(self, body: bytes, signature_header: str | None) -> None:
        if not signature_header or not signature_header.startswith("sha256="):
            raise HTTPException(status_code=401, detail="Missing or invalid signature")

        expected = hmac.new(
            settings.github_webhook_secret.encode("utf-8"),
            body,
            hashlib.sha256,
        ).hexdigest()

        received = signature_header.removeprefix("sha256=")

        if not hmac.compare_digest(expected, received):
            raise HTTPException(status_code=401, detail="Bad signature")

    async def github_webhook(self, request: Request) -> dict:
        body = await request.body()

        self._verify_github_signature(
            body,
            request.headers.get("X-Hub-Signature-256"),
        )

        event = request.headers.get("X-GitHub-Event", "")
        payload = json.loads(body)

        if event == "installation":
            action = payload.get("action")
            installation = payload.get("installation") or {}
            account = installation.get("account") or {}

            if action == "created":
                # TODO: InstallationService(...).upsert_from_github(...)
                # github_installation_id = installation["id"]
                # account_login = account.get("login")
                # account_type = account.get("type")
                pass
            elif action == "deleted":
                # TODO: mark removed / delete by github installation id
                pass

        elif event == "installation_repositories":
            # TODO: sync added/removed repos for installation["id"]
            pass

        # GitHub mainly needs 2xx quickly; keep response tiny.
        return {"ok": True}
