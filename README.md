# Context-Aware Translator

A simple AI-powered translation tool that adapts translations based on context using LangChain and Azure OpenAI.

## Features

- **Context-aware translation**: Adapts tone and terminology based on context
- **Bidirectional translation**: Supports both English ↔ Bulgarian translation
- **Multiple contexts**: Personal, Business, Technical, and General
- **Interactive mode**: Real-time translation with user input
- **Test mode**: Predefined test cases for validation

## Supported Contexts

- **Personal**: Informal, casual tone with friendly expressions
- **Business**: Formal, professional language with business terminology
- **Technical**: Precise technical terms and clear, unambiguous language
- **General**: Neutral, standard language suitable for general audience

## Project Structure

```
context_translator/
├── main.py              # Main application entry point
├── translator.py        # Translation logic and ContextTranslator class
├── prompts.py          # Context-specific prompts and instructions
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API keys)
└── README.md          # This file
```

## Prerequisites

- Python 3.7+
- Azure OpenAI account with deployed GPT-4 model
- PyCharm Professional (recommended)

## Installation

1. Clone or download the project
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install langchain langchain-openai python-dotenv
   pip freeze > requirements.txt
   ```

4. Create a `.env` file with your Azure OpenAI credentials:
   ```
   AZURE_OPENAI_API_KEY=your_api_key_here
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_DEPLOYMENT=your-deployment-name
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   ```

## Usage

Run the application:
```bash
python main.py
```

Choose between:
1. **Test mode**: Run predefined test cases to see how different contexts affect translations
2. **Interactive mode**: Enter your own text and choose context for real-time translation

### Interactive Mode Example
```
📝 Enter text to translate: Hello, how are you?
🔄 Translation direction (EN→BG or BG→EN): EN→BG
🎯 Enter context (personal/business/technical/general): personal
🔄 Translating from English to Bulgarian...
✅ Translation (personal, English→Bulgarian): Здравей, как си?
```

## Key Components

### ContextTranslator Class
- Handles Azure OpenAI connection
- Manages translation logic
- Supports multiple languages and contexts

### Context-Specific Prompts
- Specialized instructions for each context
- Modular prompt system for easy customization
- Consistent translation quality

### Interactive Interface
- User-friendly command-line interface
- Input validation and error handling
- Support for both translation directions

## Example Translations

| Context | English | Bulgarian |
|---------|---------|-----------|
| Personal | "Hey! What's up?" | "Хей! Как си?" |
| Business | "Please submit your report" | "Моля, изпратете вашия отчет" |
| Technical | "The API returned an error" | "API върна грешка" |
| General | "Thank you for your help" | "Благодаря ви за помощта" |

## Learning Objectives

This project demonstrates:
- **LangChain basics**: Working with Azure OpenAI integration
- **Prompt engineering**: Creating context-specific prompts
- **Modular design**: Separating concerns across multiple files
- **Error handling**: Managing API errors and user input validation
- **Interactive CLI**: Building user-friendly command-line interfaces

## Future Enhancements

- Translation history tracking
- Support for additional languages
- Batch translation processing
- Web interface
- Custom context definitions

## Dependencies

- `langchain` - LLM framework
- `langchain-openai` - Azure OpenAI integration
- `python-dotenv` - Environment variable management

## License

This project is for educational purposes.
