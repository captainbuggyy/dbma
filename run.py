from flask import Flask, render_template, request, session,flash,get_flashed_messages,url_for,redirect,make_response
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
import mysql.connector
import pandas
import sklearn
import pickle
import requests
import numpy as np
app = Flask(__name__)
bcrypt=Bcrypt(app)
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="agr"
)
model = pickle.load(open('model.pkl','rb'))
sc = pickle.load(open('standscaler.pkl','rb'))
ms = pickle.load(open('minmaxscaler.pkl','rb'))
s=mydb.cursor(dictionary=True)
app.config['SECRET_KEY']="c61261c7b2ba8da70c004965"
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    N = request.form['Nitrogen']
    P = request.form['Phosphorus']
    K = request.form['Potassium']
    temp = request.form['Temperature']
    humidity = request.form['Humidity']
    ph = request.form['pH']
    rainfall = request.form['Rainfall']

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    return render_template('index.html',result = result)

@app.route('/')
@app.route('/home')
def home():
    session['user']=0
    print("satvat")
    return render_template('home.html',session=session)
@app.route('/crop')
def crop():
    item=[{'name':'DAL','soil_type':'red','season':'12'}]
   
    return render_template("crop.html",l=item)
def showland():
    cur=mydb.cursor()
    query1 = "SELECT * FROM land WHERE farmer_id = %s"
    cur.execute(query1,(session['ids'],))
    b = cur.fetchall()
    cur.close()
    return render_template('land.html', l=b)
@app.route('/profile',methods=['GET','POST'])
def profile():
    id=session['ids']
    cur=mydb.cursor(dictionary=True)
    query="select * from farmer where farmer_id=%s"
    cur.execute(query,(id,))
    a=cur.fetchall()
    query="select name from govt_schemes right join scheme_applied on scheme_applied.scheme_id=govt_schemes.scheme_id where farmer_id=%s"
    cur.execute(query,(id,))
    d=cur.fetchall()
    print(a)
    print("ddd"*1000)
    # print(id)
    query="SELECT count(*) from land WHERE approved=1 and farmer_id=%s"
    cur.execute(query,(id,));
    b=cur.fetchall()
    # print(type(b))
    a[0]['no_of_land']=b[0].get('count(*)')
    return render_template('profile.html',user=a[0],scheme=d)
@app.route('/land', methods=['GET', 'POST'])
def land():
    cur = mydb.cursor(dictionary=True)
    username = session['username']
    query = "SELECT id FROM user WHERE user_name = %s"
    cur.execute(query, (username,))
    l = cur.fetchall()
    
    if not l:
        cur.close()
        return "Farmer not found", 404
    
    k = session['ids']
    
    query1 = "SELECT * FROM land WHERE farmer_id = %s"
    cur.execute(query1, (k,))
    b = cur.fetchall()
    
    if request.method == 'POST':
        address = request.form['newLandAddress']
        survey_number = request.form['newSurveyNumber']
        soil_type = request.form['soil_type']
        land_area = request.form['land_area']

        pdf_file = request.files['pdf_file']
        pdf_data = pdf_file.read() if pdf_file else None
        if not address or not survey_number:
            cur.close()
            return "Invalid input", 400
        query = "INSERT INTO land (district, survey_no, farmer_id, land_area, soil_type, file) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (address, survey_number, k, land_area, soil_type, pdf_data))
        mydb.commit()
        query = "SELECT MAX(land_id) as ma FROM land"
        cur.execute(query)
        landid = cur.fetchone().get('ma')
        
        query = "INSERT INTO notification (farmer_id, land_id, type) VALUES (%s, %s, %s)"
        cur.execute(query, (k, landid, "land"))
        mydb.commit()
        
        # Refresh the land list after inserting new land
        cur.execute(query1, (k,))
        b = cur.fetchall()
    
    cur.close()
    return render_template('land.html', l=b)

