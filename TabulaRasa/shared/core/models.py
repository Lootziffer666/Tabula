from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class RiskLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class PurgeKind(str, Enum):
    TEMP = "Temp"
    CACHE = "Cache"
    SHADER_CACHE = "ShaderCache"
    LOGS = "Logs"
    THUMBNAILS = "Thumbnails"
    SCREENSHOTS = "Screenshots"
    CAPTURES = "Captures"
    INSTALLER_LEFTOVERS = "InstallerLeftovers"
    UPDATER_RESIDUE = "UpdaterResidue"
    APP_RESIDUE = "AppResidue"
    ORPHANED_APP_DATA = "OrphanedAppData"
    UNKNOWN = "Unknown"


class RecommendedAction(str, Enum):
    PURGE = "Purge"
    REVIEW = "Review"
    KEEP = "Keep"


class ExecutionMode(str, Enum):
    DRY_RUN = "DryRun"
    SAFE = "RecycleBinPreferred"
    AGGRESSIVE = "PermanentDelete"


class PurgeItem(BaseModel):
    id: str
    selected: bool = False
    display_name: str
    path: str
    owner_hint: Optional[str] = None
    kind: PurgeKind
    risk_level: RiskLevel
    recommended_action: RecommendedAction
    size_bytes: int
    size_human: str
    confidence: str = "Medium"
    detection_source: str = "KnownPath"
    notes: Optional[str] = None
    review_required: bool = False


class PurgeRun(BaseModel):
    id: str
    started_at: datetime
    finished_at: Optional[datetime] = None
    mode: ExecutionMode = ExecutionMode.DRY_RUN
    selected_item_count: int = 0
    estimated_bytes: int = 0
    deleted_bytes: Optional[int] = None
    skipped_count: int = 0
    failed_count: int = 0
    log_path: str
