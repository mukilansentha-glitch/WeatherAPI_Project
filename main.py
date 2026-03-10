from flask import Flask,request,render_template
from config import settings
import requests

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def landingpage():
    content={
        "content":"Weather API"
    }
    return render_template("index.html",**content)

@app.route("/fetchapi",methods=["GET","POST"])
def fetchapi():
    a=request.form.get("cityname")
    params={
        "key":settings.API_KEY,"q":a
    }
    content={
        "content":"Fetch API"
    }
    try:
        res=requests.get(f"{settings.url}/current.json",params=params).json()
        timest=requests.get(f"{settings.url}/timezone.json",params=params).json()
        weather=res["current"]["temp_c"]
        forcast=res["current"]["condition"]["text"]
        time=timest["location"]["localtime"].split(" ")[1]
        icon=res["current"]["condition"]["icon"]
        return render_template("resultshow.html",cityname=a,
                    forcast=forcast,icon=icon,degree=weather,time=time,**content)
    except KeyError:
        errmsg="Looking for city is not found or invalid"
        return render_template("error.html",errmsg=errmsg)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=3200, debug=True)
