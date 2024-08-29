from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

def generate_password(length):
    if length < 4:
        raise ValueError('Password length should be at least 4 characters.')
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine character sets
    characters = lower + upper + digits + special

    # Ensure that the password contains at least one of each character type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all character sets
    password += [random.choice(characters) for _ in range(length - 4)]
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = int(data.get('length', 12))
    
    try:
        password = generate_password(length)
        return jsonify({'password': password})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
