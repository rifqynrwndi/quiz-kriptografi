import tkinter as tk
from tkinter import filedialog, messagebox

def vigenere_cipher(text, key, encrypt=True):
    text = text.upper()
    key = key.upper()
    result = []
    
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if encrypt:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result.append(new_char)
            key_index = (key_index + 1) % key_length
        else:
            result.append(char)

    return ''.join(result)

def playfair_cipher(text, key, encrypt=True):
    # Create a 5x5 matrix for the Playfair cipher
    def create_matrix(key):
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        matrix = []
        for char in key:
            if char in alphabet and char not in matrix:
                matrix.append(char)
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]
    
    def find_position(char, matrix):
        for i, row in enumerate(matrix):
            if char in row:
                return (i, row.index(char))
        return None
    
    # Prepare text
    text = text.upper().replace('J', 'I')
    prepared_text = []
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
            if char1 == char2:
                prepared_text.append(char1 + 'X')  # Add 'X' between duplicates
                i += 1
            else:
                prepared_text.append(char1 + char2)
                i += 2
        else:
            prepared_text.append(char1 + 'X')  # Add 'X' at the end if odd length
            i += 1
    
    matrix = create_matrix(key)
    result = []
    
    for pair in prepared_text:
        row1, col1 = find_position(pair[0], matrix)
        row2, col2 = find_position(pair[1], matrix)
        if row1 == row2:
            result.append(matrix[row1][(col1 + 1) % 5])
            result.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            result.append(matrix[(row1 + 1) % 5][col1])
            result.append(matrix[(row2 + 1) % 5][col2])
        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])
    
    return ''.join(result)

def hill_cipher(text, key, encrypt=True):
    def prepare_text(text):
        text = text.upper().replace(' ', '').replace('J', 'I')
        while len(text) % 2 != 0:
            text += 'X'  # Padding
        return text

    def mod26(n):
        return n % 26

    def matrix_multiply(a, b):
        return [
            [mod26(a[0][0] * b[0] + a[0][1] * b[1]),
             mod26(a[0][0] * b[2] + a[0][1] * b[3])],
            [mod26(a[1][0] * b[0] + a[1][1] * b[1]),
             mod26(a[1][0] * b[2] + a[1][1] * b[3])]
        ]

    def inverse_key(key_matrix):
        det = mod26(key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0])
        if det == 0 or det % 2 == 0:  # Not invertible
            raise ValueError("Key matrix is not invertible.")
        det_inv = pow(det, -1, 26)

        inv_matrix = [
            [key_matrix[1][1] * det_inv % 26, -key_matrix[0][1] * det_inv % 26],
            [-key_matrix[1][0] * det_inv % 26, key_matrix[0][0] * det_inv % 26]
        ]
        return [[mod26(i) for i in row] for row in inv_matrix]

    text = prepare_text(text)
    key_matrix = [list(map(int, row.split())) for row in key.strip().splitlines()]
    
    result = []
    for i in range(0, len(text), 2):
        block = [ord(text[i]) - 65, ord(text[i + 1]) - 65]
        if encrypt:
            result_block = matrix_multiply(key_matrix, [block[0], block[1]])
        else:
            inv_matrix = inverse_key(key_matrix)
            result_block = matrix_multiply(inv_matrix, [block[0], block[1]])
        result.extend(result_block)

    return ''.join(chr(x + 65) for x in result)

def encrypt_decrypt():
    text = text_input.get("1.0", tk.END).strip()
    key = key_input.get()
    
    if len(key) < 12 and cipher_var.get() != 'Hill':
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter.")
        return
    
    if not text:
        messagebox.showerror("Error", "Teks tidak boleh kosong.")
        return

    cipher_type = cipher_var.get()
    if cipher_type == 'Vigenere':
        if operation_var.get() == 'Encrypt':
            result = vigenere_cipher(text, key, encrypt=True)
        else:
            result = vigenere_cipher(text, key, encrypt=False)
    elif cipher_type == 'Playfair':
        if operation_var.get() == 'Encrypt':
            result = playfair_cipher(text, key, encrypt=True)
        else:
            result = playfair_cipher(text, key, encrypt=False)
    elif cipher_type == 'Hill':
        try:
            result = hill_cipher(text, key, encrypt=(operation_var.get() == 'Encrypt'))
        except Exception as e:
            messagebox.showerror("Error", "Hill Cipher hanya menerima kunci dalam bentuk matriks 2x2.\n" + str(e))
            return
    
    result_display.config(state='normal')
    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, result)
    result_display.config(state='disabled')

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, content)

app = tk.Tk()
app.title("Cipher Tool")
app.configure(bg="#004D40")

cipher_var = tk.StringVar(value='Vigenere')
operation_var = tk.StringVar(value='Encrypt')

# Labels
tk.Label(app, text="Teks:", bg="#004D40", fg="white", font=("Helvetica", 12)).pack(pady=5)
text_input = tk.Text(app, height=10, width=40, font=("Helvetica", 10), bg="#E0F2F1", fg="#004D40", wrap="word")
text_input.pack(pady=5)

tk.Label(app, text="Kunci:", bg="#004D40", fg="white", font=("Helvetica", 12)).pack(pady=5)
key_input = tk.Entry(app, width=40, font=("Helvetica", 10), bg="#E0F2F1", fg="#004D40")
key_input.pack(pady=5)

# Cipher Type
tk.Label(app, text="Jenis Cipher:", bg="#004D40", fg="white", font=("Helvetica", 12)).pack(pady=5)
tk.Radiobutton(app, text="Vigenere", variable=cipher_var, value='Vigenere', bg="#004D40", fg="white", selectcolor="#004D40", font=("Helvetica", 10)).pack()
tk.Radiobutton(app, text="Playfair", variable=cipher_var, value='Playfair', bg="#004D40", fg="white", selectcolor="#004D40", font=("Helvetica", 10)).pack()
tk.Radiobutton(app, text="Hill", variable=cipher_var, value='Hill', bg="#004D40", fg="white", selectcolor="#004D40", font=("Helvetica", 10)).pack()

# Operation Type
tk.Label(app, text="Operasi:", bg="#004D40", fg="white", font=("Helvetica", 12)).pack(pady=5)
tk.Radiobutton(app, text="Encrypt", variable=operation_var, value='Encrypt', bg="#004D40", fg="white", selectcolor="#004D40", font=("Helvetica", 10)).pack()
tk.Radiobutton(app, text="Decrypt", variable=operation_var, value='Decrypt', bg="#004D40", fg="white", selectcolor="#004D40", font=("Helvetica", 10)).pack()

# Buttons
tk.Button(app, text="Upload File", command=upload_file, font=("Helvetica", 10), bg="#00796B", fg="white").pack(pady=5)
tk.Button(app, text="Proses", command=encrypt_decrypt, font=("Helvetica", 10), bg="#00796B", fg="white").pack(pady=5)

# Result Display (Text Widget)
tk.Label(app, text="Hasil:", bg="#004D40", fg="white", font=("Helvetica", 12)).pack(pady=5)
result_display = tk.Text(app, height=10, width=40, font=("Helvetica", 10), bg="#E0F2F1", fg="#004D40", wrap="word", state="disabled")
result_display.pack(pady=5)

app.mainloop()