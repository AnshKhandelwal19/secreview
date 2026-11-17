from enum import StrEnum
from pydantic import BaseModel, Field

class Severity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Finding(BaseModel):
    line: int
    category: str
    cwe: str | None = Field(
        pattern=r"^CWE-\d+$",
        description="CWE identifier such as 'CWE-89'. Use null only if no CWE applies.",
    )
    severity: Severity
    suggested_fix: str = Field(description="A suggestion for how to fix this vulnerability")
    line: int = Field(description="Line number exactly as shown in the left column of the code")
    explanation: str = Field(description="How an attacker could exploit this, in one or two sentences")

class ReviewResponse(BaseModel):
    findings: list[Finding]
