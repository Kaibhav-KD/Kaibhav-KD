from flask import Flask, request, redirect, render_template_string


app = Flask(__name__)





@app.route('/')
def home():
    return '''
    <!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Let's Code..</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&family=Open+Sans:wght@400&family=Lobster&family=Montserrat:wght@300&display=swap');
        
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: black;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            background-color: white;
            font-family: 'Roboto', sans-serif;
        }
        .header .title {
            font-size: 28px;
            color: black;
        }
        .header .button {
            background-color: #00008b;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            cursor: pointer;
            border-radius: 5px;
            text-align: center;
            font-family: 'Open Sans', sans-serif;
        }
        .header .button:hover {
            background-color: #0000cd;
        }
        .subheading {
            text-align: left;
            margin-top: 200px;
            font-size: 60px;
            color: white;
            font-family: Times;
        }
        .subheading strong {
            font-weight: bold;
        }
        .mini-subheading {
            font-size: 22px;
            color: white;
            font-family: 'Montserrat', sans-serif;
        }
        .lottie-animation {
            width: 500px;
            height: 500px;
            margin-left: 350px;
            text-align: center;
        }
        .action-button {
            display: inline-block;
            margin-top: 30px;
            padding: 15px 40px;
            background-color: #87CEFA;
            color: black;
            border: none;
            font-size: 18px;
            cursor: pointer;
            border-radius: 5px;
            text-align: center;
            text-decoration: none;
        }
        .action-button:hover {
            background-color: #00BFFF;
        }
        .additional-text {
            margin-top: 20px;
            font-size: 18px;
            color: white;
            font-family: 'Montserrat', sans-serif;
            text-align: left;
        }
        .mini-text {
            text-align: center;
            margin-top: 300px;
            font-size: 30px;
            color: white;
            font-family: 'Montserrat', sans-serif;
        }
        .mini-text strong {
            font-weight: bold;
        }
        .search-box {
            margin-top: 30px;
            margin-bottom: 20px;
            text-align: center;
        }
        .search-box input[type="text"] {
            padding: 12px;
            font-size: 18px;
            width: 350px;
            border: 2px solid #ccc;
            border-radius: 5px;
            font-family: 'Open Sans', sans-serif;
        }
        .search-box input[type="submit"] {
            padding: 12px 25px;
            font-size: 18px;
            background-color: #87CEFA;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-left: 10px;
            font-family: 'Open Sans', sans-serif;
        }
        .search-box input[type="submit"]:hover {
            background-color: #00BFFF;
        }
        
        .section-title {
            text-align: center;
            font-size: 40px;
            color: #87CEFA;
            margin: 40px 0;
            font-family: 'Roboto', sans-serif;
        }
        .card-section {
            display: flex;
            justify-content: space-around;
            padding: 20px;
        }
        .card {
            background-color: #333;
            border-radius: 10px;
            padding: 20px;
            width: 30%;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: 0.3s;
            font-family: 'Montserrat', sans-serif;
        }
        .card:hover {
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        .card h3 {
            color: #87CEFA;
        }
        .card p {
            color: white;
        }
        .footer {
            background-color: #00008b;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .footer a {
            color: #87CEFA;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .contact-section {
            background-color: #444;
            padding: 40px;
            border-radius: 10px;
            margin: 20px auto;
            width: 60%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .contact-section h2 {
            text-align: center;
            color: #87CEFA;
        }
        .contact-section form {
            max-width: 600px;
            margin: 0 auto;
            font-family: 'Open Sans', sans-serif;
        }
        label {
            display: block;
            margin: 10px 0 5px;
            color: white;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            background-color: #87CEFA;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 18px;
        }
        input[type="submit"]:hover {
            background-color: #00BFFF;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.4/lottie.min.js"></script>
</head>
<body>
    <header class="header">
        <div class="title"><strong>Let's Code..</strong></div>
        <button class="button" onclick="window.location.href='/about'">About</button>
    </header>
    
    <div class="subheading">
       <strong>Let's Experience The New World of Coding </strong> 
    </div>
    
    <div class="mini-subheading">
        Simplifying Programming Language Learning For All Levels Of Students.
    </div>
    
    <a href="#" class="action-button" onclick="scrollToSearchBox()">Start Playing With Code...</a>

    <div class="additional-text">
        Easy Learning | Master Skills
    </div>
    
    <div class="mini-text">
       <strong>Choose Your Language.</strong>
    </div>
    
    <div class="search-box">
        <form action="/search" method="get">
            <input type="text" name="q" placeholder="Search Programming Languages..." required>
            <input type="submit" value="Search">
        </form>
    </div>
    
    <div id="lottie-animation" class="lottie-animation"></div>
    
    <div class="programming-logos">
        <img src="https://example.com/logo1.png" alt="Logo 1">
        <img src="https://example.com/logo2.png" alt="Logo 2">
        <img src="https://example.com/logo3.png" alt="Logo 3">
        <img src="https://example.com/logo4.png" alt="Logo 4">
        <img src="https://example.com/logo5.png" alt="Logo 5">
        <img src="https://example.com/logo6.png" alt="Logo 6">
        <img src="https://example.com/logo7.png" alt="Logo 7">
        <img src="https://example.com/logo8.png" alt="Logo 8">
        <img src="https://example.com/logo9.png" alt="Logo 9">
        <img src="https://example.com/logo10.png" alt="Logo 10">
        <img src="https://example.com/logo11.png" alt="Logo 11">
        <img src="https://example.com/logo12.png" alt="Logo 12">
        <img src="https://example.com/logo13.png" alt="Logo 13">
        <img src="https://example.com/logo14.png" alt="Logo 14">
        <img src="https://example.com/logo15.png" alt="Logo 15">
    </div>
    
    
    <!-- Programming Languages Section -->
    <div class="section-title">Programming Languages</div>
    <div class="card-section">
        <div class="card">
            <h3>Python</h3>
            <p>Learn Python, a versatile and beginner-friendly programming language with a wide range of applications.</p>
        </div>
        <div class="card">
            <h3>JavaScript</h3>
            <p>Explore JavaScript, the language of the web, perfect for building interactive and dynamic websites.</p>
        </div>
        <div class="card">
            <h3>Java</h3>
            <p>Master Java, one of the most widely used languages for building scalable and secure applications.</p>
        </div>
    </div>

    <!-- Projects Section -->
    <div class="section-title">Projects</div>
    <div class="card-section">
        <div class="card">
            <h3>Web Development</h3>
            <p>Build dynamic websites using HTML, CSS, and JavaScript.</p>
        </div>
        <div class="card">
            <h3>Data Analysis</h3>
            <p>Analyze large datasets using Python and machine learning algorithms.</p>
        </div>
        <div class="card">
            <h3>Mobile Apps</h3>
            <p>Create mobile applications for Android and iOS using frameworks like React Native or Kotlin.</p>
        </div>
    </div>

    <!-- Blog Section -->
    <div class="section-title">Blog</div>
    <div class="card-section">
        <div class="card">
            <h3>Coding Tips</h3>
            <p>Read about best practices, shortcuts, and useful tips to improve your coding efficiency.</p>
        </div>
        <div class="card">
            <h3>Latest Trends</h3>
            <p>Stay updated on the latest trends and advancements in programming and technology.</p>
        </div>
        <div class="card">
            <h3>Tutorials</h3>
            <p>Follow step-by-step tutorials to learn new coding techniques and build projects.</p>
        </div>
    </div>

    <!-- Contact Section with Animations -->
<div class="contact-section">
    <h2>Contact Us</h2>
    <form action="/contact" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        <input type="submit" value="Send">
    </form>
</div>

    <div class="footer">
        <p>&copy; 2024 Let's Code.. | <a href="/about">About Us</a> | <a href="/contact">Contact Us</a></p>
    </div>
    <script>
        // Load the Lottie animation
        lottie.loadAnimation({
            container: document.getElementById('lottie-animation'),
            renderer: 'svg',
            loop: true,
            autoplay: true,
            path: 'https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json'
        });
    </script>
    <style>
    /* Updated Contact Section Styling */
    .contact-section {
        background-color: #1e1e1e;
        padding: 40px;
        border-radius: 15px;
        margin: 40px auto;
        width: 50%;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease-in-out;
    }
    
    .contact-section:hover {
        transform: scale(1.05);
    }

    .contact-section h2 {
        text-align: center;
        color: #00BFFF;
        font-size: 36px;
        font-family: 'Lobster', sans-serif;
        margin-bottom: 30px;
    }

    .contact-section form {
        max-width: 600px;
        margin: 0 auto;
    }

    label {
        display: block;
        margin: 10px 0;
        color: white;
        font-size: 18px;
    }

    input, textarea {
        width: 100%;
        padding: 12px;
        margin-bottom: 15px;
        border: none;
        border-radius: 10px;
        font-size: 16px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease-in-out;
    }

    input:focus, textarea:focus {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }

    input[type="submit"] {
        background-color: #00BFFF;
        color: white;
        font-size: 20px;
        cursor: pointer;
        padding: 12px;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }

    input[type="submit"]:hover {
        background-color: #1E90FF;
    }
    </style>
</body>
</html>
    '''

