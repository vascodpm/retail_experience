
# Typing hints
from typing import Optional

# Configuration and helpers
from fastapi.encoders import jsonable_encoder
from src.config import CONFIG
from src.prompts.functions import ALL_ALLOWED_FUNCTIONS

# Importing schemas and hints
from src.schemas import ChatRequest

# Utils
import json


CFG_PROMPTS = CONFIG["prompts"]
CFG_CHAT = CFG_PROMPTS["chat"]
CFG_FUNCTIONS = CFG_PROMPTS["functions"]


# Utils
from pathlib import Path


## Creating handler
class PromptHandler():
    def __init__(
        self,
    ):
        pass

    def get_messages(self, prompt_request):
        """Gets the chatlog from the user and prepares the prompt for the system"""

        # Gets the system prompt and injects context
        system_prompt = Path(CFG_CHAT["filepath"]).read_text()

        chatlog = []

        # Retrieves the chat log
        chatlog = jsonable_encoder(prompt_request.query.history)
        
        chatlog = [
            {
                "role": message["role"],            # Keep the role
                "content": message["content"]       # Keep the content
            }
            if message["role"] != "function"        # If the role is not "function"
            else {
                "role": message["role"],            # Keep the role
                "content": message["content"],      # Keep the content
                "name": message["name"]             # Include the name if the role is "function"
            }
            for message in chatlog                  # Loop over each message in chatlog
            if message["role"] != "assistant"       # Exclude messages with role "assistant"
        ]


        print("chatlog", chatlog)
        # Merges all together
        messages = [{"role": "system", "content": system_prompt}] + chatlog

        return messages

    def prepare_response(self, response):
        """Formats the response from the system"""
        response = jsonable_encoder(response)

        # Get the content from the response
        content = response["choices"][0]["message"].get("content")

        # Check if content is None
        if content is None:
            return {
                "response": response["choices"][0]["message"],
                "function_call": response["choices"][0]["message"].get("function_call", None),
            }

        # Attempt to parse the content as JSON
        try:
            # Convert the string inside the content field to a JSON object
            content_json = json.loads(content)

            # Return the formatted response with HTML content
            return {
                "response": content_json.get("message", ""),  # Extract HTML message
                "product_ids": content_json.get("product_ids", []),  # Extract product IDs
                "function_call": response["choices"][0]["message"].get("function_call", None),
            }

        except json.JSONDecodeError:
            # Handle the case where content is not a valid JSON string
            return {
                "response": "Invalid JSON format in response content",
                "function_call": response["choices"][0]["message"].get("function_call", None),
            }
    
    def get_functions(self,):
        """Returns the functions signatures"""
        return ALL_ALLOWED_FUNCTIONS
