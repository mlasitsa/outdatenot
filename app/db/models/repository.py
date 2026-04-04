from typing import Optional
from datetime import datetime, timezone

from sqlmodel import SQLModel, Field


class RepositoryModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    installation_id: int = Field(foreign_key="installation.id", index=True)

    github_repo_id: int = Field(index=True, unique=True)
    owner: str
    name: str
    full_name: str
    repository_url: str
    default_branch: str = "main"

    is_active: bool = True

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))