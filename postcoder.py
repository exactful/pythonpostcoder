from exceptions import *
from models import AddressLookupResponse, BankValidationResponse, EmailValidationResponse, MobileValidationResponse
from json.decoder import JSONDecodeError
from typing import List, Optional
from urllib.parse import quote
import requests

class Postcoder:

    def __init__(self, api_key):

        if api_key.strip() == "":
            raise PostcoderParameterError("Required parameter is missing: api_key")
        
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json"
        }

    def _handle_response(self, response):

        if response.status_code == 400:    
            raise PostcoderParameterError(f"{response.text or 'Unknown reason'} | 400 {response.request.url}")
        elif response.status_code == 403:
            raise PostcoderAccountError(f"{response.text or 'Unknown reason'} | 403 {response.request.url}")
        elif response.status_code == 404:
            raise PostcoderEndpointNotFoundError(f"Endpoint not found | 404 {response.request.url}")
        elif response.status_code == 405:
            raise PostcoderMethodNotAllowedError(f"Method not allowed | 405 {response.request.url}")
        elif response.status_code == 500:
            raise PostcoderServerError(f"Server error | 500 {response.request.url}")
        
        data = None
        try:
            data = response.json()
        except JSONDecodeError as e:
            raise PostcoderJSONError(f"JSON expected but not found | {e}")

        return data

    def lookup_address(self, 
                       query: str,
                       country_code: str,
                       label: str,
                       page: Optional[int]=0) -> List[AddressLookupResponse]:
        
        # Raise if query is None or empty
        if query is None or query.strip() == "":
            raise PostcoderParameterError("Required parameter is missing: query")
        
        # Raise if country_code is None or empty
        if country_code is None or country_code.strip() == "":
            raise PostcoderParameterError("Required parameter is missing: country_code")

        # Raise if label is None or empty
        if label is None or label.strip() == "":
            raise PostcoderParameterError("Required parameter is missing: label")

        # Raise if page is not an integer
        if not isinstance(page, int):
            raise PostcoderParameterError("Parameter is not an integer: page")

        # URL encode string parameters with % encoding
        encoded_query = quote(query)
        encoded_country_code = quote(country_code)
        encoded_label = quote(label)

        # Construct request 
        url = f"https://ws.postcoder.com/pcw/{self.api_key}/address/{encoded_country_code}/{encoded_query}?lines=5&include=posttown,postcode&exclude=country&page={page}"
        
        params = {
            "identifier": encoded_label
            }

        # Do POST request
        response = requests.get(url, headers=self.headers, params=params)

        # Check response for errors
        data = self._handle_response(response)
        
        # Map JSON response to List[AddressLookupResponse model] 
        address_lookup_response = None
        try:
            address_lookup_response = [AddressLookupResponse(**item) for item in data]
        except Exception as e:
            raise PostcoderJSONError(f"Could not map JSON to expected structure | {e}")

        return address_lookup_response

    def validate_bank_account(self, 
                       account_number: str, 
                       sort_code: str,
                       label: str) -> BankValidationResponse:
        
        # Raise if account_number is None or empty
        if account_number is None or account_number.strip() == "":
            raise PostcoderParameterError("Required parameter is missing: account_number")

        # Raise if sort_code is None or empty
        if sort_code is None or sort_code.strip() == "":
            raise PostcoderParameterError("Required parameter is missing: sort_code")

        # Raise if label is None or empty
        if label is None or label.strip() == "":
            raise PostcoderParameterError("Required parameter is missing: label")

        # URL encode string parameters with % encoding
        encoded_account_number = quote(account_number)
        encoded_sort_code = quote(sort_code)
        encoded_label = quote(label)

        # Construct request 
        url = f"https://ws.postcoder.com/pcw/{self.api_key}/bank"
        
        body = {
            "sortcode": encoded_account_number,
            "accountnumber": encoded_sort_code
            }

        params = {
            "identifier": encoded_label
            }

        # Do POST request
        response = requests.post(url, headers=self.headers, json=body, params=params)

        # Check response for errors
        data = self._handle_response(response)
        
        # Map JSON response to BankValidationResponse model
        bank_validation_response = None
        try:
            bank_validation_response = BankValidationResponse(**data)
        except Exception as e:
            raise PostcoderJSONError(f"Could not map JSON to expected structure | {e}")

        return bank_validation_response

    def validate_email_address(self, 
                               email_address: str, 
                               label: str, 
                               timeout: Optional[int]=1000) -> EmailValidationResponse:
        
        # Raise if email_address is None or empty
        if email_address is None or email_address.strip() == "":
            raise PostcoderParameterError("Required parameter is None or empty: email_address")

        # Raise if label is None or empty
        if label is None or label.strip() == "":
            raise PostcoderParameterError("Required parameter is None or empty: label")

        # Raise if timeout is not an integer
        if not isinstance(timeout, int):
            raise PostcoderParameterError("Parameter is not an integer: timeout")

        # URL encode string parameters with % encoding
        encoded_email_address = quote(email_address)
        encoded_label = quote(label)

        # Construct request 
        url = f"https://ws.postcoder.com/pcw/{self.api_key}/email/{encoded_email_address}"
        
        params = {
                "identifier": encoded_label,
                "timeout": timeout
            }

        # Do request
        response = requests.get(url, headers=self.headers, params=params)

        # Check response for errors
        data = self._handle_response(response)
        
        # Map JSON response to EmailValidationResponse model
        email_validation_response = None
        try:
            email_validation_response = EmailValidationResponse(**data)
        except Exception as e:
            raise PostcoderJSONError(f"Could not map JSON to expected structure | {e}")

        return email_validation_response

    def validate_mobile_phone_number(self, 
                                     mobile_phone_number: str, 
                                     label: str, 
                                     country: Optional[str]=None) -> MobileValidationResponse:
       
        # Raise if account_number is None or empty
        if mobile_phone_number is None or mobile_phone_number.strip() == "":
            raise PostcoderParameterError("Required parameter is missing: mobile_phone_number")
        
         # Raise if country is not None but is empty
        if country is not None and len(country) and country.strip() == "":
            raise PostcoderParameterError("Optional parameter contained whitespace only: country")

        # URL encode string parameters with % encoding
        encoded_mobile_phone_number = quote(mobile_phone_number)

        # Construct request
        url = f"https://ws.postcoder.com/pcw/{self.api_key}/mobile/{encoded_mobile_phone_number}"
        
        params = {
            "identifier": label,
            **({"country": country} if country is not None and len(country) else {})
        }

        # Do request
        response = requests.get(url, headers=self.headers, params=params)
        
        # Check response for errors
        data = self._handle_response(response)
        
        # Map JSON response to MobileValidationResponse model
        mobile_validation_response = None
        try:
            mobile_validation_response = MobileValidationResponse(**data)
        except Exception as e:
            raise PostcoderJSONError(f"Could not map JSON to expected structure | {e}")

        return mobile_validation_response