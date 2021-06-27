from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import send_file
from werkzeug.utils import secure_filename
import glob
import os
import json
import sys
import pdftotext as pdftotext
import Extraction as Extraction
import OntologyMapping as ontology
app = Flask(__name__, template_folder='Web/templates',static_folder='Web/static')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image',methods=['GET','POST'])
def file_pdf():
	value={'name':'image.png'}
	return jsonify(value)

@app.route('/demo_page', methods=['GET', 'POST'])
def demo_page():
    return render_template('index.html')

@app.route('/getjob')
def getJob():
	out_file = open("JobDescription.json", "r")
	data=json.load(out_file)
	return jsonify(data)

@app.route('/savejob',methods=['POST'])
def saveJob():
    data = request.json
    out_file = open("JobDescription.json", "w")  
    json.dump(data, out_file) 
    out_file.close() 
    return jsonify(data)

@app.route('/upload',methods=['POST'])
def upload_file():
	# pdfList=glob.glob("./Upload_Folder/*")
	# for f in pdfList:
	# 	os.remove(f)
	if 'files[]' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	
	files = request.files.getlist('files[]')
	
	errors = {}
	success = False
	
	for file in files:		
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join('Upload_Folder', filename))
			success = True
		else:
			errors[file.filename] = 'File type is not allowed'
	
	if success and errors:
		errors['message'] = 'File(s) successfully uploaded'
		resp = jsonify(errors)
		resp.status_code = 500
		return resp
	if success:
		resp = jsonify({'message' : 'Files successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify(errors)
		resp.status_code = 500
		return resp

@app.route('/process',methods=['POST'])
def processJobs():
	data = request.json
	returnList=ontology.OntologyMapping(data)
	return jsonify(returnList)

@app.route('/view',methods=['GET'])
def viewPdfs():
	pdf = request.args.get('pdf')
	return send_file('Upload_Folder/'+pdf, attachment_filename=pdf)

@app.route('/uploadsingle',methods=['POST'])
def upload_single_file():
	if 'files[]' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	
	files = request.files.getlist('files[]')
	textFile=""
	errors = {}
	success = False
	
	for file in files:		
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join('Demo_Upload', filename))
			textFile=pdftotext.pdf2txt_file(os.path.join('Demo_Upload', filename),os.path.join('Demo_Upload', 'processing.txt'))
			success = True
		else:
			errors[file.filename] = 'File type is not allowed'
	
	if success and errors:
		errors['message'] = 'File(s) successfully uploaded'
		resp = jsonify(textFile)
		resp.status_code = 500
		return resp
	if success:
		resp = jsonify({'message' : textFile})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify(errors)
		resp.status_code = 500
		return resp

@app.route('/allsingle')
def singe_Process():
	returnList=Extraction.concept_extraction_single()
	return jsonify(returnList)

if __name__ == "__main__":
	CORS(app)
	app.run(debug=True, host='127.0.0.1', port=5100)