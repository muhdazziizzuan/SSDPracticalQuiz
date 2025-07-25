from flask import Flask, render_template_string, request, redirect, url_for, session
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session

#Function to validate input against XSS and allow only safe characters
def is_valid_search_term(term):
    # Allow only alphanumeric and spaces
    return bool(re.fullmatch(r'[A-Za-z0-9 ]{1,100}', term))

def is_sql_injection(term):
    # Simple patterns for SQL injection detection (expand as needed)
    sql_patterns = [
        r"('|\"|;|--|#|/\*|\*/|\bOR\b|\bAND\b|\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bDROP\b|\bUNION\b|\bWHERE\b)",
    ]
    for pattern in sql_patterns:
        if re.search(pattern, term, re.IGNORECASE):
            return True
    return False

HTML_FORM = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Search Page</title>
</head>
<body>
    <h1>Search</h1>
    <form method="POST">
        <input type="text" name="search_term" placeholder="Enter search term" value="{{ input_value }}" required>
        <button type="submit">Submit</button>
    </form>
    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    input_value = ''
    if request.method == 'POST':
        user_input = request.form.get('search_term', '')
        if is_sql_injection(user_input):
            error = "SQL injection patterns are not allowed."
            input_value = ''
        elif not is_valid_search_term(user_input):
            error = "Invalid input. Only letters, numbers, and spaces are allowed."
            input_value = ''
        else:
            session['search_term'] = user_input
            return redirect(url_for('result'))
    return render_template_string(HTML_FORM, error=error, input_value=input_value)

@app.route('/result')
def result():
    search_term = session.get('search_term', None)
    return render_template_string(RESULT_PAGE, search_term=search_term)

RESULT_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Search Result</title>
</head>
<body>
    <h1>Search Result</h1>
    {% if search_term %}
        <p>You searched for: <strong>{{ search_term }}</strong></p>
    {% else %}
        <p>No search term provided.</p>
    {% endif %}
    <form action="/" method="get">
        <button type="submit">Return to Home</button>
    </form>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 