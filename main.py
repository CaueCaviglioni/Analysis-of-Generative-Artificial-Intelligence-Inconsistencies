from config import API_KEY, MODEL
from chat_client import ChatClient
from utils.messaging import (
    is_negative_response, 
    print_message
)

def main():
    client = ChatClient(api_key=API_KEY, model=MODEL)
    
    user_input = input("You: ")
    assistant_response = client.add_and_get_response("user", user_input)
    print_message("Mistrall", assistant_response)
    
    if is_negative_response(assistant_response):
        assistant_response = client.handle_negative_response()
        print_message("Mistrall", assistant_response)
    
    summary_response = client.summarize_response()
    print_message("Summary", summary_response)
    
if __name__ == "__main__":
    main()