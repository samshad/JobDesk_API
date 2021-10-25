from pydantic import BaseModel
from typing import Optional


class JobData(BaseModel):
    data: str
    uid: str
    lc: str
    geoLat: Optional[str] = None
    geoLong: Optional[str] = None
    jsonJobLocation: dict


class ProfileData(BaseModel):
    data: str
    uid: str


class JobTitle(BaseModel):
    jobtitle: str
