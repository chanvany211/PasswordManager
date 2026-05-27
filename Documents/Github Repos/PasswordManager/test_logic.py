from logic import generate_password

def test_password_length():
    pwd = generate_password(12)
    assert len(pwd) == 12