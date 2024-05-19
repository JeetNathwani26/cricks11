from flask import Flask, render_template, request,flash,redirect,session,url_for
import mysql.connector

app = Flask(__name__,static_url_path='/static')
app.secret_key="login form"



@app.route("/")
def index():
    return render_template("login.html")

b=[]
f=[]
a=0
g=[]
v=0
h=[]
s=0
@app.route("/login",methods=["POST"])
def login():
    global a,v,s
    t1=request.form.get('username')
    session['name']=t1
    t2=request.form.get('password')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from register where name=%s and password=%s",(t1,t2,))
    db=cur.fetchall()
    count=cur.rowcount
    con.close()
   
    if count==1:
        b.clear()
        f.clear()
        g.clear()
        print(g)
        h.clear()
        print(h)
        if a==1:
            a=a-len(b)
        if v==1 and s==1:
            v=v-1
            s=s-1
        print(v)
        print(s)    
        return redirect(url_for("home"))        
    else:
        return redirect("logout")
   
        
        



# register page....
@app.route("/sign")
def sign():
    return render_template("register.html ")       
@app.route("/sign-up",methods=["POST"])
def register():
      t1=request.form.get('username')
      t3=request.form.get('password')
      t4=request.form.get('cname')
      print(t4)
      con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
      cur=con.cursor()
      cur.execute("Select * from register where name=%s",(request.form.get('username'),))
      dc=cur.fetchall()
      if dc:
        flash("user alerdy exist....")
        return render_template("register.html")
      else:    
            cur.execute("insert into register values (%s,%s,%s)",(
                                                             t1,
                                                            t3,
                                                            t4
                                                            
                                                            ))
        

            con.commit()
            return redirect(url_for('logout'))
      
       

# forget passwrd

@app.route("/forget")
def forget():
    return render_template("forget.html")
@app.route("/forgetup",methods=["POST"])
def forgetup():
      t1= request.form.get('username')
      t2=request.form.get('password')
      t3=request.form.get('cname')
      con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
      cur=con.cursor()
      cur.execute("update register set password=%s where name=%s and cname=%s",(t2,t1,t3))
      con.commit()
      con.close()
      flash("password update successfully....")
      return redirect(url_for('logout'))


# log-out ....
@app.route("/logout")
def logout():
    return render_template("login.html")

#home...
@app.route("/home")
def home():
    global a,v,s
    a=a-len(b)
    b.clear()
    f.clear()
    g.clear()
    h.clear()
    if v==1 and s==1:
        v=v-1
        print(v)
        s=s-1
        print(s)
    q4=session.get('name')
    q3=q4[0]
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("Select * from match1  where updates='upcomming' ")
    dc=cur.fetchall()
    cur.execute("Select * from adverties ")
    dw=cur.fetchall()
    con.close()
    return render_template("home.html",user=q3.upper(),sw=dc,dw=dw)

@app.route("/contest/<t2>/<t3>/<t4>",methods=["GET"])
def con(t2,t3,t4):
    q4=session.get('name')
    q3=q4[0]
    session['team1']=t2
    session['team2']=t3
    session['mid']=t4
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("Select * from vouchers where id=%s",(t4,))
    dc=cur.fetchall()
    
    con.close()
    return render_template("contest.html",hi1=t2,hi2=t3,user=q3.upper(),bn=dc)

@app.route("/con1")
def con1():
    return redirect(url_for('con',t2=session.get('team1'),t3=session.get('team2'),t4=session.get('mid')))

@app.route("/Mlive")
def Mlive():
   q4=session.get('name')
   q3=q4[0]
   con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
   cur=con.cursor()
   cur.execute("Select * from  match1  where updates='live' ")
   dc=cur.fetchall()
   cur.execute("Select * from adverties ")
   dw=cur.fetchall()
   con.close()
   return render_template("Mlive.html",user=q3.upper(),sw=dc,dw=dw)

@app.route("/Mcompleted")
def Mcompleted():
   q4=session.get('name')
   q3=q4[0]
   con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
   cur=con.cursor()
   cur.execute("Select * from  match1  where updates='complete' ")
   dc=cur.fetchall()
   cur.execute("Select * from adverties ")
   dw=cur.fetchall()
   con.close()
   return render_template("Mcompleted.html",user=q3.upper(),sw=dc,dw=dw)

