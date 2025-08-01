import dataclasses
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class OAuthState:
    session_id: str
    expires_at: datetime
    complete_page_url: Optional[str] = None
    complete_page_html: Optional[str] = None
    code: Optional[str] = None
    error: Optional[str] = None
    error_description: Optional[str] = None
