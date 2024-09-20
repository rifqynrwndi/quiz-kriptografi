import numpy as np

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def multiply_matrix(pair, matrix):
    return np.dot(pair, matrix) % 26

def hill_cipher(text, key, encrypt=True):
    text = text.upper().replace(" ", "") 
    if len(text) % 2 != 0:
        text += 'X'

    key_matrix = np.array([list(map(int, row.split())) for row in key.split('\n')])
    if key_matrix.shape != (2, 2):
        raise ValueError("Kunci Hill harus matriks 2x2")

    result = []
    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - ord('A'), ord(text[i + 1]) - ord('A')]
        if encrypt:
            new_pair = multiply_matrix(pair, key_matrix)
        else:
            determinant = int(np.round(np.linalg.det(key_matrix))) % 26
            determinant_inv = mod_inverse(determinant, 26)
            adjugate_matrix = np.array([[key_matrix[1][1], -key_matrix[0][1]], [-key_matrix[1][0], key_matrix[0][0]]])
            inverse_matrix = (determinant_inv * adjugate_matrix) % 26
            new_pair = multiply_matrix(pair, inverse_matrix)

        result.append(chr(int(new_pair[0]) + ord('A')))
        result.append(chr(int(new_pair[1]) + ord('A')))

    return ''.join(result)