@app.route("/splayer/<id1>/<id2>/<id3>",methods=['GET'])
def splayer(id1,id2,id3):
    q4=session.get('name')
    q3=q4[0]
    session['vid']=id1
    session['vname']=id2
    session['vimg']=id3
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("Select * from userteam where name=%s and matchid=%s",(session.get('name'),session.get('mid')))
    db=cur.fetchall()
    cur.execute("select * from uservoucher where name=%s and matchid=%s and vid=%s",(session.get('name'),session.get('mid'),session.get('vid')))
    dw=cur.fetchall() 
    if db:
         if dw:
             return redirect(url_for('mycontest'))
         else: 
            return redirect(url_for('join'))
    cur=con.cursor()
    cur.execute("Select * from  player where tame=%s and selection='wicketkeeper'",(session.get('team1'),))
    dc=cur.fetchall()
    cur.execute("Select * from  player where tame=%s and selection='wicketkeeper' ",(session.get('team2'),))
    dc1=cur.fetchall()
    con.close()
    return render_template("splayer.html",hi1=session.get('team1'),hi2=session.get('team2'),user=q3.upper(),bn=dc,bn1=dc1,n=a,n1=c,d=b,f=f)     
 
@app.route('/sp')
def sp():
    return redirect(url_for('splayer',id1=session.get('vid'),id2=session.get('vname'),id3=session.get('vimg'))) 

  
    
        

    

@app.route("/sbat")
def sbat():
    q4=session.get('name')
    q3=q4[0]
    u='batsman'
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("Select * from  player where tame=%s and selection='batsman'",(session.get('team1'),))
    dc=cur.fetchall()
    cur.execute("Select * from  player where tame=%s and selection='batsman' ",(session.get('team2'),))
    dc1=cur.fetchall()
    con.close() 
    return render_template("sbat.html",hi1=session.get('team1'),hi2=session.get('team2'),user=q3.upper(),bn=dc,bn1=dc1,n=a,n1=c,d=b,f=f)

@app.route("/sallr")
def sallr():
    q4=session.get('name')
    q3=q4[0]
    u='allrounder'
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("Select * from  player where tame=%s and selection='allrounder'",(session.get('team1'),))
    dc=cur.fetchall()
    cur.execute("Select * from  player where tame=%s and selection='allrounder' ",(session.get('team2'),))
    dc1=cur.fetchall()
    con.close()
    return render_template("sallr.html",hi1=session.get('team1'),hi2=session.get('team2'),user=q3.upper(),bn=dc,bn1=dc1,n=a,n1=c,d=b,f=f)

@app.route("/sbow")
def sbow():
    q4=session.get('name')
    q3=q4[0]
    u='bowler'
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("Select * from  player where tame=%s and selection='bowler'",(session.get('team1'),))
    dc=cur.fetchall()
    cur.execute("Select * from  player where tame=%s and selection='bowler' ",(session.get('team2'),))
    dc1=cur.fetchall()
    con.close()
    return render_template("sbow.html",hi1=session.get('team1'),hi2=session.get('team2'),user=q3.upper(),bn=dc,bn1=dc1,n=a,n1=c,d=b,f=f)
c=11
@app.route("/uplayer/<i>/<i2>")
def uplayer(i,i2):
    global a
    a=a+1
    b.append(i)
    f.append(i2)   
    g=session.get('vid')
    print(g)
    return redirect(url_for('splayer',id1=session.get('vid'),id2=session.get('vname'),id3=session.get('vimg')))
@app.route("/dplayer/<i>/<i2>")
def dplayer(i,i2):
    global a     
    b.remove(i)
    f.remove(i2)
    a=a-1
    return redirect(url_for('splayer',id1=session.get('vid'),id2=session.get('vname'),id3=session.get('vimg')))
@app.route("/uplayer1/<i>/<i2>")
def uplayer1(i,i2):
    global a
    a=a+1
    b.append(i)
    f.append(i2)   
    return redirect(url_for('sbat'))
@app.route("/dplayer1/<i>/<i2>")
def dplayer1(i,i2):
    global a     
    b.remove(i)
    f.remove(i2)
    a=a-1
    return redirect(url_for('sbat'))
