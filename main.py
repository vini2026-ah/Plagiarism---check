import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_plagiarism():
    text1 = text_box1.get("1.0", tk.END).strip()
    text2 = text_box2.get("1.0", tk.END).strip()
    
    if not text1 or not text2:
        messagebox.showwarning("Warning", "Please enter both texts first!")
        return
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    percentage = round(similarity * 100, 2)
    result_label.config(text=f"Similarity Score: {percentage}%", fg="red" if percentage > 50 else "green")

root = tk.Tk()
root.title("Plagiarism Checker - Text Similarity")
root.geometry("500x450")

tk.Label(root, text="Original Text (النص الأصلي):", font=("Arial", 10, "bold")).pack(pady=5)
text_box1 = tk.Text(root, height=7, width=55)
text_box1.pack()

tk.Label(root, text="Submitted Text (النص المراد فحصه):", font=("Arial", 10, "bold")).pack(pady=5)
text_box2 = tk.Text(root, height=7, width=55)
text_box2.pack()

tk.Button(root, text="Check Similarity", command=check_plagiarism, bg="#0052cc", fg="white", font=("Arial", 11, "bold")).pack(pady=15)
result_label = tk.Label(root, text="Similarity Score: 0.0%", font=("Arial", 14, "bold"))
result_label.pack()

root.mainloop()o
