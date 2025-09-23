from pydantic import BaseModel, field_validator, ValidationError, Field


class spacexdata_info(BaseModel):
    class Headquarters(BaseModel):
        address: str
        city: str  
        state: str

    class Links(BaseModel):
        website: str
        flickr: str
        twitter: str
        elon_twitter: str

    name: str
    founder: str
    founded: int
    employees: int = Field (le=7000)
    vehicles: int
    launch_sites: int
    test_sites: int
    ceo: str
    cto: str
    coo: str
    cto_propulsion: str
    valuation: int
    headquarters: Headquarters
    links: Links
    summary: str
