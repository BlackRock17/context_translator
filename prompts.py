"""
Specialized prompts for different translation contexts
"""

# Base prompt template
BASE_PROMPT = """
You are a professional translator specializing in context-aware translations.
Translate the following text from {source_lang} to {target_lang}.

Context: {context}
Original text: "{text}"

{context_instructions}

Provide only the translation without any additional explanations.
"""

# Context-specific instructions
CONTEXT_INSTRUCTIONS = {
    "personal": """
    Instructions for personal context:
    - Use informal tone and casual language
    - Choose familiar, everyday expressions
    - Use "ти" form instead of "вие" when appropriate
    - Make it sound natural for personal conversation
    """,

    "business": """
    Instructions for business context:
    - Use formal, professional language
    - Maintain courteous and respectful tone
    - Use proper business terminology
    - Use "вие" form for respectful address
    - Keep the professional register consistent
    """,

    "technical": """
    Instructions for technical context:
    - Use precise technical terminology
    - Maintain accuracy of technical terms
    - Keep technical concepts clear and unambiguous
    - Use established technical vocabulary
    - Prioritize clarity and precision over style
    """,

    "general": """
    Instructions for general context:
    - Use neutral, standard language
    - Balance between formal and informal tone
    - Choose commonly understood expressions
    - Make it suitable for general audience
    """
}


def get_translation_prompt(text, source_lang, target_lang, context):
    """
    Generate context-specific translation prompt

    Args:
        text (str): Text to translate
        source_lang (str): Source language
        target_lang (str): Target language
        context (str): Translation context

    Returns:
        str: Formatted prompt
    """

    # Get context instructions, default to general if not found
    context_instructions = CONTEXT_INSTRUCTIONS.get(context, CONTEXT_INSTRUCTIONS["general"])

    # Format the prompt
    prompt = BASE_PROMPT.format(
        source_lang=source_lang,
        target_lang=target_lang,
        context=context,
        text=text,
        context_instructions=context_instructions
    )

    return prompt
