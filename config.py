import os

# Try to get API key from environment variable first
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)

# If not found in environment, prompt the user
if not OPENAI_API_KEY:
    OPENAI_API_KEY = input("Please enter your OpenAI API key: ")
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"