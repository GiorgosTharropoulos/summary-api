from pydantic import BaseModel
from pydantic.networks import AnyHttpUrl


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummaryUpdateSchema(SummaryPayloadSchema):
    summary: str
