from flask import Flask, render_template, request, session,flash,get_flashed_messages,url_for,redirect,make_response
from flask_mysqldb import MySQL
# from flask
from flask_bcrypt import Bcrypt
import mysql.connector
import requests

app = Flask(__name__)
bcrypt=Bcrypt(app)
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="agriculture"
)
s=mydb.cursor(dictionary=True)
# session['user']=0
app.config['SECRET_KEY']="c61261c7b2ba8da70c004965"
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
    cur.execute(query,(id,));
    a=cur.fetchall()
    # print(id)
    query="SELECT count(*) from land WHERE approved=1 and farmer_id=%s"
    cur.execute(query,(id,));
    b=cur.fetchall()
    # print(type(b))
    a[0]['no_of_land']=b[0].get('count(*)')
    print(a[0]['no_of_land'])
    # print()
    # for key,val in a[0]:
        # 
        # print(key,":",val," ")
    print("*"*1000)
    # if request.method==
    return render_template('profile.html',user=a[0])
# @app.route('/land', methods=['GET', 'POST'])
# def land():
#     cur = mydb.cursor(dictionary=True)
#     username = session['username']
    
#     # Use parameterized query to avoid SQL injection
#     query = "SELECT id FROM user WHERE user_name = %s"
#     cur.execute(query, (username,))
#     l = cur.fetchall()
    
#     if not l:
#         cur.close()
#         return "Farmer not found", 404
    
#     k = session['ids']
    
#     query1 = "SELECT * FROM land WHERE farmer_id = %s"
#     cur.execute(query, (k,))
#     b = cur.fetchall()
    
#     if request.method == 'POST':
#         address = request.form['newLandAddress']
#         survey_number = request.form['newSurveyNumber']
#         soil_type=request.form['soil_type']
#         land_area=request.form['land_area']
#         pdf_file = request.files['pdf_file']
#         pdf_data = pdf_file.read() if pdf_file else None
#         # Validate form data (basic example)
#         if not address or not survey_number:
#             cur.close()
#             return "Invalid input", 400
        
#         # Use parameterized query to avoid SQL injection
#         query = "INSERT INTO land (district, survey_no, farmer_id,land_area,soil_type,file) VALUES (%s, %s, %s,%s,%s,%s)"
#         cur.execute(query, (address, survey_number, k,land_area,soil_type,pdf_data))
#         mydb.commit()
#         query="select max(land_id) as ma from land"
#         cur.execute(query)
#         landid=cur.fetchone().get('ma')
#         print(landid)
#         print('*'*1000)
#         query="insert into notification(farmer_id,land_id,type)values(%s,%s,%s)"
#         cur.execute(query,(k,landid,"land"))
#         mydb.commit()
        
#         # Refresh the land list after inserting new land
#     cur.execute(query1,(k,))
#     b = cur.fetchall()
    
#     cur.close()
#     return render_template('land.html', l=b)
@app.route('/land', methods=['GET', 'POST'])
def land():
    cur = mydb.cursor(dictionary=True)
    username = session['username']
    
    # Use parameterized query to avoid SQL injection
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
        
        # Handle file upload
        pdf_file = request.files['pdf_file']
        pdf_data = pdf_file.read() if pdf_file else None
        
        # Validate form data
        if not address or not survey_number:
            cur.close()
            return "Invalid input", 400
        
        # Use parameterized query to avoid SQL injection
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
        print('1'*1000)
        scheme_id=request.form.get("scheme")
        query = "INSERT INTO notification (farmer_id, type) VALUES (%s, %s)"
        cur.execute(query, (session['ids'], "govt_scheme"))
        print(session['ids'])
        mydb.commit()
    cur=mydb.cursor(dictionary=True)
    cur.execute("select * from govt_schemes")
    a=cur.fetchall()
    return render_template('govt_schemes.html',scheme=a)
