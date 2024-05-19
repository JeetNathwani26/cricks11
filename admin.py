from flask import Flask, render_template, request,flash,redirect,session,url_for
import mysql.connector

app = Flask(__name__)
app.secret_key="login form"



@app.route("/")
def l():
  return render_template("admin.html")


@app.route("/admin",methods=["POST"])
def admin():
    t1=request.form.get('username')
    t2=request.form.get('password')
    session["admin"]=t1
    if t1=='Admin' and t2=='ab123':
        return redirect(url_for("admin_home"))        
    else:
        flash("enter all detail.....")
        return redirect(url_for('admin_back'))

@app.route("/admin_back")
def admin_back():
    return render_template("admin.html")

@app.route("/admin_home")
def admin_home():
    return render_template("admin_home.html",user=session.get('admin'))
#show team..
@app.route("/admin_team")
def admin_team():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from team ")
    db=cur.fetchall()
    con.close()
    return render_template("admin_team.html",data=db)


# delete team..
@app.route("/delete/<id>",methods=['GET'])
def de(id):
    print(id)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("delete from team where team=%s",(id,))
    flash("Data is deleted...")
    con.commit()
    return redirect(url_for('admin_team'))
    



#team data ..
@app.route("/insert",methods=['POST'])
def insert():
    t3=request.form.get('id')
    t4=request.form.get('team')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("SELECT * FROM `team` WHERE id=%s",(t3,))
    fg=cur.fetchall()
    gf=cur.rowcount
    if gf==1:
        flash('Team is alerady exist..')
        return redirect(url_for('admin_team'))
    else:
      cur.execute("INSERT INTO `team` VALUES (%s,%s)",(t3,t4))
      con.commit()
      flash("Team data added successfully..")
      return redirect(url_for('admin_team'))

    
#update team..
@app.route("/edit1/<i1>",methods=['post'])
def edit1(i1):
    
    t4=request.form.get('team')

    
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("""update team set team=%swhere id=%s""",(t4,i1))
    db=cur.fetchone()
    flash("Data is updated")
    print(db)
    con.commit() 
    return redirect(url_for('admin_team',id=session.get('id')))  

#team search..
@app.route("/search1",methods=['POST'])
def search1():
    t1=request.form.get('v1')
    print(t1)
    print(session.get('teamid'))
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from team where id=%s",(t1,))
    db=cur.fetchall()
    count=cur.rowcount
    print()
    cur.close()
    print(db)
    if count==1:
        return render_template("admin_team.html",data=db)
    else:
      flash("Data does not found..")
      return redirect(url_for('admin_team')) 

    

#plyer show 
@app.route("/admin_player/<team>",methods=['GET'])
def admin_player(team):
    session['team']=team
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from player where tame=%s",(team,))
    se=cur.fetchall()
    cur.close()
    return render_template("player.html",sw=se) 

#player delete..


@app.route("/deletep/<id>",methods=['GET'])
def dep(id):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    print(id)
    cur=con.cursor()
    cur.execute("DELETE FROM `player` WHERE playerid=%s",(id,))
    flash("Data is deleted...")
    cur.close()
    con.commit()
    return redirect(url_for('admin_player',team=session.get('team')))


#player add
@app.route("/add",methods=['POST'])
def add():
    t1=request.form.get('playerid')
    t2=request.form.get('playername')
    t3=request.form.get('team')
    t4=request.form.get('picture')
    t5=request.form.get('selection')
    print(t5)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("SELECT * FROM `player` WHERE playerid=%s",(t1,))
    fg=cur.fetchall()
    gf=cur.rowcount
    print(gf)
    print(fg)
    if gf==1:
        flash("Player is already have..")
        return redirect(url_for('admin_player',team=session.get('team')))
    else:           
        if(t1==""):
            flash("Plase enter playerid..")
            return redirect(url_for('admin_player',team=session.get('team')))
        else: 
            cur.execute("insert into player values(%s,%s,%s,%s,%s)",(t1,t2,t4,t5,t3))
            con.commit()
            flash("Player  data is added successfully..")
            return redirect(url_for('admin_player',team=session.get('team')))
    
