# chatbot.py
from transformers import pipeline
import random
from collections import deque

# Load Hugging Face emotion model
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

# Crisis keywords
CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life", "self harm", "hurt myself",
    "can't go on", "worthless", "no reason to live"
]

# Response templates
RESPONSES = {
    "joy": [
        "That's wonderful to hear! 🌟",
        "I'm so glad you're feeling this way! Keep enjoying the moment.",
        "Your happiness is contagious — keep smiling!"
    ],
    "sadness": [
        "I'm really sorry you're feeling this way. I'm here to listen. 💙",
        "It's okay to feel sad sometimes. Talking about it can help.",
        "You matter, and your feelings are valid."
    ],
    "anger": [
        "It sounds like something has upset you. Want to talk about it?",
        "I hear your frustration — let's try to work through it together.",
        "It's okay to feel angry; expressing it in words is a good start."
    ],
    "fear": [
        "That sounds scary. Do you want to share more so I can understand?",
        "It's okay to feel afraid; you're not alone in this.",
        "Your feelings are valid — let's take it one step at a time."
    ],
    "love": [
        "Love is such a beautiful emotion. 💖",
        "That's so heartwarming to hear!",
        "Cherish this feeling and the people who make you feel this way."
    ],
    "surprise": [
        "Oh, that's unexpected! How do you feel about it?",
        "Wow! That must have caught you off guard.",
        "Surprises can be exciting — or overwhelming. Which is it for you?"
    ],
    "neutral": [
        "I hear you. Would you like to share more?",
        "Thanks for sharing. How are you feeling about it?",
        "I’m listening — tell me more."
    ]
}

# Conversation memory (stores last 5 user messages)
conversation_memory = deque(maxlen=5)

def detect_crisis(user_input):
    """Check if message contains crisis keywords."""
    return any(keyword in user_input.lower() for keyword in CRISIS_KEYWORDS)

def get_bot_response(user_input):
    """Generate a context-aware response."""
    # Save user message to memory
    conversation_memory.append(user_input)

    # Crisis check
    if detect_crisis(user_input):
        return (
            "It sounds like you might be going through a crisis. "
            "You are not alone — please reach out to a suicide prevention helpline immediately.\n"
            "India: AASRA 91-9820466726\n"
            "USA: 988 Suicide and Crisis Lifeline"
        ), "CRISIS"

    # Create a context string
    context = " ".join(conversation_memory)

    # Emotion detection on combined context
    emotion_result = emotion_model(context)[0][0]
    emotion = emotion_result['label'].lower()

    # Choose varied reply
    response = random.choice(RESPONSES.get(emotion, RESPONSES["neutral"]))
    return response, emotion.upper()
