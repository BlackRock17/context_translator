import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from prompts import get_translation_prompt

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

        # Generate context-specific prompt
        prompt = get_translation_prompt(
            text=text,
            source_lang=source_lang,
            target_lang=target_lang,
            context=context
        )

        try:
            # Send translation request
            response = self.llm.invoke(prompt)
            return response.content.strip()

        except Exception as e:
            return f"Translation error: {e}"
