from flask import Flask, request

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    membership = request.form.get('membership')
    payment = request.form.get('payment')
    orientation = request.form.get('orientation')

    # You can now use the form data. For example, you might store it in a database.
    # For now, let's just print it to the console.
    print(f'Name: {name}')
    print(f'Email: {email}')
    print(f'Phone: {phone}')
    print(f'Membership: {membership}')
    print(f'Payment: {payment}')
    print(f'Orientation: {orientation}')

    return 'Form submitted successfully.'

if __name__ == '__main__':
    app.run(debug=True)