@app.route("/uplayer2/<i>/<i2>")
def uplayer2(i,i2):
    global a
    a=a+1
    b.append(i)
    f.append(i2)   
    return redirect(url_for('sallr'))
@app.route("/dplayer2/<i>/<i2>")
def dplayer2(i,i2):
    global a     
    b.remove(i)
    f.remove(i2)
    a=a-1
    return redirect(url_for('sallr'))
@app.route("/uplayer3/<i>/<i2>")
def uplayer3(i,i2):
    global a
    b.append(i)
    f.append(i2)
    a=a+1   
    return redirect(url_for('sbow'))
@app.route("/dplayer3/<i>/<i2>")
def dplayer3(i,i2):
    global a     
    b.remove(i)
    f.remove(i2)
    a=a-1
    return redirect(url_for('sbow'))



@app.route("/show")
def show(): 
    q4=session.get('name')
    q3=q4[0]  
    return render_template('allplayer.html',vb=b,vb2=f,g=g,v=v,h=h,s=s,hi1=session.get('team1'),hi2=session.get('team2'),user=q3.upper(),d=b,f=f)

@app.route("/uplayer4/<i>/<i2>")
def uplayer4(i,i2):
    global v
    g.append(i)
    g.append(i2)
    v=v+1   
    return redirect(url_for('show'))
@app.route("/dplayer4/<i>/<i2>")
def dplayer4(i,i2):
    global v    
    g.remove(i)
    g.remove(i2)
    v=v-1
    return redirect(url_for('show'))

@app.route("/uplayer5/<i>/<i2>")
def uplayer5(i,i2):
    global s
    h.append(i)
    h.append(i2) 
    s=s+1  
    return redirect(url_for('show'))
@app.route("/dplayer5/<i>/<i2>")
def dplayer5(i,i2):
    global s   
    h.remove(i)
    h.remove(i2)
    s=s-1
    return redirect(url_for('show'))


