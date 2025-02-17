import tkinter as tk
from tkinter import messagebox, Canvas
from PIL import Image, ImageTk
from pythainlp.tokenize import syllable_tokenize


class ThaiSyllableMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Syllable Matcher")
        self.root.geometry("650x680")
        self.root.configure(bg="#F5F5F5")

        self.words = []

        self.create_header()
        self.create_input_word_frame()
        self.create_input_section()
        self.create_listbox_section()
        self.create_reset_button()

    def get_syllables(self, word):
        return set(syllable_tokenize(word))

    def add_word(self, event=None):
        new_word = self.entry.get().strip()
        if new_word:
            self.words.append(new_word)
            self.entry.delete(0, tk.END)
            self.update_input_word_list()
            self.update_word_list(new_word)
        else:
            messagebox.showwarning("Input Error", "Please enter a word.")

    def remove_word(self, word):
        if word in self.words:
            self.words.remove(word)
            self.update_input_word_list()
            self.update_word_list('')

    def update_word_list(self, new_word):
        new_syllables = self.get_syllables(new_word)
        matching_words = [word for word in self.words if new_syllables & self.get_syllables(word)]

        self.listbox.delete(0, tk.END)
        for word in matching_words:
            self.listbox.insert(tk.END, word)

        # Update listbox background color based on the number of matching words
        if len(matching_words) > 1:
            self.listbox.config(bg="#FFCCCC")  # Red box for more than 2 words
        else:
            self.listbox.config(bg="#CCFFCC")  # Green box for 2 or fewer words

    def update_input_word_list(self):
        for widget in self.input_word_frame.winfo_children():
            widget.destroy()
        for word in self.words:
            word_frame = tk.Frame(self.input_word_frame, bg="#FFFFFF")
            word_label = tk.Label(word_frame, text=word, bg="#FFFFFF", fg="#333333", font=("Calibri", 12))
            remove_button = tk.Label(word_frame, text=" x", bg="#FFFFFF", fg="#FF0000", font=("Calibri", 12, "bold"))
            remove_button.bind("<Button-1>", lambda e, w=word: self.remove_word(w))

            word_label.pack(side=tk.LEFT, padx=(10, 0))
            remove_button.pack(side=tk.RIGHT, padx=(0, 10))
            word_frame.pack(fill=tk.X, pady=2)

    def reset_word_list(self):
        self.words = []
        self.update_input_word_list()
        self.update_word_list('')

    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, r=50, **kwargs):
        points = [
            x1 + r, y1,
            x1 + r, y1,
            x2 - r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1 + r,
            x1, y1,
        ]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def create_header(self):
        self.header_canvas = Canvas(self.root, width=650, height=150, bg="#F5F5F5", highlightthickness=0)
        self.header_canvas.place(x=0, y=0)
        self.create_rounded_rectangle(self.header_canvas, 10, 10, 640, 140, r=40, outline="#E0E0E0", width=2, fill="#FFFFFF")

        logo_image = Image.open("Screenshot_2024-08-03_222053-removebg-preview.png")
        logo_width, logo_height = logo_image.size
        aspect_ratio = logo_width / logo_height
        new_height = 120
        new_width = int(new_height * aspect_ratio)
        if new_width > 640:
            new_width = 640
            new_height = int(new_width / aspect_ratio)
        logo_image = logo_image.resize((new_width, new_height), Image.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(self.header_canvas, image=self.logo_image, bg="#FFFFFF")
        self.header_canvas.create_window(325, 75, window=logo_label)

    def create_input_word_frame(self):
        self.input_word_canvas = Canvas(self.root, width=260, height=500, bg="#F5F5F5", highlightthickness=0)
        self.input_word_canvas.place(x=10, y=160)
        self.create_rounded_rectangle(self.input_word_canvas, 10, 10, 250, 490, r=40, outline="#E0E0E0", width=2, fill="#FFFFFF")

        input_word_label = tk.Label(self.root, text="Input Words:", bg="#FFFFFF", fg="#333333", font=("Calibri", 12))
        self.input_word_canvas.create_window(130, 40, window=input_word_label)

        self.input_word_frame = tk.Frame(self.input_word_canvas, bg="#F9F9F9")
        self.input_word_canvas.create_window(130, 260, window=self.input_word_frame, height=400, width=200)

    def create_input_section(self):
        self.input_canvas = Canvas(self.root, width=350, height=150, bg="#F5F5F5", highlightthickness=0)
        self.input_canvas.place(x=280, y=160)
        self.create_rounded_rectangle(self.input_canvas, 10, 10, 340, 140, r=40, outline="#E0E0E0", width=2, fill="#FFFFFF")

        entry_label = tk.Label(self.root, text="Enter a word:", bg="#FFFFFF", fg="#333333", font=("Calibri", 12))
        self.input_canvas.create_window(175, 40, window=entry_label)

        self.entry_frame = Canvas(self.root, width=270, height=30, bg="#E0E0E0", bd=0, highlightthickness=0, relief='ridge')
        self.input_canvas.create_window(175, 70, window=self.entry_frame)
        self.entry_frame.create_rounded_rectangle = self.create_rounded_rectangle(self.entry_frame, 0, 0, 270, 30, r=15,
                                                                                  outline="#E0E0E0", width=0, fill="#F5F5F5")

        self.entry = tk.Entry(self.entry_frame, width=30, font=("Calibri", 12), bd=0, highlightthickness=0, bg="#F5F5F5", justify='center')
        self.entry.place(x=5, y=5, width=260, height=20)
        self.entry.bind("<Return>", self.add_word)

        add_button = tk.Button(self.root, text="Add Word", command=self.add_word, font=("Calibri", 12), bg="#007BFF",
                               fg="#FFFFFF", bd=0, highlightthickness=0)
        self.input_canvas.create_window(175, 110, window=add_button)

    def create_listbox_section(self):
        self.listbox_canvas = Canvas(self.root, width=350, height=300, bg="#F5F5F5", highlightthickness=0)
        self.listbox_canvas.place(x=280, y=320)
        self.create_rounded_rectangle(self.listbox_canvas, 10, 10, 340, 290, r=40, outline="#E0E0E0", width=2, fill="#FFFFFF")

        listbox_label = tk.Label(self.root, text="Words containing the same syllables:", bg="#FFFFFF", fg="#333333",
                                 font=("Calibri", 12))
        self.listbox_canvas.create_window(175, 40, window=listbox_label)

        self.listbox = tk.Listbox(self.root, font=("Calibri", 12), bg="#F9F9F9", bd=0, highlightthickness=0, selectbackground="#CCCCFF")
        self.listbox_canvas.create_window(175, 160, window=self.listbox, height=200, width=280)

    def create_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_word_list, font=("Calibri", 12), bg="#007BFF",
                                 fg="#FFFFFF", bd=0, highlightthickness=0)
        reset_button.place(x=300, y=620)


if __name__ == "__main__":
    root = tk.Tk()
    app = ThaiSyllableMatcherApp(root)
    root.mainloop()
