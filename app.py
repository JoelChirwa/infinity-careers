from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {'id': 1, 
     'title': "Software Engineer", 
     'location': "London", 
     'salary': "Mwk. 2,900,000",
    },

    {'id': 2, 
     'title': "Data Scientist", 
     'location': "Mzuzu", 
     'salary': "Mwk. 1,500,000",
    },

    {'id': 3, 
     'title': "Product Manager", 
     'location': "Blantyre", 
     'salary': "Mwk. 1,300,000",
    },

    {'id': 4, 
     'title': "Farm Manager",
     'location': "Kasungu",
     'salary': "Mwk. 1,100,000",
    },

    {'id': 5, 
     'title': "Mathematics Teacher",
     'location': "Zomba",
     'salary': "Mwk. 1,000,000",
    },

    {'id': 6,
     'title': "Virtual Assistant",
     'location': "Remote"
    }
]

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
    