from pydantic import BaseModel, Field
from typing import List

# request of questions
class Message(BaseModel):
    role:str = "User"
    content:str = Field(
        example="Write your query"
    )

class ChatRequest(BaseModel):
    messages:list[Message]

# response of questions
