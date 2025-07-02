from pydantic import BaseModel

class EditPDFRequest(BaseModel):
    new_value: str
    new_name: str
    new_cpf: str
    new_bank: str
    new_agency: str | None
    new_account: str | None
