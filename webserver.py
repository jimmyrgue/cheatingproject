from flask import Flask, request, render_template_string
from typoer import typoer
app = Flask(__name__)

# HTML template for the form
html_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Text Input</title>
  </head>
  <body>
    <div style="margin: 50px;">
      <h1>Enter Text</h1>
      <form action="/" method="post">
        <textarea name="text" rows="4" cols="50" placeholder="Enter your text here"></textarea><br><br>
        <input type="submit" value="Submit">
      </form>
    </div>
  </body>
</html>
'''

textMAIN = ""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":


        text = request.form["text"]
        typoer(text, wpm = 85, accuracy = 0.99, wait_key = 'right', break_key = 'left')

        process_text(text)
        return render_template_string(html_template)
    return render_template_string(html_template)

def process_text(text):
    print("Processing text:", text)

if __name__ == "__main__":
    app.run(host="192.168.0.120", port=5000, debug=True)