@app.route('/about')
def about():
    return '''
    <!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: black;
            color: white;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            background-color: white;
            font-family: 'Roboto', sans-serif;
        }
        .header .title {
            font-size: 28px;
            color: black;
        }
        .footer {
            background-color: #00008b;
            color: white;
            padding: 20px;
            text-align: center;
            font-family: 'Open Sans', sans-serif;
        }
        .footer a {
            color: #87CEFA;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="title"><strong>Let's Code..</strong></div>
        <button class="button" onclick="window.location.href='/'">Home</button>
    </header>
    
    <div class="content">
        <h1>About Us</h1>
        <p>Welcome to Let's Code.., a platform dedicated to making programming learning easy and accessible for everyone. Whether you're a beginner or an experienced coder, we have resources and tools to help you enhance your skills and explore new languages.</p>
    </div>

    <div class="footer">
        <p>&copy; 2024 Let's Code.. | <a href="/">Home</a> | <a href="/contact">Contact Us</a></p>
    </div>
</body>
</html>
    '''

@app.route('/start-coding')
def start_coding():
    return '''
    <!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Start Coding</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: black;
            color: white;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            background-color: white;
            font-family: 'Roboto', sans-serif;
        }
        .header .title {
            font-size: 28px;
            color: black;
        }
        .footer {
            background-color: #00008b;
            color: white;
            padding: 20px;
            text-align: center;
            font-family: 'Open Sans', sans-serif;
        }
        .footer a {
            color: #87CEFA;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="title"><strong>Let's Code..</strong></div>
        <button class="button" onclick="window.location.href='/'">Home</button>
    </header>
    
    <div class="content">
        <h1>Start Coding</h1>
        <p>Get started with our coding resources and tutorials. Dive into interactive lessons and start building your projects.</p>
    </div>

    <div class="footer">
        <p>&copy; 2024 Let's Code.. | <a href="/">Home</a> | <a href="/contact">Contact Us</a></p>
    </div>
</body>
</html>
    '''