@app.route("/show1/<d0>/<f0>/<d1>/<f1>/<d2>/<f2>/<d3>/<f3>/<d4>/<f4>/<d5>/<f5>/<d6>/<f6>/<d7>/<f7>/<d8>/<f8>/<d9>/<f9>/<d10>/<f10>/<g0>/<g1>/<h0>/<h1>",methods=["GET"])
def show1(d0,f0,d1,f1,d2,f2,d3,f3,d4,f4,d5,f5,d6,f6,d7,f7,d8,f8,d9,f9,d10,f10,g0,g1,h0,h1):
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("insert into userteam values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(session.get('name'),session.get('mid'),d0,f0,d1,f1,d2,f2,d3,f3,d4,f4,d5,f5,d6,f6,d7,f7,d8,f8,d9,f9,d10,f10,g0,g1,h0,h1))
    dc=cur.fetchall()
    con.commit()
    global a
    global v,s
    a=a-len(b)
    b.clear()
    f.clear()
    v=v-1
    g.clear()
    s=s-1 
    g.clear()
    return redirect(url_for('myteam'))

@app.route("/myteam")
def myteam():
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select ca,caimg,vc,vcimg from userteam where name=%s and matchid=%s",(session.get('name'),session.get('mid')))
    dc=cur.fetchall()
    cur.execute("select player1,img1,player2,img2,player3,img3,player4,img4,player5,img5,player6,img6,player7,img7,player8,img8,player9,img9,player10,img10,player11,img11 from userteam where name=%s and matchid=%s",(session.get('name'),session.get('mid')))
    d1=cur.fetchall()
    print(d1)
    return render_template('myteam.html',hi1=session.get('team1'),hi2=session.get('team2'),user=q3.upper(),ca=dc,d1=d1)
@app.route('/join')
def join():
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select ca,caimg,vc,vcimg from userteam where name=%s and matchid=%s",(session.get('name'),session.get('mid'),))
    dc=cur.fetchall()
    print(dc)
    return render_template('join.html',ca=dc,user=q3.upper())
@app.route("/join1")
def join1():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    print(session.get('vid'))
    cur.execute("select * from uservoucher where vid=%s ",(session.get('vid'),))
    df=cur.fetchall()
    print(df)
    dc1=cur.rowcount
    print(dc1)
    if dc1==5:
        flash("voucher contest is full..")
        return  redirect(url_for('con1'))
    else:
       cur.execute("INSERT INTO uservoucher VALUES (%s, %s, %s, %s, %s,%s)", (session.get('name'), session.get('mid'), session.get('vname'), session.get('vimg'), session.get('vid'),'0'))
       dc=cur.fetchall()
       con.commit() 
       flash("join voucher contest..")
       return  redirect(url_for('mycontest'))
    

@app.route("/mycontest")
def mycontest():
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from uservoucher where name=%s and matchid=%s ",(session.get('name'),session.get('mid')))
    dc=cur.fetchall()
    con.close()
    return  render_template('mycontest.html',hi1=session.get('team1'),hi2=session.get('team2'),user=q3.upper(),dc=dc)

@app.route('/user')
def user():
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from uservoucher where  vid=%s and matchid=%s ",(session.get('vid'),session.get('mid')))
    dc=cur.fetchall()
    con.close()
    return render_template('userpoint.html',hi1=session.get('team1'),hi2=session.get('team2'),user=q3.upper(),bn=dc)
 
@app.route("/mycontest1/<i>/<j>/<j1>")
def mycontest1(i,j,j1):
    q4=session.get('name')
    q3=q4[0] 
    session['li']=i
    session['j']=j
    session['j1']=j1
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from uservoucher where name=%s and matchid=%s ",(session.get('name'),i,))
    dc=cur.fetchall()
    con.close()
    return  render_template('mycontest1.html',hi1=session.get('j'),hi2=session.get('j1'),user=q3.upper(),dc=dc) 
@app.route('/myc1')
def myc1():
    return redirect(url_for('mycontest1',i=session.get('li'),j=session.get('j'),j1=session.get('j1')))
@app.route("/myteam1")
def myteam1():
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select ca,caimg,vc,vcimg from userteam where name=%s and matchid=%s",(session.get('name'),session.get('li')))
    dc=cur.fetchall()
    cur.execute("select player1,img1,player2,img2,player3,img3,player4,img4,player5,img5,player6,img6,player7,img7,player8,img8,player9,img9,player10,img10,player11,img11 from userteam where name=%s and matchid=%s",(session.get('name'),session.get('li')))
    d1=cur.fetchall()
    return render_template('myteam1.html',hi1=session.get('j'),hi2=session.get('j1'),user=q3.upper(),ca=dc,d1=d1) 


@app.route("/score")
def score():
    b=0
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select  player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11 from userteam where matchid=%s and name=%s",(session.get('li'),session.get('name')))
    data=cur.fetchall()
    v=[]
    for h in data:
       for j in h: 
          v.append(j)
    print(v)    
    cur.execute("select point from score where matchid=%s and (name=%s or name=%s or name=%sor name=%sor name=%sor name=%sor name=%sor name=%sor name=%sor name=%sor name=%s)",(session.get('li'),v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10]))
    dc=cur.fetchall() 
    print(dc)
    
    a=[]
    for i in dc:
       for e in i:
          a.append(e)
    b=sum(int(x) for x in a ) 
    print(a)
    print(session.get('name'))
    cur.execute("SELECT * FROM `userpoint` WHERE name=%s and matchid=%s",(session.get('name'),session.get('li'),))
    fg=cur.fetchall()
    print(fg)   
    if fg:
       cur.execute("update userpoint set point=%s where name=%s and matchid=%s",(b,session.get('name'),session.get('li'),))
       con.commit()
    else:

      cur.execute("insert into userpoint values(%s,%s,%s)",(session.get('name'),session.get('li'),b))
      con.commit()     
    cur.execute("select name,point from userpoint where name=%s and matchid=%s",(session.get('name'),session.get('li'),))
    gh=cur.fetchall() 
    con.close()   
    return render_template('score.html',hi1=session.get('j'),hi2=session.get('j1'),user=q3.upper(),gh=gh)

