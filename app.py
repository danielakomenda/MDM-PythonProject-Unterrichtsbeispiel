from flask import Flask, render_template, request


app = Flask(__name__)

@app.get('/')
def main_page():
    return web_page('main')

@app.route('/pages/<string:page>')
def web_page(page):
    return render_template(f'{page}.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        # Extract numbers and operation from submitted form
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')
        
        # Perform calculation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
        else:
            result = 'Invalid operation'
        
        # Render the template with the result
        return render_template("calculation.html", result=result, num1=num1, num2=num2)
    else:
        # Initial page load
        return render_template("calculation.html", result=None)



if __name__ == "__main__":
    app.run(port=5000)
    