@app.route('/govt_schemes',methods=['GET','POST'])
def govt_schemes():
    if request.method=='POST':
        cur=mydb.cursor(dictionary=True)
        scheme_id=request.form.get("scheme")
        pdf_file = request.files['pdf_file']
        pdf_data = pdf_file.read()
        query = "INSERT INTO notification (farmer_id, type,scheme_id,pd) VALUES (%s, %s,%s,%s)"
        cur.execute(query, (session['ids'], "govt_scheme",scheme_id,pdf_data))
        mydb.commit()
        flash('Successfully applied for the scheme.')
        return redirect(url_for('govt_schemes'))
    cur=mydb.cursor(dictionary=True)
    cur.execute("select * from govt_schemes")
    a=cur.fetchall()
    return render_template('govt_schemes.html',scheme=a)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # password=bcrypt.generate_password_hash(password).decode('utf-8')
        # print(password)
        cursor = mydb.cursor()
        query = "SELECT * FROM user WHERE user_name = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        query = "SELECT id FROM user WHERE user_name = %s"
        cursor.execute(query, (username,))
        farmer = cursor.fetchone()[0]
        cursor.close()
        if user:
            session['username'] =username
            session['ids']=farmer
            session['user']='user'
            return redirect(url_for('land'))
        else:
            return render_template('login.html', msg="Invalid username or password.")
    return render_template('login.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        print("hello")
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        
        cur = mydb.cursor()
        cur.execute("INSERT INTO user (user_name, email, PASSWORD) VALUES (%s, %s, %s)", (username, email, password))
        mydb.commit()

        cur.close()
        s.execute("select id from user where user_name=%s",(username,))
        ap=s.fetchall()
        id=ap[0].get('id')
        return redirect(url_for('info',id=id))
    return render_template('register.html')
@app.route('/info',methods=['GET','POST'])
def info():
    id = request.args.get('id', None)

    if request.method=='POST':
        name = request.form['name']
        phone_no = request.form['phone_no']
        district = request.form['district']
        state = request.form['state']
        village = request.form['village']
        email=request.form['email']
        query = "INSERT INTO farmer (farmer_id,name, contact, district, state, village,email) VALUES (%s,%s, %s, %s, %s, %s,%s)"
        # Execute the query using the existing cursor 's'
        s.execute(query, (id ,name, phone_no, district, state, village,email))
        mydb.commit()
        
        return redirect(url_for('login'))
    return render_template('info.html')
@app.route('/logout')
def logout():
    session.clear() 
    response = make_response(redirect(url_for('login')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response
@app.route('/delete_land/<int:id>', methods=['POST'])
def delete_land(id):
    mycursor=mydb.cursor()
    if 'username' not in session:
        return redirect(url_for('login'))
    username=session['username']
    mycursor.execute(f"DELETE FROM land WHERE land_id = {id}")
    mydb.commit()
    return redirect(url_for('land'))
@app.route('/admin')
def admin():
    if session['user']!='admin':
        return redirect(url_for('home'))
    cursor = mydb.cursor(dictionary=True)
    query = """
    SELECT 
    farmer.farmer_id, 
    Name, 
    email, 
    contact, 
    COUNT(land.land_id) AS no_of_land, 
    SUM(land.land_area) AS total_area,
    GROUP_CONCAT(distinct scheme_applied.scheme_id) AS scheme_ids
FROM 
    farmer
LEFT JOIN 
    land ON land.farmer_id = farmer.farmer_id
LEFT JOIN 
    scheme_applied ON scheme_applied.farmer_id = farmer.farmer_id
GROUP BY 
    farmer.farmer_id;

    """
    cursor.execute(query)
    farmers = cursor.fetchall()
    cursor.close()
    return render_template('admin.html', farmers=farmers)
@app.route('/notifications', methods=['GET', 'POST'])
def notifications():
    if session['user'] != "admin":
        return "error", 404
    if request.method == 'POST':
        action = request.form.get('action')
        notification_id = request.form.get('notification_id')
        type = request.form.get('type')

        cur = mydb.cursor(dictionary=True)
        
        if action == 'approve':
            
            if type == 'land':
                land_id = request.form.get('land_id')
                query = "UPDATE land SET approved = 1 WHERE land_id = %s"
                cur.execute(query, (land_id,))
                query="INSERT INTO farmer_notification (farmer_id, reason) SELECT farmer_id, %s FROM land WHERE land_id = %s"
                ans="your application for land is approved"
                cur.execute(query,(ans,land_id))
            else:
                scheme_id = request.form.get('scheme_id')
                farmer_id = request.form.get('farmer_id')
                query = "INSERT INTO scheme_applied (farmer_id, scheme_id) VALUES (%s, %s)"
                cur.execute(query, (farmer_id, scheme_id))
                query="Select name from govt_schemes where scheme_id=%s"
                cur.execute(query,(scheme_id,))
                a=cur.fetchall()[0].get('name')
                # print(a)
                query="Insert into farmer_notification(farmer_id,reason) values(%s,%s)"
                ans="your application for "+a+"is approved"
                cur.execute(query,(farmer_id,ans))

        elif action == 'reject':
            
            reason = request.form.get('rejection_reason')
            
            if type == 'land':
                land_id = request.form.get('land_id')
                query="INSERT INTO farmer_notification (farmer_id, reason) SELECT farmer_id, %s FROM land WHERE land_id = %s"
                ans="Rejected Land Application:"+reason
                cur.execute(query,(ans,land_id))
                query="delete from land where land_id=%s"
                cur.execute(query,(land_id,))
            else:
                farmer_id = request.form.get('farmer_id')
                scheme_id = request.form.get('scheme_id')
                query="Insert into farmer_notification(farmer_id,reason) values(%s,%s)"
                ans="Rejected Govt scheme application"+reason
                cur.execute(query,(farmer_id,ans))

        query = "DELETE FROM notification WHERE notification_id = %s"
        cur.execute(query, (notification_id,))
        mydb.commit()
        return redirect(url_for('notifications'))

    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM notification"
    cursor.execute(query)
    notifications = cursor.fetchall()

    formatted_notifications = []
    for notification in notifications:
        type = notification.get('type')
        farmer_id = notification.get('farmer_id')
        notification_id = notification.get('notification_id')
        scheme_id = notification.get('scheme_id')
        if type == 'land':
            land_id = notification.get('land_id')
            query = '''
                SELECT 
                    farmer.Name as farmer_name, land_id,
                    farmer.email, farmer.farmer_id, farmer.contact,
                    land.survey_no, land.land_area, land.file, land.district
                FROM 
                    land
                INNER JOIN 
                    farmer 
                ON 
                    land.farmer_id = farmer.farmer_id
                WHERE 
                    land.land_id = %s
                AND 
                    land.farmer_id = %s
            '''
            cursor.execute(query, (land_id, farmer_id))
            details = cursor.fetchone()
            print(details)
            print("00"*100)
            details['type'] = 'land'
            
            details['notification_id'] = notification_id
            details['farmer_id'] = farmer_id
            details['land_id'] = land_id  # Add land_id to details for modal form
            formatted_notifications.append(details)
        else:
            query = "SELECT * FROM farmer WHERE farmer_id = %s"
            cursor.execute(query, (farmer_id,))
            details = cursor.fetchone()
            print(details)
            print("00"*100)
            details['type'] = 'govt_scheme'
            details['notification_id'] = notification_id
            details['scheme_id']=scheme_id
            cur=mydb.cursor()
            query="Select name from govt_schemes where scheme_id=%s"
            cur.execute(query,(scheme_id,))
            a=cur.fetchall()[0][0]
            details['scheme_name']=a
            formatted_notifications.append(details)
    print(formatted_notifications)
    print("##"*100)
    return render_template('adminnotification.html', notifications=formatted_notifications)
@app.route('/farmernotification')
def farmernotification():
    farmer_id=session['ids']
    cur=mydb.cursor(dictionary=True)
    cur.execute("Select * from farmer_notification where farmer_id=%s order by notification_id desc",(farmer_id,))
    a=cur.fetchall()
    return render_template('farmernotification.html',notifications=a)
@app.route('/adminlogin',methods=['GET','POST'])
def adminlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # password=bcrypt.generate_password_hash(password).decode('utf-8')
        cursor = mydb.cursor()
        query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['user']='admin'
            return redirect(url_for('admin'))
        else:
            return render_template('admin.html', msg="Invalid username or password.")
    return render_template('adminlogin.html')
@app.route('/view_pdf/<int:land_id>')
def view_pdf(land_id):
    try:
        cur = mydb.cursor()
        query = "SELECT file FROM land WHERE land_id = %s"
        cur.execute(query, (land_id,))
        result = cur.fetchone()
        cur.close()
        
        if result and result[0]:
            pdf_data = result[0]
            with open(f"land_{land_id}.pdf", "wb") as f:
                f.write(pdf_data)
            response = make_response(pdf_data)
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = 'inline; filename=land_document.pdf'
            return response
        else:
            return "PDF not found", 404
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error retrieving PDF: {e}")
        return "An error occurred while retrieving the PDF", 500
@app.route('/view_pdf2/<int:notification_id>')
def view_pdf2(notification_id):
    try:
        cur = mydb.cursor()
        query = "SELECT pd FROM notification WHERE notification_id = %s"
        cur.execute(query, (notification_id,))
        result = cur.fetchone()
        cur.close()
        
        if result and result[0]:
            pdf_data = result[0]
            with open(f"scheme_{notification_id}.pdf", "wb") as f:
                f.write(pdf_data)
            response = make_response(pdf_data)
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = 'inline; filename=land_document.pdf'
            return response
        else:
            return "PDF not found", 404
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error retrieving PDF: {e}")
        return "An error occurred while retrieving the PDF", 500
@app.route('/govt_scheme_admin',methods=['GET','POST'])
def govt_scheme_admin():
    cur=mydb.cursor(dictionary=True)
    if request.method=='POST':
        query="Insert into govt_schemes(criteria_area,income,benefits,name) values(%s,%s,%s,%s)"
        cur.execute(query,(request.form.get('criteria_area'),request.form.get('income'),request.form.get('benefits'),request.form.get('name')))
        mydb.commit()
        return redirect(url_for('govt_scheme_admin'))
    query="Select * from govt_schemes"
    cur.execute(query)
    a=cur.fetchall()
    return render_template('govt_scheme_admin.html',existing_schemes=a)
@app.route('/allland',methods=['GET','POST'])
def allland():
    cur=mydb.cursor(dictionary=True)
    cur.execute("SELECT land.District,survey_no,Name,land_area from land join farmer on land.farmer_id=farmer.farmer_id order by land.district,Name")
    a=cur.fetchall()
    cur.close()
    return render_template('allland.html',farmers=a)

if __name__ == '__main__':
    app.run(debug=True)
