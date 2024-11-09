# Python client for Postcoder

An unofficial Python client for [Postcoder](https://postcoder.com), the popular API for address lookup and form validation.

> ⚠️ This project is not affiliated with or supported by the Postcoder team. Use at your own risk.

> 🚧 This project is currently in development.

## Features

Currently supports the following Postcoder features:

- Bank account validation
- Email address validation
- Mobile phone number validation
- TODO: Address and postcode lookup

## Installation

```
git clone https://github.com/exactful/pythonpostcoder.git
cd pythonpostcoder
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

First, import the client and initialise it with your API key:

```python
from postcoder import Postcoder

client = Postcoder(api_key="YOUR-API-KEY")
```

### Global address and postcode lookup

```python
# Demo the address lookup endpoint
address_result = client.lookup_address("nr1 1ne", "uk", page=0, label="my-test-request")

print(f"Dump: {address_result}")

# Iterate each address
for address in address_result:
    
    print(address.summaryline) if address.summaryline is not None else None # For use in a drop-down list, for example
    
    print(address.addressline1) if address.addressline1 is not None else None
    print(address.addressline2) if address.addressline2 is not None else None
    print(address.addressline3) if address.addressline3 is not None else None
    print(address.addressline4) if address.addressline4 is not None else None
    print(address.addressline5) if address.addressline5 is not None else None
    
    print(f"Next page of results: {address.nextpage}") if address.nextpage is not None else None
    print("")
```

### Bank account validation

```python
result = client.validate_bank_account(
    account_number="100000",
    sort_code="31510604",
    label="my-test-request"
)

print(f"Valid: {bank_result.valid}") # All fields can be accessed this way
print(f"Dump: {bank_result}")
```

### Email address validation

```python
result = client.validate_email_address(
    email_address="test@example.com",
    label="my-test-request",
    timeout=1000  # Optional, defaults to 1000ms
)

print(f"Valid: {email_result.valid}") # All fields can be accessed this way
print(f"Dump: {email_result}")
```

### Mobile phone number validation

```python
result = client.validate_mobile_phone_number(
    mobile_phone_number="07500123456",
    label="my-test-request",
    country="44"  # Optional
)

print(f"Valid: {mobile_result.valid}") # All fields can be accessed this way
print(f"Dump: {mobile_result}")
```

## Error handling

The client includes comprehensive error handling for different scenarios and API responses:

```python
try:
    result = client.validate_email_address(...)
except PostcoderParameterError as e:
    print("Postcoder - Parameter error")
    print(e)
except PostcoderAccountError as e:
    print("Postcoder - Account error")
    print(e)
except PostcoderEndpointNotFoundError as e:
    print("Postcoder - Endpoint not found error")
    print(e)
except PostcoderMethodNotAllowedError as e:
    print("Postcoder - Method not allowed error")
    print(e)
except PostcoderServerError as e:
    print("Postcoder - Server error")
    print(e)
except PostcoderJSONError as e:
    print("Postcoder - JSON error")
    print(e)
except Exception as e:
    print("General error")
    print(e)
```

## Contributing

Contributions are welcome. Please feel free to submit a PR.
