---
title: "Flask App Documentation"
author: "Thomas Ware"
date: "2024-12-08"
project: "PARA_PJT V20"
category: "Resources"
status: "Active"
description: "Unified documentation for Flask app resources."
tags: ['Flask', 'Web Development', 'Resources', 'Guides']
version: "1.0"
last_updated: "2024-12-08"

---
# **Flask App Documentation**

---
## **1. Naming Convention Format**

```
YYYY-MM-DD_topic_version.extension
```

---

## **2. Document Organization Using PARA**

|**Original File/Folder**|**Renamed Document/Folder**|**PARA Category**|**Reason for Categorization**|
|---|---|---|---|
|MembersForm.py|2024-12-08_MembersForm.py|Resources|Documentation of Membersform.Py.|
|MakerSpace.css|2024-12-08_MakerSpace.css|Resources|Documentation of Makerspace.Css.|
|MembersForm.html|2024-12-08_MembersForm.html|Resources|Documentation of Membersform.Html.|


---
title: "Membersform.Py"
author: "Thomas Ware"
date: "2024-12-08"
original_name: "MembersForm.py"
renamed_name: "2024-12-08_MembersForm.py"
category: "Resources"
description: "Detailed documentation for Membersform.Py."
tags: ['Flask', 'Web Development', 'Resources', 'Guides']
version: "1.0"
last_updated: "2024-12-08"

---
# **Membersform.Py**

## **Original Content**

```
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('MembersForm.html')

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


```

---

---
title: "Makerspace.Css"
author: "Thomas Ware"
date: "2024-12-08"
original_name: "MakerSpace.css"
renamed_name: "2024-12-08_MakerSpace.css"
category: "Resources"
description: "Detailed documentation for Makerspace.Css."
tags: ['Flask', 'Web Development', 'Resources', 'Guides']
version: "1.0"
last_updated: "2024-12-08"

---
# **Makerspace.Css**

## **Original Content**

```
body {
    font-family: Arial, sans-serif;
    background-color: #f8f8f8;
    padding: 20px;
}

h1, h2 {
    color: #333;
}

form {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
}

label {
    font-weight: bold;
    display: block;
    margin-bottom: 5px;
}

input[type="text"], input[type="email"], input[type="tel"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

input[type="radio"] {
    margin: 10px 5px;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 15px 20px;
    margin: 10px 0;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #45a049;
}


```

---

---
title: "Membersform.Html"
author: "Thomas Ware"
date: "2024-12-08"
original_name: "MembersForm.html"
renamed_name: "2024-12-08_MembersForm.html"
category: "Resources"
description: "Detailed documentation for Membersform.Html."
tags: ['Flask', 'Web Development', 'Resources', 'Guides']
version: "1.0"
last_updated: "2024-12-08"

---
# **Membersform.Html**

## **Original Content**

```
<!DOCTYPE html>
<html>
<head>
    <title>Membership Application Form</title>
    <link rel="stylesheet" type="text/css" href="MakerSpace.css">
</head>
<body>
    <h1>Membership Application Form</h1>

    <form action="/submit_form" method="POST">
        <label for="name">Full Name:</label><br>
        <input type="text" id="name" name="name"><br>

        <label for="email">Email Address:</label><br>
        <input type="email" id="email" name="email"><br>

        <label for="phone">Phone Number:</label><br>
        <input type="tel" id="phone" name="phone"><br>

        <h2>Membership Option</h2>
        <input type="radio" id="dayPass" name="membership" value="dayPass">
        <label for="dayPass">Day Pass</label><br>

        <input type="radio" id="monthly" name="membership" value="monthly">
        <label for="monthly">Monthly Membership</label><br>

        <input type="radio" id="yearly" name="membership" value="yearly">
        <label for="yearly">Yearly Membership</label><br>

        <h2>Payment Method</h2>
        <input type="radio" id="creditCard" name="payment" value="creditCard">
        <label for="creditCard">Credit Card</label><br>

        <input type="radio" id="bankTransfer" name="payment" value="bankTransfer">
        <label for="bankTransfer">Bank Transfer</label><br>

        <input type="radio" id="inPerson" name="payment" value="inPerson">
        <label for="inPerson">In Person</label><br>

        <h2>Orientation Session</h2>
        <input type="radio" id="weekdayMornings" name="orientation" value="weekdayMornings">
        <label for="weekdayMornings">Weekday Mornings</label><br>

        <input type="radio" id="weekdayAfternoons" name="orientation" value="weekdayAfternoons">
        <label for="weekdayAfternoons">Weekday Afternoons</label><br>

        <input type="radio" id="weekdayEvenings" name="orientation" value="weekdayEvenings">
        <label for="weekdayEvenings">Weekday Evenings</label><br>

        <input type="radio" id="weekend" name="orientation" value="weekend">
        <label for="weekend">Weekend</label><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>


```

---