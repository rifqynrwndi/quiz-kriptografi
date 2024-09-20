def create_matrix(key):
    key = key.upper().replace('J', 'I')
    key = ''.join(dict.fromkeys(key))
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = list(key)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    result = []
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i+1]:
            result.extend([text[i], 'X'])
            i += 1
        else:
            result.extend([text[i], text[i+1]])
            i += 2
    return ''.join(result)

def playfair_cipher(text, key, encrypt=True):
    matrix = create_matrix(key)
    text = prepare_text(text)
    result = []
    
    for i in range(0, len(text), 2):
        row1, col1 = find_position(text[i], matrix)
        row2, col2 = find_position(text[i+1], matrix)
        
        if row1 == row2:
            if encrypt:
                result.append(matrix[row1][(col1 + 1) % 5])
                result.append(matrix[row2][(col2 + 1) % 5])
            else:
                result.append(matrix[row1][(col1 - 1) % 5])
                result.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            if encrypt:
                result.append(matrix[(row1 + 1) % 5][col1])
                result.append(matrix[(row2 + 1) % 5][col2])
            else:
                result.append(matrix[(row1 - 1) % 5][col1])
                result.append(matrix[(row2 - 1) % 5][col2])
        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])
    
    return ''.join(result)
