import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# Load environment variables
load_dotenv()


class ContextTranslator:
    """Simple context-aware translator"""

    def __init__(self):
        """Initialize the translator with Azure OpenAI client"""
        self.llm = AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            temperature=0.3  # Lower temperature for more consistent translations
        )

    def translate(self, text, source_lang="English", target_lang="Bulgarian", context="general"):
        """
        Translate text with context awareness

        Args:
            text (str): Text to translate
            source_lang (str): Source language
            target_lang (str): Target language
            context (str): Translation context (general, business, technical, personal)

        Returns:
            str: Translated text
        """

        # Create basic prompt with context
        prompt = f"""
        You are a professional translator. Translate the following text from {source_lang} to {target_lang}.

        Context: {context}

        Original text: "{text}"

        Please provide only the translation, without any additional explanations.
        """

        try:
            # Send translation request
            response = self.llm.invoke(prompt)
            return response.content.strip()

        except Exception as e:
            return f"Translation error: {e}"
