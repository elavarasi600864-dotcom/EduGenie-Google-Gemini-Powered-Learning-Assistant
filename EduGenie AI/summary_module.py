def summarize_text(text):
    if not text or not text.strip():
        return "Please provide some text to summarize."

    # Temporary working implementation.
    # We will connect this to Gemini after the server starts correctly.
    words = text.strip().split()

    if len(words) <= 50:
        return text.strip()

    return " ".join(words[:50]) + "..."