from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class RiskLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class FolderKind(str, Enum):
    CACHE = "Cache"
    TEMP = "Temp"
    SHADER_CACHE = "ShaderCache"
    LOGS = "Logs"
    SCREENSHOTS = "Screenshots"
    SUPPORT_DATA = "SupportData"
    SAVE_DATA = "SaveData"
    INSTALL_DATA = "InstallData"
    UNKNOWN = "Unknown"


class RecommendedAction(str, Enum):
    KEEP = "Keep"
    PURGE = "Purge"
    RELOCATE = "Relocate"
    REVIEW = "Review"


class RelocationState(str, Enum):
    NOT_RELOCATED = "NotRelocated"
    RELOCATED = "Relocated"
    BROKEN_LINK = "BrokenLink"
    NEEDS_VALIDATION = "NeedsValidation"


class LinkType(str, Enum):
    JUNCTION = "Junction"
    SYMLINK = "Symlink"


class TabulaItem(BaseModel):
    id: str
    display_name: str
    path: str
    normalized_path: str
    source_type: str = "KnownPath"
    owner_hint: Optional[str] = None
    kind: FolderKind = FolderKind.UNKNOWN
    risk_level: RiskLevel = RiskLevel.MEDIUM
    recommended_action: RecommendedAction = RecommendedAction.REVIEW
    size_bytes: int = 0
    size_human: str = "0 B"
    item_count: Optional[int] = None
    confidence: str = "Medium"
    notes: Optional[str] = None
    managed_by_tabula: bool = False
    relocation_state: RelocationState = RelocationState.NOT_RELOCATED
    original_path: Optional[str] = None
    target_path: Optional[str] = None
    link_type: Optional[LinkType] = None
    last_validated_at: Optional[datetime] = None


class RelocationRecord(BaseModel):
    id: str
    source_path: str
    target_path: str
    link_type: LinkType
    created_at: datetime
    validated: bool = False
    validation_notes: Optional[str] = None
    undo_supported: bool = True
    status: str = "Active"
