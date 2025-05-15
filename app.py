import random
import nltk
from nltk.corpus import movie_reviews
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import gradio as gr

# Download dataset
nltk.download('movie_reviews')

# Load and shuffle data
documents = [(movie_reviews.raw(fileid), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
texts = [doc for doc, _ in documents]
labels = [1 if label == 'pos' else 0 for _, label in documents]

# Build pipeline (no 'probability' param needed)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.7)),
    ('clf', LogisticRegression(max_iter=1000))
])
pipeline.fit(texts, labels)

# Classifier with 3 sentiment levels
def classify_review(review, history):
    proba = pipeline.predict_proba([review])[0]
    label = pipeline.predict([review])[0]
    confidence = max(proba)

    if 0.4 <= confidence <= 0.6:
        return "⚪ Neutral 😐"
    elif label == 1:
        return "🟢 Positive ✅"
    else:
        return "🔴 Negative ❌"

# Emoji insertion function
def insert_emoji(text, emoji):
    return text + emoji

# Gradio Blocks Interface
with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple")) as app:
    gr.Markdown("# 🎬 Movie Review Sentiment Analyzer (3-Class) + Emojis")
    gr.Markdown("Type a review or use emojis below to express tone:")

    chatbot = gr.ChatInterface(
        fn=classify_review,
        examples=[
            "I loved the visuals and the performances were brilliant!",
            "It was fine. I neither liked nor disliked it.",
            "This was one of the worst films I've ever seen."
        ],
        additional_inputs_accordion=None
    )

    gr.Markdown("### 😄 Positive Emojis")
    with gr.Row():
        for emoji in ["😍", "😊", "😂", "👍", "🎉", "🔥", "👏", "💯"]:
            gr.Button(emoji).click(
                fn=insert_emoji,
                inputs=[chatbot.textbox, gr.Textbox(value=emoji, visible=False)],
                outputs=chatbot.textbox
            )

    gr.Markdown("### 😐 Neutral Emojis")
    with gr.Row():
        for emoji in ["😐", "🤔", "😶", "😑", "🙃"]:
            gr.Button(emoji).click(
                fn=insert_emoji,
                inputs=[chatbot.textbox, gr.Textbox(value=emoji, visible=False)],
                outputs=chatbot.textbox
            )

    gr.Markdown("### 😠 Negative Emojis")
    with gr.Row():
        for emoji in ["😠", "👎", "💩", "😭", "😤", "😡", "😫"]:
            gr.Button(emoji).click(
                fn=insert_emoji,
                inputs=[chatbot.textbox, gr.Textbox(value=emoji, visible=False)],
                outputs=chatbot.textbox
            )

# Launch app
app.launch()
