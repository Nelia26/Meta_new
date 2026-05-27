from __future__ import annotations

from pydantic import BaseModel, Field


class GridRow(BaseModel):
    stage: str = Field(..., min_length=1)
    audience: str = Field(..., min_length=1)
    targeting: str = Field(default="")
    offer: str = Field(default="")
    creative: str = Field(..., min_length=1)
    placements: str = Field(default="")
    optimization_event: str = Field(..., min_length=1)
    kpi: str = Field(..., min_length=1)
    budget: str = Field(default="")


class Config(BaseModel):
    project: str = Field(default="")
    rows: list[GridRow]
