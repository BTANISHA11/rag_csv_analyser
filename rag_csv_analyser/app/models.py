from pydantic import BaseModel
from typing import Optional

class FileUpload(BaseModel):
    file_id: str
    file_name: str
    document: str  # CSV content