@app.route('/search')
def search():
    query = request.args.get('q').strip().lower()
    redirect_url = f"https://overapi.com/{query}#google_vignette"
    return redirect(redirect_url)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
       
        return 'Your message has been sent!'
    
    return '''
    <!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: black;
            color: white;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            background-color: white;
            font-family: 'Roboto', sans-serif;
        }
        .header .title {
            font-size: 28px;
            color: black;
        }
        .footer {
            background-color: #00008b;
            color: white;
            padding: 20px;
            text-align: center;
            font-family: 'Open Sans', sans-serif;
        }
        .footer a {
            color: #87CEFA;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        form {
            max-width: 600px;
            margin: 0 auto;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-family: 'Open Sans', sans-serif;
        }
        input[type="submit"] {
            background-color: #87CEFA;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 18px;
        }
        input[type="submit"]:hover {
            background-color: #00BFFF;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="title"><strong>Let's Code..</strong></div>
        <button class="button" onclick="window.location.href='/'">Home</button>
    </header>
    
    <div class="content">
        <h1>Contact Us</h1>
        <form action="/contact" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" required></textarea>
            <input type="submit" value="Send">
        </form>
    </div>

    <div class="footer">
        <p>&copy; 2024 Let's Code.. | <a href="/">Home</a> | <a href="/about">About Us</a></p>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
