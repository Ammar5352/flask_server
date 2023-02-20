from flask import Flask,redirect,render_template,request,flash,Response,send_file
import uuid
import os
import json
from werkzeug.utils import secure_filename
from utils import file_valid
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] =r"D:/Flask/uploads/images/"
app.config['SECRET_KEY']='My secret'
@app.route('/',methods=["GET","POST"])


def index():
    if request.method=="POST":
        if request.files:
            f = request.files["file"]
            if f.filename=="":
                flash("Please select file")
                return redirect(request.url)
            else:
                if file_valid(f.filename):
                    x= uuid.uuid4()
                    x_str= str(x)
                    filename = secure_filename(f.filename)
                    filename = x_str+'.'+filename.split('.')[-1]
                    f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))  
                    y={
                        'filepath':app.config['UPLOAD_FOLDER']+filename
                    }
                    z=json.dumps(y)
                    return Response(z,mimetype='application/json')   
                else:
                    flash('Invalid file type')
                    return redirect(request.url) 
    return render_template('index.html')

@app.route('/<string:uuid>')

def image_info(uuid):
    path='D:/Flask/uploads/images/{}'.format(uuid)
    if os.path.isfile(path):
        return send_file(path)
    else:
        return 'File not found'

if __name__=='__main__':
    app.run(debug=True)