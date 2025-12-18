# Password Audit

A small Python CLI tool that evaluates password strength using a simple ruleset, generates cryptographically secure passwords, and (optionally) encrypts and stores generated passwords in a Supabase table.

This project is intended for learning and experimentation with password hygiene, secure random generation, and basic cloud persistence.

## Features

- Password strength scoring (0–4)
  - Minimum length threshold
  - Uppercase letter presence
  - Digit presence
  - Special character presence
- Secure password generation using Python's `secrets` module
- Optional encryption-at-rest for generated passwords using `cryptography` (Fernet)
- Optional storage of encrypted passwords to Supabase

## How It Works

- **Strength analysis**: `analyse_strength()` increments a score based on four checks (length, uppercase, digit, special character).
- **Password generation**: `generate_secure_password()` uses `secrets.choice()` over an alphabet of letters, digits, and punctuation, and loops until the generated password satisfies all character-category checks.
- **Encryption + storage (optional)**: `encrypt_and_store()` encrypts the generated password with Fernet and inserts the encrypted string into a Supabase table.

## Requirements

- Python 3.9+
- Dependencies:
  - `cryptography`
  - `supabase` (the Supabase Python client)

Install dependencies:

```bash
pip install cryptography supabase
```

## Configuration (Supabase)

Supabase integration is configured in `password_audit.py`:

- `SUPABASE_URL`
- `SUPABASE_KEY`

Populate these values with your project URL and service role (or other appropriate) API key.

### Expected Table Schema

The script inserts into a table named `passwords`.

A minimal schema that matches the current insert shape:

- `id` (UUID or integer primary key; auto-generated)
- `content` (text; stores the encrypted password)
- `note` (text; metadata note)

## Running

Run the CLI tool:

```bash
python password_audit.py
```

You can:

- Enter any password to evaluate strength.
- If the password is weak, opt to generate a secure alternative.
- Optionally store the generated password to Supabase (encrypted).

## Security Notes

- This project currently **encrypts generated passwords** for storage. Encryption and hashing solve different problems:
  - **Encryption** is reversible (you can decrypt if you have the key). This is suitable for “password vault” style storage.
  - **Hashing** is one-way. This is how authentication systems store passwords.

- Fernet keys must be managed carefully:
  - The script currently generates an encryption key at runtime (`Fernet.generate_key()`). If you do not persist this key securely, previously stored encrypted values cannot be decrypted.
  - In real systems, keys should be stored in a secrets manager or a protected environment variable and rotated intentionally.

- Do not treat this repository as production-ready password storage. It is a learning project.

## Known Issues

- The current file contains a Python f-string with nested quotes that will raise a syntax error when executed. If you hit a startup error, check the success log line inside `encrypt_and_store()`.

## Roadmap

Planned enhancements:

- Store passwords using a modern hashing scheme (e.g., PBKDF2 / bcrypt / scrypt / Argon2) when modeling login-style storage
- Add a simple GUI (e.g., Tkinter) for strength checking, generation, and storage
- Move configuration to environment variables instead of hard-coded constants
- Adding a Password Retrieval feature

## License

No license has been specified yet. If you plan to publish or accept contributions, consider adding a license file (e.g., MIT, Apache-2.0).

