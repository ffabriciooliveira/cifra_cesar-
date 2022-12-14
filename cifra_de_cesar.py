# -*- coding: utf-8 -*-
"""Cifra de Cesar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zP8yd41u4n01Y5JAeNsvJi5ekONNuGeE
"""

MODE_ENCRYPT = 1 

MODE_DECRYPT = 0 

 

def cesar(data, key, mode): 

    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ' 

    new_data = '' 

    for c in data: 

        index = alphabet.find(c) 

        if index == -1: 

            new_data += c 

        else: 

            new_index = index + key if mode == MODE_ENCRYPT else index - key 

            new_index = new_index % len(alphabet) 

            new_data += alphabet[new_index:new_index+1] 

    return new_data 

 
 

# Tests 

key = 5 

original = 'Teste CRiptografia Cifra de Cesar' 

print('  Original:', original) 

ciphered = cesar(original, key, MODE_ENCRYPT) 

print('Encriptada:', ciphered) 

plain = cesar(ciphered, key, MODE_DECRYPT) 

print('Decriptada:', plain)

