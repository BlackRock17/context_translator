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


def interactive_mode():
    """Interactive translation mode"""

    translator = ContextTranslator()

    print("🌐 Interactive Context Translator")
    print("=" * 40)
    print("Available contexts: personal, business, technical, general")
    print("Type 'quit' to exit")
    print()

    while True:
        # Get user input
        text = input("📝 Enter text to translate: ").strip()

        if text.lower() == 'quit':
            print("👋 Goodbye!")
            break

        if not text:
            print("❌ Please enter some text to translate.")
            continue

        # Get context
        context = input("🎯 Enter context (personal/business/technical/general): ").strip().lower()

        # Validate context
        valid_contexts = ['personal', 'business', 'technical', 'general']
        if context not in valid_contexts:
            print(f"❌ Invalid context. Using 'general' instead.")
            context = 'general'

        # Translate
        print("🔄 Translating...")
        translation = translator.translate(
            text=text,
            source_lang="English",
            target_lang="Bulgarian",
            context=context
        )

        print(f"✅ Translation ({context}): {translation}")
        print("-" * 40)


if __name__ == "__main__":
    # Ask user what they want to do
    print("Choose mode:")
    print("1. Run test cases")
    print("2. Interactive mode")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        test_basic_translation()
    elif choice == "2":
        interactive_mode()
    else:
        print("Invalid choice. Running test cases...")
        test_basic_translation()
