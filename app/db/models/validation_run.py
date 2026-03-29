from typing import Optional
from datetime import datetime, timezone

from sqlmodel import SQLModel, Field


class ValidationRun(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    repository_id: int = Field(foreign_key="repository.id", index=True)

    trigger_type: str  # "schedule", "manual", "webhook"
    commit_sha: Optional[str] = None
    status: str = "queued"  # queued, running, passed, failed

    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

    summary: Optional[str] = None
    issue_url: Optional[str] = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))