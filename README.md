# Text Encoder / Decoder

This is a simple web application built with the Django framework to encode and decode text using various popular encoding and encryption standards. It provides a clean and user-friendly interface for text transformations.

## 🚀 Features

The application supports the following encoding and encryption methods:

*   **Encode:**
    *   Base64
    *   ROT13
    *   AES (Encryption)
    *   RSA (Encryption)
    *   Text to Binary
*   **Decode:**
    *   Base64
    *   ROT13
    *   AES Decryption
    *   RSA Decryption
    *   Binary to Text

## 📸 Screenshots
<img width="906" height="220" alt="Ekran görüntüsü 2025-08-19 120229" src="https://github.com/user-attachments/assets/640b220a-7cf9-4bab-811a-a032ff0672ea" />
<img width="895" height="217" alt="Ekran görüntüsü 2025-08-19 120216" src="https://github.com/user-attachments/assets/272f50c9-4ef6-4784-a524-8a524966d55b" />

Here is a quick demonstration of how the application works:

### Encoding Process
When "Merhaba Dünya" is entered into the textbox and `Base64` is selected as the encoding method:

<img width="1899" height="863" alt="Ekran görüntüsü 2025-08-19 115318" src="https://github.com/user-attachments/assets/603810d0-0596-4e52-83ab-4a064f87b015" />

### Decoding Process
Pasting the encoded result into the Decode tab successfully retrieves the original text:

<img width="1892" height="861" alt="Ekran görüntüsü 2025-08-19 115340" src="https://github.com/user-attachments/assets/7c4640d8-f327-40cb-8fce-0ae1f0a2c884" />

## 🛠️ Technologies Used

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS (for the basic interface)
*   **Database:** SQLite (Default for development)
*   **Cryptography Library:** PyCryptodome (for AES and RSA operations)

## 🔧 Local Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mustafadgny/TextEncoder.git
    cd TextEncoder
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    *(Note: If you don't have a `requirements.txt` file, you should create one with `pip freeze > requirements.txt` and push it to GitHub.)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

You can now access the application by navigating to `http://127.0.0.1:8000/` in your web browser.

---

This project was developed as a practical example for learning the fundamentals of cryptography and web development.
