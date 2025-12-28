from re import Pattern
from pydantic import BaseModel, Field

class arguments_model(BaseModel):
	port: int
	remote_url: str = Field(pattern=r"^https?://(?:\w+\.)+[a-zA-Z]{2,}$")


localport = 9123
domain = "http://godaddy.com"

