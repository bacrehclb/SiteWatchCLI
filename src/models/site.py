from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, HttpUrl, field_validator

"""a Site model, representing a site 
added by a user for monitoring."""
class Site(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    url: HttpUrl
    name: str
    create_date: datetime = Field(default_factory=datetime.now)

    @field_validator('id')
    def check_id(cls, value: UUID) -> UUID:
        if value == UUID("00000000-0000-0000-0000-000000000000"):
            raise ValueError("ID cannot be null")
        if value.version != 4:
            raise ValueError("ID must be UUID version 4")
        return value
    