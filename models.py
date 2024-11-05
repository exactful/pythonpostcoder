from pydantic import BaseModel
from typing import Optional

class StrMixin:
    def _str_(self) -> str:
        fields = {k: v for k, v in self._dict_.items() if v is not None}
        return ", ".join(f"{key}={value}" for key, value in fields.items())

class BankValidationResponse(StrMixin, BaseModel):
    valid: Optional[bool] = None
    stateid: Optional[int] = None
    sortcode: Optional[str] = None
    accountnumber: Optional[str] = None
    directdebits: Optional[bool] = None
    fasterpayments: Optional[bool] = None
    chaps: Optional[bool] = None
    bacs: Optional[bool] = None
    bankbic: Optional[str] = None
    branchbic: Optional[str] = None
    bankname: Optional[str] = None
    branchname: Optional[str] = None
    addressline1: Optional[str] = None
    addressline2: Optional[str] = None
    addressline3: Optional[str] = None
    addressline4: Optional[str] = None
    posttown: Optional[str] = None
    postcode: Optional[str] = None
    phone1: Optional[str] = None
    phone2: Optional[str] = None

class EmailValidationResponse(StrMixin, BaseModel):
    warning: Optional[str] = None
    state: str
    valid: bool
    score: str
    processtime: str

class MobileValidationResponse(StrMixin, BaseModel):
    stateid: Optional[int] = None
    state: Optional[str] = None
    on: Optional[bool] = None
    valid: Optional[bool] = None
    number: Optional[str] = None
    type: Optional[str] = None
    networkname: Optional[str] = None
    networkcode: Optional[str] = None
    countrycode: Optional[str] = None
    countryname: Optional[str] = None
