import pydantic


class HozyainAPIDataTypeBase(pydantic.BaseModel):
    class Config:
        allow_population_by_field_name = True
