from django.shortcuts import render
import base64
import urllib.parse
import codecs

from django.conf import settings
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad

def home_view(request):
    mode = request.GET.get('mode', 'encode')
    input_text = ''
    output_text = ''
    selected_operation = ''
    error = None

    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        operation = request.POST.get('operation', '')
        mode = request.POST.get('mode', 'encode')
        selected_operation = operation

        try:
            if operation == 'b64_encode':
                output_text = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')
            elif operation == 'b64_decode':
                output_text = base64.b64decode(input_text.encode('utf-8')).decode('utf-8')



            elif operation == 'rot13':
                output_text = codecs.encode(input_text, 'rot_13')

            elif operation == 'aes_encode':
                key = settings.AES_SECRET_KEY
                data_bytes = input_text.encode('utf-8')
                cipher = AES.new(key, AES.MODE_CBC)
                ciphertext_bytes = cipher.encrypt(pad(data_bytes, AES.block_size))
                iv = cipher.iv
                output_text = base64.b64encode(iv + ciphertext_bytes).decode('utf-8')

            elif operation == 'aes_decode':
                key = settings.AES_SECRET_KEY
                encrypted_data_with_iv = base64.b64decode(input_text)
                iv = encrypted_data_with_iv[:AES.block_size]
                ciphertext_bytes = encrypted_data_with_iv[AES.block_size:]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                decrypted_bytes = unpad(cipher.decrypt(ciphertext_bytes), AES.block_size)
                output_text = decrypted_bytes.decode('utf-8')

            elif operation == 'rsa_encode':
                public_key_str = settings.RSA_PUBLIC_KEY
                recipient_key = RSA.import_key(public_key_str)
                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                encrypted_data = cipher_rsa.encrypt(input_text.encode("utf-8"))
                output_text = base64.b64encode(encrypted_data).decode("utf-8")

            elif operation == 'rsa_decode':
                private_key_str = settings.RSA_PRIVATE_KEY
                private_key = RSA.import_key(private_key_str)
                cipher_rsa = PKCS1_OAEP.new(private_key)
                encrypted_data = base64.b64decode(input_text)
                decrypted_data = cipher_rsa.decrypt(encrypted_data)
                output_text = decrypted_data.decode("utf-8")

            elif operation == 'binary_encode':
                output_text = ' '.join(format(ord(char), '08b') for char in input_text)

            elif operation == 'binary_decode':
                binary_values = input_text.split(' ')
                ascii_characters = [chr(int(binary, 2)) for binary in binary_values]
                output_text = "".join(ascii_characters)

        except Exception as e:
            error = f"Error: {e}. Please check your input format."
            output_text = ''

    context = {
        'input_text': input_text,
        'output_text': output_text,
        'selected_operation': selected_operation,
        'error': error,
        'mode': mode,
    }
    return render(request, 'encoder_decoder/index.html', context)