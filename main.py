import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# Load environment variables from .env file
load_dotenv()


def test_azure_connection():
    """Test basic connection to Azure OpenAI"""

    # Create Azure OpenAI client
    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        temperature=0.7
    )

    # Simple test message
    test_message = "Hello! Please respond with 'Connection successful' if you can read this."

    try:
        # Send message and get response
        response = llm.invoke(test_message)
        print(f"✅ Connection successful!")
        print(f"Response: {response.content}")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False


if __name__ == "__main__":
    print("Testing Azure OpenAI connection...")
    test_azure_connection()
