from typing import Optional
from datetime import datetime, timezone

from sqlmodel import SQLModel, Field


class Installation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    github_installation_id: int = Field(index=True, unique=True)
    account_login: str
    account_type: str  # "User" or "Organization"

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))