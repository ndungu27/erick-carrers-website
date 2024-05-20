from flask import Flask, render_template, jsonify

app=Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Nairobi, Kenya',
    'salary':'Ksh. 150000'
  },
  {
    'id':2,
    'title':'Data Scientiist',
    'location':'Nairobi, Kenya',
    'salary':'Ksh. 250000'
  },
{
  'id':3,
  'title':'Front End Developer',
  'location':'Arusha, Tanzania'
},
  {
    'id':4,
    'title':'back end developer',
    'location':'Remote',
    'salary':'Ksh. 350000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name='Erick')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
  