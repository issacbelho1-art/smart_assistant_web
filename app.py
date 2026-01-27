from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        choice = request.form.get("choice")

        if choice == "emi":
            monthly = int(request.form.get("monthly"))
            result = f"Your yearly EMI is {monthly * 12}"

        elif choice == "loan":
            loan = int(request.form.get("loan"))
            if loan > 1000000:
                result = "High debt, skill upgrade needed"
            else:
                result = "Debt manageable"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
