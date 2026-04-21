from enum import Enum
from pydantic import BaseModel

class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class MyClass(BaseModel):
    type: ContactType


my_obj = MyClass(type="visual")

print(my_obj.type.value)