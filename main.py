from postcoder import Postcoder
from exceptions import *
from config import API_KEY

# Example usage
try:
    client = Postcoder(api_key=API_KEY)

    # Demo the bank validation endpoint
    bank_result = client.validate_bank_account("100000", "31510604", label="my-test-request")
    print(f"Valid: {bank_result.valid}") # All fields can be accessed this way
    print(f"Dump: {bank_result}")
    
    # Demo the email validation endpoint
    email_result = client.validate_email_address("test@example.com", label="my-test-request", timeout=1000)
    print(f"Valid: {email_result.valid}") # All fields can be accessed this way
    print(f"Dump: {email_result}")

    # Demo the mobile validation endpoint
    mobile_result = client.validate_mobile_phone_number("07500123456", label="my-test-request", country="")
    print(f"Valid: {mobile_result.valid}") # All fields can be accessed this way
    print(f"Dump: {mobile_result}")

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