from flask import Flask, request, render_template
from otp_quantum import generate_quantum_otp_decimal
import smtplib, os, time
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

EMAIL = os.getenv("EMAIL_ADDRESS")
PASS = os.getenv("EMAIL_PASSWORD")
otp_storage = {}

def send_email(to, code):
    msg = EmailMessage()
    msg.set_content(f"Your OTP: {code}")
    msg["Subject"] = "Your Quantum OTP"
    msg["From"] = EMAIL
    msg["To"] = to
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(EMAIL, PASS)
        s.send_message(msg)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        email = request.form.get("email")
        action = request.form.get("action")
        if action == "send":
            code = generate_quantum_otp_decimal()
            otp_storage[email] = {
                "otp": code,
                "timestamp": time.time(),
                "used": False
            }
            send_email(email, code)
            result = "Quantum OTP sent!"
        elif action == "verify":
            code_input = request.form.get("otp")
            record = otp_storage.get(email)
            try:
                input_int = int(code_input)
            except ValueError:
                input_int = -1                      # 숫자 아닌 입력 방지

            if (record and not record["used"] and
                record["otp"] == input_int and
                time.time() - record["timestamp"] < 120):
                result = "✅ OTP verified!"
                record["used"] = True
            else:
                result = "❌ Invalid or expired OTP"
    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# if __name__ == "__main__":
#     for _ in range(3):
#         print("Quantum OTP:", generate_quantum_otp())
