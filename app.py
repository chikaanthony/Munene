from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id ': 1,
    'title': 'Data Analyst',
    'location': 'NDDC hostels',
    'salary': '$100,000',
  },
  {
    'id ': 2,
    'title': 'front end',
    'location': ' Computing Faculty',
    'salary': '$100,000',
  },
{
  'id ': 3,
  'title': 'Backend Engineer ',
  'location': 'NDDC office',
  'salary': '$100,000',
},
{
  'id ': 4,
  'title': 'food seller',
  'location': 'Agric lecture Theatre ',
  'salary': '$100,000',
},
 ]

@app.route('/')
def hello_world():
  return render_template('home.html',
                         jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