@app.route('/edit_land', methods=['POST'])
def edit_land():
    mycursor=mydb.cursor(dictionary=True)
    if 'username' not in session:
        return redirect(url_for('login'))
    id = request.form.get('id')
    # id=session['ids']

    address = request.form['editLandAddress']
    print(address*100)
    survey_number = request.form['editSurveyNumber']
    mycursor.execute(
    "UPDATE land SET district = %s, survey_no = %s WHERE land_id = %s",
    (address, survey_number, id))
    mydb.commit()
    # query="insert into notification(farmer_id,land_id,type)values(%s,%s,%s)"
    #     cur.execute(query,(id,landid,"land"))
    #     mydb.commit()
    # showland()
    return redirect(url_for('land'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # password=bcrypt.generate_password_hash(password).decode('utf-8')
        cursor = mydb.cursor()
        query = "SELECT * FROM user WHERE user_name = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        query = "SELECT id FROM user WHERE user_name = %s"
        cursor.execute(query, (username,))
        farmer = cursor.fetchone()[0]
        # print(farmer)
        # print(1000*'*')
        cursor.close()
        if user:
            # print(id*1000)
            session['username'] =username
            session['ids']=farmer
            session['user']='user'
            return redirect(url_for('land'))
        else:
            # Invalid credentials
            # Render login page with error message
            flash(f'Account created successfully  as sex',category='success')
            return render_template('login.html', msg="Invalid username or password.")
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        print("hello")
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # print(password)
        # password=bcrypt.generate_password_hash(password).decode('utf-8')
        # print(password)
        
        cur = mydb.cursor()
        cur.execute("INSERT INTO user (user_name, email, PASSWORD) VALUES (%s, %s, %s)", (username, email, password))
        mydb.commit()

        cur.close()
        s.execute("select id from user where user_name=%s",(username,))
        ap=s.fetchall()
        id=ap[0].get('id')
        return redirect(url_for('info',id=id))
        # return render_template('info.html')
       
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
        
        # cur=mydb.cursor()
        print('*'*100)
        query = "INSERT INTO farmer (farmer_id,name, contact, district, state, village,email) VALUES (%s,%s, %s, %s, %s, %s,%s)"
        # Execute the query using the existing cursor 's'
        s.execute(query, (id ,name, phone_no, district, state, village,email))
        mydb.commit()
        
        return redirect(url_for('login'))
        return render_template('info.html')
    return render_template('info.html')
@app.route('/logout')
def logout():
    session.clear()  # Clear the session
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
    # a=mycursor.execute(f"select land_id from farmer where Name='{username}'")
    # a=a[0].get('farmer_id')
    mycursor.execute(f"DELETE FROM land WHERE land_id = {id}")
    mydb.commit()
    return redirect(url_for('land'))
@app.route('/admin')
def admin():
    if session['user']!='admin':
        return redirect(url_for('home'))
    cursor = mydb.cursor(dictionary=True)
    query = """
    SELECT farmer.farmer_id, Name, email, contact, COUNT(land.land_id) AS no_of_land, SUM(land.land_area) AS total_area
FROM farmer
LEFT JOIN land ON land.farmer_id = farmer.farmer_id
GROUP BY farmer.farmer_id


    """
    cursor.execute(query)
    farmers = cursor.fetchall()
    cursor.close()
    return render_template('admin.html', farmers=farmers)
@app.route('/notifications',methods=['GET','POST'])
def notifications():
    if session['user']!="admin":
        return "error",404
    if request.method == 'POST':
        land_id = request.form.get('land_id')
        notification_id = request.form.get('notification_id')
        action = request.form.get('action')
        scheme_id=request.form.get('scheme_id')
        farmer_id=request.form.get('farmer_id')
        type=request.form.get('type')
        print(notification_id*2)
        print('&'*1000)
        cur=mydb.cursor(dictionary=True)
        if action == 'approve':
            if type=='land':
                query="UPDATE land set approved=1 where land_id=%s"
                cur.execute(query,(land_id,))
            else:
                query="insert into scheme_applied(farmer_id,scheme_id) values(%s,%s)"
                cur.execute(query,(farmer_id,scheme_id))
             
            pass
        elif action == 'reject':
            reason=request.form.get("rejection_reason")
            query="UPDATE land set approved=%s where land_id=%s"
            cur.execute(query,(reason,land_id)) 
            pass
        query="delete from notification where notification_id=%s"
        cur.execute(query,(land_id,))

    cursor=mydb.cursor(dictionary=True)
    query="select * from notification"
    cursor.execute(query)
    a=cursor.fetchall()
    print(a)
    l=[]
    noti=[]
    for i in range(len(a)):
        type=a[i].get('type')
        farmer_id=a[i].get('farmer_id')
        notification_id=int(a[i].get('notification_id'))
        if(type=='land'):
            landid=a[i].get('land_id')
            query='''SELECT 
        farmer.Name as farmer_name,land_id,
        farmer.email as email,
        farmer.farmer_id as farmer_id,
        farmer.contact as contact,
        land.survey_no ,
        land.land_area,
        land.file,
        land.district
    FROM 
        land
    INNER JOIN 
        farmer 
    ON 
        land.farmer_id = farmer.farmer_id
    WHERE 
        land.land_id = %s
    AND 
        land.farmer_id = %s'''

            cursor.execute(query,(landid,farmer_id))
            name=cursor.fetchall()[0]
            name['type']='land'
            l.append(name)
        else:
            query="Select * from farmer where farmer_id=%s"
            cursor.execute(query,(farmer_id,))
            name=cursor.fetchall()[0]
            # print(name)
            name['land_id']=0
            name['type']='govt_scheme'
            name['notifcation_id']=notification_id
            # print('1'*1000)
            l.append(name)
            
    return render_template('adminnotification.html', notifications=l)
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
        # cursor.execute(query, (username,))
        # print(farmer)
        # print(1000*'*')
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
@app.route('/allland',methods=['GET','POST'])
def allland():
    cur=mydb.cursor(dictionary=True)
    cur.execute("SELECT land.District,survey_no,Name,land_area from land join farmer on land.farmer_id=farmer.farmer_id order by land.district,Name")
    a=cur.fetchall()
    cur.close()
    return render_template('allland.html',farmers=a)

if __name__ == '__main__':
    app.run(debug=True)
