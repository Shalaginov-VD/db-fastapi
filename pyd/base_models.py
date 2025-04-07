from pydantic import BaseModel, Field

class BaseProduct(BaseModel):
    id: int = Field(example = 1)
    name: str = Field(example = 'Молоко')

class BaseFilm(BaseModel):
    id: int = Field(example = 1)
    name: str = Field(example = 'Название фильма')
    rating: int = Field(gt = 0, example = 9)