@app.route("/search",methods=['POST'])
def search():
    t1=request.form.get('v1')
    print(t1)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from player where name=%s and tame=%s",(t1,session.get('team')))
    db=cur.fetchall()
    count=cur.rowcount
    print(db)
    if count==1:
        return render_template('player.html',sw=db)
    else:
      flash("Data does not found..")
      return redirect(url_for('admin_player',id=session.get('id'))) 
    
     
    

@app.route("/edit/<i1>",methods=['post'])
def edit(i1):
    #t1=request.form.get('playerid')
    t2=request.form.get('playername')
    #t3=request.form.get('id')
    t4=request.form.get('picture')
    t5=request.form.get('selection')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("""update player set name=%s,picture=%s,selection=%s where playerid=%s""",(t2,t4,t5,i1))
    db=cur.fetchone()
    flash("Data is updated")
    print(db)
    con.commit() 
    return redirect(url_for('admin_player',team=session.get('team')))     


#match 
@app.route("/match")
def match():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from team ")
    db=cur.fetchall()
    cur.execute("select * from match1")
    dd=cur.fetchall()
    print(dd)
    con.commit
    return render_template('admin_match.html',d2=db,data=dd)

#match add
@app.route("/matchinfo",methods=['POST'])
def matchinfo():
    t1=request.form.get('id')
    t2=request.form.get('team1')
    t3=request.form.get('picture1')
    t4=request.form.get('team2')
    t5=request.form.get('picture2')
    t6=request.form.get('league')
    t7=request.form.get('d1')
    t8=request.form.get('venue')
    t9=request.form.get('selection')
    
    print(t1,t2,t3,t4,t5,t6,t7,t8,t9)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    if(t1==""):
       flash("Plase enter teamid..")
       return redirect(url_for('match'))
    else: 
        cur.execute("insert into match1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(t1,t2,t3,t4,t5,t6,t7,t8,t9))
        con.commit()
        flash("Match info is inserted..")
        return redirect(url_for('match'))
    
@app.route("/delete1/<id1>",methods=['GET'])
def de1(id1):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("delete from match1 where  id=%s",(id1,))
    flash("Data is deleted...")
    cur.close()
    con.commit()
    return redirect(url_for('match'))  

@app.route("/edit2/<i1>",methods=['post'])
def edit2(i1):
    t2=request.form.get('team1')
    t3=request.form.get('team2')
    t4=request.form.get('league')
    t5=request.form.get('d1')
    t6=request.form.get('selection')
    t7=request.form.get('venue')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("""update match1 set team1=%s,team2=%s,leaguge=%s,date1=%s,updates=%s,vanue=%s where id=%s""",(t2,t3,t4,t5,t6,t7,i1))
    db=cur.fetchone()
    flash("Data is updated")
    print(db)
    con.commit() 
    return redirect(url_for('match'))   

@app.route("/search2",methods=['POST'])
def search2():
    t1=request.form.get('v1')
    print(t1)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from team ")
    dd=cur.fetchall()
    print(dd)
    cur.execute("select * from match1 where date1=%s",(t1,))
    db=cur.fetchall()
    print(db)
    if db:
        return render_template('admin_match.html',d2=dd,data=db)
    else:
      flash("Data does not found..")
      return redirect(url_for('match'))  

#vouchers
@app.route("/vouchers")
def vouchers():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from vouchers ")
    db=cur.fetchall()
    con.commit
    return render_template('contest.html',data=db) 

@app.route("/vadd",methods=['POST'])
def vadd():
    t1=request.form.get('id')
    t2=request.form.get('v1')
    t3=request.form.get('s1')
    t4=request.form.get('w1')
    t5=request.form.get('m1')
    t6=request.form.get('c1')
    t7=request.form.get('picture')
    
    print(t1,t2,t3,t4,t5,t6,t7)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    if(t1==""):
       flash("Plase enter voucher..")
       return redirect(url_for('vouchers'))
    else: 
        cur.execute("select * from vouchers where vid=%s",(t1,))
        db=cur.fetchall() 
        if db:
            flash('Vouchers is already have..')
            return redirect(url_for('vouchers')) 
        else:
           cur.execute("insert into vouchers values(%s,%s,%s,%s,%s,%s,%s)",(t1,t2,t3,t4,t5,t6,t7))
           con.commit()
           flash("Vouchers data add successfully..")
           return redirect(url_for('vouchers')) 

@app.route("/search3",methods=['POST'])
def search3():
    t1=request.form.get('v1')
    print(t1)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from team ")
    dd=cur.fetchall()
    print(dd)
    cur.execute("select * from vouchers where vid=%s",(t1,))
    db=cur.fetchall()
    print(db)
    if db:
        return render_template('contest.html',d2=dd,data=db)
    else:
      flash("Data does not found..")
      return redirect(url_for('vouchers'))

@app.route("/del1/<id1>",methods=['GET'])
def d1(id1):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("delete from vouchers where  vid=%s",(id1,))
    flash("Data is deleted...")
    cur.close()
    con.commit()
    return redirect(url_for('vouchers')) 


#adverties...
@app.route("/adver")
def adver():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from adverties")
    dv=cur.fetchall()
    cur.close()
    con.commit()
    return render_template('adverties.html',data=dv)
@app.route("/inser6",methods=['POST'])
def inser6():
    t1=request.form.get('id')
    t2=request.form.get('picture')
    
    print(t1,t2)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute('select * from adverties where id=%s',(t1,))
    gh=cur.fetchall()
    if gh:
        flash("Data is already have..")
        return redirect(url_for('adver'))
    else:
       if(t1==""):
          flash("Plase enter detail..")
          return redirect(url_for('adver'))
       else: 
          cur.execute("INSERT INTO `adverties`(`id`, `picture`) VALUES (%s,%s)",(t1,t2))
          con.commit()
          flash("Adverties  is insert..")
          return redirect(url_for('adver'))

@app.route("/del6/<id1>",methods=['GET'])
def del6(id1):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("delete from adverties where  id=%s",(id1,))
    flash("Data is deleted...")
    cur.close()
    con.commit()
    return redirect(url_for('adver')) 

#score...



@app.route("/score/<i1>/<i2>/<i3>")
def score(i1,i2,i3):
    session['i1']=i1
    session['i2']=i2
    session['i3']=i3
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    #frist inning batsmaan
    cur.execute("select * from player where tame=%s and (selection='batsman' or selection='wicketkeeper')",(i2,))
    db=cur.fetchall()
    cur.execute("select name,one,two,three,four,six,trun,tball from score where team=%s and selection=%s and matchid=%s",(i2,'batsman',session.get('i1')))
    dd=cur.fetchall()
    #frist inning allrounder
    cur.execute("select * from player where tame=%s and selection='allrounder'",(i2,))
    dc1=cur.fetchall()
    cur.execute("select name,one,two,three,four,six,trun,whitball,noball,run,whicket,over1,tball from score where team=%s and selection=%s and matchid=%s",(i2,'allrounder',session.get('i1')))
    df=cur.fetchall()
    #frist inning bowler
    cur.execute("select * from player where tame=%s and selection = 'bowler'",(i2,))
    dc=cur.fetchall()   
    cur.execute("select name,one,two,three,four,six,trun,whitball,noball,run,whicket,over1,tball from score where team=%s and selection=%s and matchid=%s",(i2,'bowler',session.get('i1')))
    ff=cur.fetchall() 
    #second inning batsmaan
    cur.execute("select * from player where tame=%s and (selection='batsman' or selection='wicketkeeper')",(i3,))
    cc=cur.fetchall()
    cur.execute("select name,one,two,three,four,six,trun,tball from score where team=%s and selection=%s and matchid=%s",(i3,'batsman',session.get('i1')))
    dv=cur.fetchall()
    #seond inning allrounder
    cur.execute("select * from player where tame=%s and selection='allrounder'",(i3,))
    dt=cur.fetchall()
    cur.execute("select name,one,two,three,four,six,trun,whitball,noball,run,whicket,over1,tball from score where team=%s and selection=%s and matchid=%s",(i3,'allrounder',session.get('i1')))
    dt1=cur.fetchall()
    #seond inning bowler
    cur.execute("select * from player where tame=%s and selection = 'bowler'",(i3,))
    tt=cur.fetchall() 
    cur.execute("select name,one,two,three,four,six,trun,whitball,noball,run,whicket,over1,tball from score where team=%s and selection=%s and matchid=%s",(i3,'bowler',session.get('i1')))
    jj=cur.fetchall()
    cur.close()
    return render_template('score.html',i1=i1,i2=i2,i3=i3,db1=db,dd=dd,dc1=dc1,df=df,dc=dc,ff=ff,cc=cc,dv=dv,tt=tt,jj=jj,dt=dt,dt1=dt1)

@app.route("/run1",methods=['POST'])
def run1():
    t5=request.form.get('i1')
    a=1*int(t5)
    print(a)
    t1=request.form.get('i2')
    b=2*int(t1)
    print(b)
    t2=request.form.get('i3')
    c=3*int(t2)
    print(c)
    t3=request.form.get('i4')
    d=4*int(t3)
    print(d)
    t4=request.form.get('i5')
    e=6*int(t4)
    t5=request.form.get('i6')
    print(e)  
    t0=request.form.get('i0')
    f=a+b+c+d+e
    print(f)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("insert into score (name,matchid,selection,team,one,two,three,four,six,trun,point,tball,whitball,noball,run,whicket,over1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(t0,session.get('i1'),'batsman',session.get('i2'),a,b,c,d,e,f,'0',t5,'0','0','0','0','0'))
    db=cur.fetchall()
    cur.close()
    con.commit()
    return redirect(url_for('score',i1=session.get('i1'),i2=session.get('i2'),i3=session.get('i3')))
@app.route("/run3",methods=['POST'])
def run3():
    t5=request.form.get('i1')
    a=1*int(t5)
    print(a)
    t1=request.form.get('i2')
    b=2*int(t1)
    print(b)
    t2=request.form.get('i3')
    c=3*int(t2)
    print(c)
    t3=request.form.get('i4')
    d=4*int(t3)
    print(d)
    t4=request.form.get('i5')
    e=6*int(t4)
    print(e)  
    t0=request.form.get('i0')
    f=a+b+c+d+e
    t6=request.form.get('i6')
    t7=request.form.get('i7')
    t8=request.form.get('i8')
    t9=request.form.get('i9')
    t10=request.form.get('i10')
    t11=request.form.get('i11')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("INSERT INTO `score`(`name`, `selection`, `matchid`, `team`, `one`, `two`, `three`, `four`, `six`, `trun`, `tball`, `whitball`, `noball`, `run`, `whicket`, `over1`, `point`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(t0,'allrounder',session.get('i1'),session.get('i2'),a,b,c,d,e,f,t11,t6,t7,t8,t9,t10,'0'))
    db=cur.fetchall()
    cur.close()
    con.commit()
    return redirect(url_for('score',i1=session.get('i1'),i2=session.get('i2'),i3=session.get('i3')))
@app.route("/run2",methods=['POST'])
def run2():
    t5=request.form.get('i1')
    a=1*int(t5)
    print(a)
    t1=request.form.get('i2')
    b=2*int(t1)
    print(b)
    t2=request.form.get('i3')
    c=3*int(t2)
    print(c)
    t3=request.form.get('i4')
    d=4*int(t3)
    print(d)
    t4=request.form.get('i5')
    e=6*int(t4)
    print(e)  
    t0=request.form.get('i0')
    f=a+b+c+d+e
    t6=request.form.get('i6')
    t7=request.form.get('i7')
    t8=request.form.get('i8')
    t9=request.form.get('i9')
    t10=request.form.get('i10')
    t11=request.form.get('i11')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("INSERT INTO `score`(`name`, `selection`, `matchid`, `team`, `one`, `two`, `three`, `four`, `six`, `trun`, `tball`, `whitball`, `noball`, `run`, `whicket`, `over1`, `point`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(t0,'bowler',session.get('i1'),session.get('i2'),a,b,c,d,e,f,t11,t6,t7,t8,t9,t10,'0'))
    db=cur.fetchall()
    cur.close()
    con.commit()
    return redirect(url_for('score',i1=session.get('i1'),i2=session.get('i2'),i3=session.get('i3')))

@app.route("/srun3",methods=['POST'])
def srun3():
    t5=request.form.get('i1')
    a=1*int(t5)
    print(a)
    t1=request.form.get('i2')
    b=2*int(t1)
    print(b)
    t2=request.form.get('i3')
    c=3*int(t2)
    print(c)
    t3=request.form.get('i4')
    d=4*int(t3)
    print(d)
    t4=request.form.get('i5')
    e=6*int(t4)
    print(e)  
    t5=request.form.get('i6')
    t0=request.form.get('i0')
    f=a+b+c+d+e
    print(f)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("insert into score (name,matchid,selection,team,one,two,three,four,six,trun,point,tball,whitball,noball,run,whicket,over1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(t0,session.get('i1'),'batsman',session.get('i3'),a,b,c,d,e,f,'0',t5,'0','0','0','0','0'))
    db=cur.fetchall()
    cur.close()
    con.commit()
    return redirect(url_for('score',i1=session.get('i1'),i2=session.get('i2'),i3=session.get('i3')))

@app.route("/srun2",methods=['POST'])
def srun2():
    t5=request.form.get('i1')
    a=1*int(t5)
    print(a)
    t1=request.form.get('i2')
    b=2*int(t1)
    print(b)
    t2=request.form.get('i3')
    c=3*int(t2)
    print(c)
    t3=request.form.get('i4')
    d=4*int(t3)
    print(d)
    t4=request.form.get('i5')
    e=6*int(t4)
    print(e)  
    t0=request.form.get('i0')
    f=a+b+c+d+e
    t6=request.form.get('i6')
    t7=request.form.get('i7')
    t8=request.form.get('i8')
    t9=request.form.get('i9')
    t10=request.form.get('i10')
    t11=request.form.get('i11')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("INSERT INTO `score`(`name`, `selection`, `matchid`, `team`, `one`, `two`, `three`, `four`, `six`, `trun`, `tball`, `whitball`, `noball`, `run`, `whicket`, `over1`, `point`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(t0,'allrounder',session.get('i1'),session.get('i3'),a,b,c,d,e,f,t11,t6,t7,t8,t9,t10,'0'))
    db=cur.fetchall()
    cur.close()
    con.commit()
    return redirect(url_for('score',i1=session.get('i1'),i2=session.get('i2'),i3=session.get('i3')))

@app.route("/srun4",methods=['POST'])
def srun4():
    t5=request.form.get('i1')
    a=1*int(t5)
    print(a)
    t1=request.form.get('i2')
    b=2*int(t1)
    print(b)
    t2=request.form.get('i3')
    c=3*int(t2)
    print(c)
    t3=request.form.get('i4')
    d=4*int(t3)
    print(d)
    t4=request.form.get('i5')
    e=6*int(t4)
    print(e)  
    t0=request.form.get('i0')
    f=a+b+c+d+e
    t6=request.form.get('i6')
    t7=request.form.get('i7')
    t8=request.form.get('i8')
    t9=request.form.get('i9')
    t10=request.form.get('i10')
    t11=request.form.get('i11')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("INSERT INTO `score`(`name`, `selection`, `matchid`, `team`, `one`, `two`, `three`, `four`, `six`, `trun`, `tball`, `whitball`, `noball`, `run`, `whicket`, `over1`, `point`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(t0,'bowler',session.get('i1'),session.get('i3'),a,b,c,d,e,f,t11,t6,t7,t8,t9,t10,'0'))
    db=cur.fetchall()
    cur.close()
    con.commit()
    return redirect(url_for('score',i1=session.get('i1'),i2=session.get('i2'),i3=session.get('i3')))

@app.route("/point")
def point():
    i1=session.get('i1')
    i2=session.get('i2')
    i3=session.get('i3')
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from player where tame=%s",(i2,))
    db=cur.fetchall()
    cur.execute("select name,trun,whicket,point from score where team=%s and matchid=%s",(i2,session.get('i1')))
    dd=cur.fetchall() 
    cur.execute("select * from player where tame=%s",(i3,))
    cc=cur.fetchall()
    cur.execute("select name,trun,whicket,point from score where team=%s and matchid=%s",(i3,session.get('i1')))
    dv=cur.fetchall()

    cur.close()
    return render_template('point.html',i1=session.get('i1'),i2=session.get('i2'),i3=session.get('i3'),db1=db,dd=dd,cc=cc,dv=dv)

@app.route("/update",methods=['POST'])
def update():
    t0=request.form.get('i0')
    t1=request.form.get('i1')
    print(t0,t1)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("UPDATE score SET point = %s WHERE name=%s and matchid=%s",(t1,t0,session.get('i1')))
    db=cur.fetchall()
    con.commit()
    con.close()
    return redirect('point')

@app.route("/contest1")
def contest1():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from vouchers where id=%s",(session.get('i1'),))
    db=cur.fetchall()
    con.close()
    return render_template('usercontest.html',db=db)

@app.route("/user/<id>")
def user(id):
    session['b1']=id
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select * from uservoucher where matchid=%s and vid=%s order by point desc ",(session.get('i1'),id))
    db=cur.fetchall()
    con.close()
    return render_template('user.html',db=db)

@app.route("/getscore/<id>")
def getscore(id):
    b=0
    print(id)
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    print(session.get('i1'))
    cur=con.cursor()
    cur.execute("select  player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11 from userteam where   name=%s and matchid=%s",(id,session.get('i1')))
    data=cur.fetchall()
    v=[]
    for h in data:
       for j in h: 
          v.append(j)
    print(v)    
    cur.execute("select point from score where matchid=%s and (name=%s or name=%s or name=%s or name=%sor name=%sor name=%sor name=%sor name=%sor name=%sor name=%sor name=%s)",(session.get('i1'),v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10]))
    dc=cur.fetchall() 
    print(dc)
    a=[]
    for i in dc:
       for e in i:
          a.append(e)
    b=sum(int(x) for x in a ) 
    print(a)  
    print(b)   
    cur.execute("update uservoucher set point=%s where name=%s and matchid=%s",(b,id,session.get('i1'),))
    con.commit() 
    return redirect(url_for("user",id=session.get('b1')))

@app.route("/give/<vid>/<name>")
def give(vid,name):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jeet@123",
        database="tybca29"
    )
    cur=con.cursor()
    cur.execute("select voucher,img,code,vid,id from vouchers where id=%s and vid=%s ",(session.get('i1'),vid))
    db=cur.fetchall()
    v=[]
    for i in db:
        for h in i:
            v.append(h)
    cur.execute("INSERT INTO `prize` VALUES (%s,%s,%s,%s,%s,%s)",(name,v[0],v[1],v[2],v[3],v[4]))
    dc=cur.fetchall()
    con.commit()
    con.close()
    flash("Prize wiil be sent..")
    return redirect(url_for("user",id=session.get('b1')))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)