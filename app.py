from flask import Flask,render_template,url_for,request
app=Flask(__name__)
books = [
    {
        'author': 'George RR Martin',
        'location':'T.Nagar, Chennai',
        'title':'A song of ice and fire ',
        'price': '500',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'JK Rowling',
        'location':'Mambalam, Chennai',
        'title': 'Harry potter',
        'price': '300',
        'date_posted': 'April 21, 2018',
        
    }
]
movies=[
    {
        'name':'Avengers',
        'cast':'Robert downey jr, Chris Evans',
        'price':'150',
        'Show':'5:00 pm, april 26th',
        'theatre':'Sathyam Cinemas, Chennai'
    },
    {
        
        'name':'Spider-Man',
        'cast':'Tom Holland',
        'price':'150',
        'Show':'7:30 pm, april 26th',
        'theatre':'Devi cinemas, Chennai'
    
    }
]
mobiles=[
    {
        'name':'iPhone 11',
        'size':' 4gb, 128gb',
        'usage':'6 months old',
        'location':'kk nagar, chennai',
        'price':'50,000'
    },
    {
        'name':'redmi note 7',
        'size':' 4gb, 64gb',
        'usage':'6 months old',
        'location':'anna nagar, chennai',
        'price':'10,000'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')
@app.route("/events")
def event():
    return render_template('events.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/books")
def book():
    return render_template('books.html',books=books)
@app.route("/movies")
def movie():
    return render_template('movies.html',movies=movies)
@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return variable
@app.route("/mobiles")
def mobile():
    return render_template('mobiles.html',mobiles=mobiles)
if __name__=='__main__':
    app.run(debug=True)