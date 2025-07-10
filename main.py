import os
from dotenv import load_dotenv
from translator import ContextTranslator

# Load environment variables from .env file
load_dotenv()


def test_basic_translation():
    """Test basic translation functionality"""

    # Create translator instance
    translator = ContextTranslator()

    # Test cases - now with more varied examples
    test_cases = [
        {
            "text": "Hey! What's up? Want to grab coffee later?",
            "context": "personal",
            "description": "Personal casual conversation"
        },
        {
            "text": "We need to schedule a meeting to discuss the quarterly budget allocation.",
            "context": "business",
            "description": "Business meeting request"
        },
        {
            "text": "The API endpoint returned a 404 error. Please check the URL configuration.",
            "context": "technical",
            "description": "Technical error report"
        },
        {
            "text": "Thank you for your assistance with this matter.",
            "context": "general",
            "description": "General polite expression"
        }
    ]

    print("🔄 Testing improved context-aware translation...")
    print("=" * 60)

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['description']}")
        print(f"Original: {test_case['text']}")
        print(f"Context: {test_case['context']}")

        # Translate
        translation = translator.translate(
            text=test_case['text'],
            source_lang="English",
            target_lang="Bulgarian",
            context=test_case['context']
        )

        print(f"Translation: {translation}")
        print("-" * 40)


if __name__ == "__main__":
    test_basic_translation()
