from typing import Optional
from datetime import datetime, timezone

from sqlmodel import SQLModel, Field


class ValidationStep(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    validation_run_id: int = Field(foreign_key="validationrun.id", index=True)

    step_order: int
    step_name: str
    command: str

    status: str = "pending"   # pending, running, passed, failed
    exit_code: Optional[int] = None

    stdout_excerpt: Optional[str] = None
    stderr_excerpt: Optional[str] = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))