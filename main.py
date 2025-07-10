import os
from dotenv import load_dotenv
from translator import ContextTranslator

# Load environment variables from .env file
load_dotenv()


def test_basic_translation():
    """Test basic translation functionality"""

    # Create translator instance
    translator = ContextTranslator()

    # Test cases
    test_cases = [
        {
            "text": "Hello, how are you?",
            "context": "personal",
            "description": "Personal greeting"
        },
        {
            "text": "Please submit your quarterly report by Friday.",
            "context": "business",
            "description": "Business communication"
        },
        {
            "text": "The database connection failed.",
            "context": "technical",
            "description": "Technical error message"
        }
    ]

    print("🔄 Testing basic translation...")
    print("=" * 50)

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
        print("-" * 30)


if __name__ == "__main__":
    test_basic_translation()
