# PasswordManager
 1. Stores passwords securely
You save entries like:
- website
- username
- password
These get encrypted before being written to disk.
So even if someone opens the file, they can’t read anything.

 2. Uses real encryption (Fernet)
Your crypto.py handles:
- generating an encryption key
- encrypting data
- decrypting data
This is proper cryptography, not fake obfuscation.

 3. Saves everything in an encrypted vault
Your storage.py:
- reads the encrypted vault
- decrypts it
- returns a Python dictionary
- writes back encrypted data
This is the core of the password manager.

 4. Logic functions handle the operations
Your logic.py:
- generates random passwords
- saves entries
- searches entries
This is the “brain” of the app.

 5. UI lets you interact with it
Your ui.py (Tkinter):
- input fields
- buttons
- display results
- generate password button
- save entry button
- search entry button
This is the front‑end.

 6. main.py launches the whole app
This is the entry point.
You run:
python main.py


And the password manager opens.
