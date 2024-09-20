import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from ciphers.vigenere import vigenere_cipher
from ciphers.playfair import playfair_cipher
from ciphers.hill import hill_cipher

class CipherToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cipher Tool")
        self.configure(bg="#2C3E50")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=6, relief="flat", background="#3498DB", foreground="white")
        style.configure("TRadiobutton", background="#2C3E50", foreground="white")
        style.configure("TLabel", background="#2C3E50", foreground="white", font=("Helvetica", 12))

        main_frame = ttk.Frame(self, padding="10 10 10 10", style="Main.TFrame")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        input_frame = ttk.Frame(main_frame, padding="5 5 5 5", style="Main.TFrame")
        input_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(input_frame, text="Input Text:").grid(column=0, row=0, sticky=tk.W)
        self.text_input = ScrolledText(input_frame, wrap=tk.WORD, width=60, height=10)
        self.text_input.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(input_frame, text="Key:").grid(column=0, row=2, sticky=tk.W)
        self.key_input = ScrolledText(input_frame, wrap=tk.WORD, width=60, height=5)
        self.key_input.grid(column=0, row=3, sticky=(tk.W, tk.E))

        options_frame = ttk.Frame(main_frame, padding="5 5 5 5", style="Main.TFrame")
        options_frame.grid(column=1, row=0, sticky=(tk.N, tk.S))

        ttk.Label(options_frame, text="Cipher Type:").grid(column=0, row=0, sticky=tk.W)
        self.cipher_var = tk.StringVar(value='Vigenere')
        ttk.Radiobutton(options_frame, text="Vigenere", variable=self.cipher_var, value='Vigenere').grid(column=0, row=1, sticky=tk.W)
        ttk.Radiobutton(options_frame, text="Playfair", variable=self.cipher_var, value='Playfair').grid(column=0, row=2, sticky=tk.W)
        ttk.Radiobutton(options_frame, text="Hill", variable=self.cipher_var, value='Hill').grid(column=0, row=3, sticky=tk.W)

        ttk.Label(options_frame, text="Operation:").grid(column=0, row=4, sticky=tk.W, pady=(10, 0))
        self.operation_var = tk.StringVar(value='Encrypt')
        ttk.Radiobutton(options_frame, text="Encrypt", variable=self.operation_var, value='Encrypt').grid(column=0, row=5, sticky=tk.W)
        ttk.Radiobutton(options_frame, text="Decrypt", variable=self.operation_var, value='Decrypt').grid(column=0, row=6, sticky=tk.W)

        button_frame = ttk.Frame(main_frame, padding="5 5 5 5", style="Main.TFrame")
        button_frame.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.E))

        ttk.Button(button_frame, text="Upload File", command=self.upload_file).grid(column=0, row=0, padx=5)
        ttk.Button(button_frame, text="Process", command=self.encrypt_decrypt).grid(column=1, row=0, padx=5)

        output_frame = ttk.Frame(main_frame, padding="5 5 5 5", style="Main.TFrame")
        output_frame.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(output_frame, text="Result:").grid(column=0, row=0, sticky=tk.W)
        self.result_display = ScrolledText(output_frame, wrap=tk.WORD, width=80, height=10, state="disabled")
        self.result_display.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_input.insert(tk.END, file.read())

    def encrypt_decrypt(self):
        text = self.text_input.get("1.0", tk.END).strip()
        key = self.key_input.get("1.0", tk.END).strip()
        operation = self.operation_var.get() == 'Encrypt'

        if not text or not key:
            messagebox.showwarning("Input Error", "Text dan Key tidak boleh kosong.")
            return

        cipher_type = self.cipher_var.get()

        try:
            if cipher_type == 'Vigenere':
                result = vigenere_cipher(text, key, encrypt=operation)
            elif cipher_type == 'Playfair':
                result = playfair_cipher(text, key, encrypt=operation)
            elif cipher_type == 'Hill':
                result = hill_cipher(text, key, encrypt=operation)
            else:
                result = "Invalid cipher type selected."
        except Exception as e:
            result = f"Error: {str(e)}"

        self.result_display.config(state="normal")
        self.result_display.delete("1.0", tk.END)
        self.result_display.insert(tk.END, result)
        self.result_display.config(state="disabled")
