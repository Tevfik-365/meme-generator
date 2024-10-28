# Import
from flask import Flask, render_template, request, send_from_directory




app = Flask(__name__)


# Form results
@app.route('/', methods=['GET','POST'])
def index():
if request.method == 'POST':
# retrieve selected image
selected_image = request.form.get('image-selector')


# Task #2. Getting the text


# Task #3. Getting the position of the text


# Task #3. Getting the colour of the text


return render_template('index.html',
# Display the selected image
selected_image=selected_image,


# Task #2. Display text


# Task #3. Display colour
# Task #3. Display the position of text


)
else:
# Display the first image by default
return render_template('index.html', selected_image='logo.svg')




@app.route('/static/img/<path:path>')
def serve_images(path):
return send_from_directory('static/img', path)


app.run(debug=True)