@app.route('/user1/<id>')
def user1(id):
    b=0
    q4=session.get('name')
    q3=q4[0] 
    print(id)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select  player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11 from userteam where matchid=%s and name=%s",(session.get('li'),session.get('name')))
    data=cur.fetchall()
    v=[]
    for h in data:
       for j in h: 
          v.append(j)
    print(v)    
    cur.execute("select point from score where matchid=%s and (name=%s or name=%s or name=%sor name=%sor name=%sor name=%sor name=%sor name=%sor name=%sor name=%sor name=%s)",(session.get('li'),v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10]))
    dc=cur.fetchall() 
    
    a=[]
    for i in dc:
       for e in i:
          a.append(e)
    b=sum(int(x) for x in a ) 
    print(a)  
    print(b)   
    cur.execute("update uservoucher set point=%s where name=%s and matchid=%s",(b,session.get('name'),session.get('li'),))
    con.commit() 

    cur.execute("select name,point from uservoucher where  matchid=%s and vid=%s order by point desc ",(session.get('li'),id,))
    dc=cur.fetchall()
    con.close()
    return render_template('userpoint.html',hi1=session.get('j'),hi2=session.get('j1'),user=q3.upper(),bn=dc)


@app.route("/mscore")
def mscore():
    q4=session.get('name')
    q3=q4[0] 
    b=0
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    hi=session.get('j')
    
    cur.execute("select trun from score where team=%s and matchid=%s ",(hi,session.get('li')))
    dc=cur.fetchall()
    print(dc)
    a=[]
    for i in dc:
       for e in i: 
        a.append(e)
    print(a)
    b=sum(int(x) for x in a )
    e=0
    hi2=session.get('j1')
    cur.execute("select whicket from score where team=%s and matchid=%s ",(hi2,session.get('li')))
    dw=cur.fetchall()
    c=[]
    for i in dw:
       for e in i: 
        c.append(e)
    print(c)
    e=sum(int(x) for x in c )
    t=0
    cur.execute("select trun from score where team=%s and matchid=%s ",(hi2,session.get('li')))
    dr=cur.fetchall()
    t1=[]
    for i in dr:
       for e in i: 
        t1.append(e)
    print(t1)
    t=sum(int(x) for x in t1 )
    u=0
    cur.execute("select whicket from score where team=%s and matchid=%s ",(hi,session.get('li')))
    dg=cur.fetchall()
    u1=[]
    for i in dg:
       for e in i: 
        u1.append(e)
    print(u1)
    u=sum(int(x) for x in u1 )
    cur.execute("select name,trun,tball,point from score where team=%s and matchid=%s ",(session.get('j'),session.get('li')))
    da=cur.fetchall()
    cur.execute("select name,run,whicket,over1,point from score where team=%s and (selection='bowler' or selection='allrounder') and matchid=%s ",(session.get('j1'),session.get('li')))
    da1=cur.fetchall()
    cur.execute("select name,trun,tball,point from score where team=%s  and matchid=%s ",(session.get('j1'),session.get('li')))
    daa=cur.fetchall()
    cur.execute("select name,run,whicket,over1,point from score where team=%s and (selection='bowler' or selection='allrounder') and matchid=%s ",(session.get('j'),session.get('li')))
    da2=cur.fetchall()
    con.close()
    return render_template("matchscore.html",b=b,e=e,t=t,u=u,da=da,daa=daa,da1=da1,da2=da2,user=q3.upper(),hi1=session.get('j'),hi2=session.get('j1'))

#mcompleted code... 
@app.route("/my2/<i>/<j>/<j1>")
def my2(i,j,j1):
    q4=session.get('name')
    q3=q4[0] 
    session['l1']=i
    session['l2']=j
    session['l3']=j1
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from uservoucher where name=%s and matchid=%s ",(session.get('name'),i,))
    dc=cur.fetchall()
    con.close()
    return  render_template('mycontest2.html',hi1=session.get('l2'),hi2=session.get('l3'),user=q3.upper(),dc=dc) 

@app.route('/mc1')
def mc1():
    return redirect(url_for('my2',i=session.get('l1'),j=session.get('l2'),j1=session.get('l3')))

@app.route("/myteam2")
def myteam2():
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select ca,caimg,vc,vcimg from userteam where name=%s and matchid=%s",(session.get('name'),session.get('l1')))
    dc=cur.fetchall()
    cur.execute("select player1,img1,player2,img2,player3,img3,player4,img4,player5,img5,player6,img6,player7,img7,player8,img8,player9,img9,player10,img10,player11,img11 from userteam where name=%s and matchid=%s",(session.get('name'),session.get('l1')))
    d1=cur.fetchall()
    return render_template('myteam2.html',hi1=session.get('l2'),hi2=session.get('l3'),user=q3.upper(),ca=dc,d1=d1) 


