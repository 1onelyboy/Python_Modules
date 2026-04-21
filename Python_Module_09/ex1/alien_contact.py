from datetime import datetime
from enum import Enum
from typing import Optional, Self
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validator(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (>7.0) should include received messages"
            )

        return self


def main() -> None:

    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-04-18 23:46"),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
        print(f"""Alien Contact Log Validation
{"=" * 40}
Valid contact report:
ID: {valid_contact.contact_id}
Type: {valid_contact.contact_type.value}
Location: {valid_contact.location}
Signal: {valid_contact.signal_strength}/10
Duration: {valid_contact.duration_minutes} minutes
Witnesses: {valid_contact.witness_count}
Message: '{valid_contact.message_received}'""")
    except ValidationError as error:
        print(f"Unexpected error: {error}")

    print(f"""\n{"=" * 40}
Expected validation error:""")

    try:
        AlienContact(
            contact_id="AC_2026_002",
            timestamp=datetime.fromisoformat("2026-04-18 23:46"),
            location="Casablanca, Morocco",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=15,
            witness_count=2,
            is_verified=True,
        )
    except ValidationError as error:
        for item in error.errors():
            message = item["msg"].replace("Value error, ", "")
            print(message)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
