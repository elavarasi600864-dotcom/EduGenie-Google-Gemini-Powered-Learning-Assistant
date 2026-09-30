def generate_quiz(text, question_count=3):
    return {
        "questions": [
            {
                "question": f"What is the main idea of the following text?",
                "options": [
                    text[:100],
                    "An unrelated idea",
                    "Another unrelated idea",
                    "None of the above"
                ],
                "correct_answer": text[:100],
                "explanation": "The first option represents the main content provided."
            }
        ]
    }