@app.route("/mscore1")
def mscore1():
    q4=session.get('name')
    q3=q4[0] 
    b=0
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select trun from score where team=%s and matchid=%s ",(session.get('l2'),session.get('l1')))
    dc=cur.fetchall()
    a=[]
    for i in dc:
       for e in i: 
        a.append(e)
    print(a)
    b=sum(int(x) for x in a )
    e=0
    cur.execute("select whicket from score where team=%s and matchid=%s ",(session.get('l3'),session.get('l1')))
    dw=cur.fetchall()
    c=[]
    for i in dw:
       for e in i: 
        c.append(e)
    print(c)
    e=sum(int(x) for x in c )
    t=0
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select trun from score where team=%s and matchid=%s ",(session.get('l3'),session.get('l1')))
    dr=cur.fetchall()
    t1=[]
    for i in dr:
       for e in i: 
        t1.append(e)
    print(t1)
    t=sum(int(x) for x in t1 )
    u=0
    cur.execute("select whicket from score where team=%s and matchid=%s ",(session.get('l2'),session.get('l1')))
    dg=cur.fetchall()
    u1=[]
    for i in dg:
       for e in i: 
        u1.append(e)
    print(u1)
    u=sum(int(x) for x in u1 )
    cur.execute("select name,trun,tball,point from score where team=%s and matchid=%s ",(session.get('l2'),session.get('l1')))
    da=cur.fetchall()
    cur.execute("select name,run,whicket,over1,point from score where team=%s and (selection='bowler' or selection='allrounder') and matchid=%s ",(session.get('l3'),session.get('l1')))
    da1=cur.fetchall()
    cur.execute("select name,trun,tball,point from score where team=%s and matchid=%s ",(session.get('l3'),session.get('l1')))
    daa=cur.fetchall()
    cur.execute("select name,run,whicket,over1,point from score where team=%s and (selection='bowler' or selection='allrounder') and matchid=%s ",(session.get('l2'),session.get('l1')))
    da2=cur.fetchall()
    con.close()
    return render_template("matchscore1.html",b=b,e=e,t=t,u=u,da=da,daa=daa,da1=da1,da2=da2,user=q3.upper(),hi1=session.get('l2'),hi2=session.get('l3'))


@app.route("/score1")
def score1():
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select name,point from userpoint where name=%s and matchid=%s",(session.get('name'),session.get('l1')))
    gh=cur.fetchall() 
    print(gh)
    con.close()   
    return render_template('score1.html',hi1=session.get('l2'),hi2=session.get('l3'),user=q3.upper(),gh=gh)

@app.route('/user2/<id>')
def user2(id):
    q4=session.get('name')
    q3=q4[0] 
    print(id)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    print(session.get('l1'))
    session['v1id']=id
    cur.execute("select name,point from uservoucher where matchid=%s and vid=%s order by point desc ",(session.get('l1'),id))
    bn=cur.fetchall()
    print(bn)
    con.close()
    return render_template('userpoint1.html',hi1=session.get('l2'),hi2=session.get('l3'),user=q3.upper(),bn=bn)
@app.route('/h1')
def h1():
    return redirect(url_for('user2',id=session.get('v1id')))

@app.route('/winner')
def winner():
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select name from prize where mid=%s and vid=%s",(session.get('l1'),session.get('v1id')))
    bn=cur.fetchall()
    print(bn)
    con.close()
    return render_template('winner.html',bn=bn,hi1=session.get('l2'),hi2=session.get('l3'),user=q3.upper())

@app.route('/myv1')
def myv1():
    global a,v,s
    a=a-len(b)
    b.clear()
    f.clear()
    g.clear()
    print(g)
    h.clear()
    print(h)
    if v==1 and s==1:
        v=v-1
        print(v)
        s=s-1
        print(s)
    q4=session.get('name')
    q3=q4[0] 
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("SELECT * FROM `prize` where name=%s",(q4,))
    bn=cur.fetchall()
    print(bn)
    con.close()
    return render_template('myvoucher.html',bn=bn,user=q3.upper())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
 