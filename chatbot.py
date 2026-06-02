import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faqs = {
    "What is your return policy?": "You can return any item within 30 days of purchase for a full refund.",
    "How do I track my order?": "You can track your order using the tracking link sent to your email.",
    "What payment methods do you accept?": "We accept credit cards, debit cards, PayPal, and UPI.",
    "How do I contact customer support?": "You can reach us at support@example.com or call 1800-123-456.",
    "Do you offer free shipping?": "Yes, we offer free shipping on orders above $50.",
    "How long does delivery take?": "Standard delivery takes 5-7 business days.",
    "Can I change my order?": "Orders can be modified within 24 hours of placement.",
    "Is my payment information secure?": "Yes, we use SSL encryption to protect your payment data.",
    "Do you ship internationally?": "Yes, we ship to over 50 countries worldwide.",
    "How do I reset my password?": "Click on Forgot Password on the login page to reset it."
}

questions = list(faqs.keys())
answers = list(faqs.values())

def get_response():
    user_input = entry.get().strip()
    if not user_input:
        return
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n", "user")
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(questions + [user_input])
    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best = similarity.argmax()
    if similarity[0][best] < 0.1:
        response = "Sorry, I don't understand. Please try rephrasing."
    else:
        response = answers[best]
    chat_box.insert(tk.END, f"Bot: {response}\n\n", "bot")
    chat_box.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("FAQ Chatbot")
window.geometry("600x500")
window.configure(bg="#1a0a1a")

tk.Label(window, text="🤖 FAQ Chatbot", font=("Arial", 20, "bold"),bg="#1a0a1a", fg="#ff69b4").pack(pady=10)

chat_box = tk.Text(window, height=18, width=65, state=tk.DISABLED,bg="#1a2a1a", fg="#cdd6f4", font=("Arial", 10))
chat_box.tag_config("user", foreground="#ff69b4")
chat_box.tag_config("bot", foreground="#a6e3a1")
chat_box.pack(pady=5)

frame = tk.Frame(window, bg="#1a0a1a")
frame.pack()
entry = tk.Entry(frame, width=45, font=("Arial", 11),bg="#1a2a1a", fg="#ff69b4", insertbackground="white")
entry.pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Send 🚀", command=get_response,bg="#ff69b4", fg="#1a0a1a", font=("Arial", 11, "bold"),relief="flat").pack(side=tk.LEFT)

window.mainloop()