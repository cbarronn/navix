from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Configuración del correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'  # Reemplazar con correo real
app.config['MAIL_PASSWORD'] = 'tu_contraseña'      # Reemplazar con contraseña real

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        msg = Message('Nuevo mensaje de contacto',
                     sender=email,
                     recipients=['tu_correo@gmail.com'])
        msg.body = f"Nombre: {name}\nEmail: {email}\nMensaje: {message}"
        mail.send(msg)
        
        return render_template('index.html', success=True)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
