from typing import Optional
from datetime import datetime, timezone

from sqlmodel import SQLModel, Field


class RepositorySettings(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    repository_id: int = Field(foreign_key="repository.id", index=True, unique=True)

    schedule_cron: str = "0 0 * * 1"  # weekly, example
    report_mode: str = "issue"        # "issue" now, "pr" later
    network_enabled: bool = True
    sandbox_timeout_seconds: int = 900
    target_branch: str = "main"

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))