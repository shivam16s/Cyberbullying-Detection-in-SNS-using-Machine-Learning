from flask import Flask, render_template, request, url_for, Markup, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

hates = pickle.load(open('D:\BE project\Detection-of-cyberbullying-main\hate.pickle','rb'))

tfidf_vectorizer = pickle.load(open('D:/BE project/Detection-of-cyberbullying-main/tfid.pickle','rb'))

tfid_wikis = pickle.load(open('D:/BE project/Detection-of-cyberbullying-main/tfid_wiki.pkl','rb'))
wikis = pickle.load(open('D:\BE project\Detection-of-cyberbullying-main\wiki.pkl','rb'))
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/logins')
def logins():
    return render_template('logins.html')    
    
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)    
@app.route('/uploads')
def uploads():
    return render_template('uploads.html')  
@app.route('/previews',methods=["POST"])
def previews():
    if request.method == 'POST':
        datasets = request.files['datasetfile']
        df = pd.read_csv(datasets,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("previews.html",df_view = df) 

 
@app.route('/prediction')
def prediction():
 	return render_template("prediction.html")

#@app.route('/chart')
#def chart():
	#abc = request.args.get('news')	
	#input_data = [abc.rstrip()]
	# transforming input
	#tfidf_test = tfidf_vectorizer.transform(input_data)
	# predicting the input
	#y_pred = pac.predict(tfidf_test)
    #output=y_pred[0]
	#return render_template('chart.html', prediction_text='Review is {}'.format(y_pred[0])) 

@app.route('/check')
def check():	

	abc = request.args.get('news')	
	input_data = [abc.rstrip()]
	# transforming input
	# tfidf_test = tfid_wikis.transform(input_data)
	tfidf_test = tfidf_vectorizer.transform(input_data)
	# predicting the input
	y_pred = wikis.predict(tfidf_test)
	# y_pred = hates.predict(tfidf_test)
	if y_pred[0] == 1:         
		label='Offensive'
	elif y_pred[0] == 0:
		label='Non Offensive'
	return render_template('prediction.html', prediction_text=label) 
    
@app.route('/predictions')
def predictions():
 	return render_template("predictions.html")

#@app.route('/chart')
#def chart():
	#abc = request.args.get('news')	
	#input_data = [abc.rstrip()]
	# transforming input
	#tfidf_test = tfidf_vectorizer.transform(input_data)
	# predicting the input
	#y_pred = pac.predict(tfidf_test)
    #output=y_pred[0]
	#return render_template('chart.html', prediction_text='Review is {}'.format(y_pred[0])) 

@app.route('/attack')
def attack():	

	abc = request.args.get('attacks')	
	input_data = [abc.rstrip()]
	# transforming input
	tfidf_test = tfid_wikis.transform(input_data)
	# predicting the input
	y_pred = wikis.predict(tfidf_test)
	if y_pred[0] == 1:         
		label='Personal attack'
	elif y_pred[0] == 0:
		label='Non Personal attack'
	return render_template('predictions.html', prediction_text=label)    
    
    
    
@app.route('/chart')
def chart():
    return render_template('chart.html') 

@app.route('/charts')
def charts():
    return render_template('charts.html') 
@app.route('/performance')
def performance():
    return render_template('performance.html') 

@app.route('/performances')
def performances():
    return render_template('performances.html')     
    
if __name__=='__main__':
    app.run(debug=True)
