from openai import OpenAI
import os

# Replace with your OpenAI API key
api_key = 'your-API-key'

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def check_api_key():
    try:
        # Make a simple API call to test the key
        response = client.models.list()
        
        # If we get here, the API call was successful
        print("API Key is valid and active!")
        print("Available models:")
        for model in response.data:
            print(f"- {model.id}")
        
        # Check account balance (if applicable)
        try:
            balance = client.billing.get_balance()
            print(f"Current account balance: ${balance.total_available:.2f}")
        except Exception as e:
            print("Unable to retrieve balance information.")
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        print("API Key is invalid or there was an issue with the request.")
        return False

if __name__ == "__main__":
    check_api_key()
