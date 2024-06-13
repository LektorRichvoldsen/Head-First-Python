Bruke gunicorn:

apt install gunicorn
apt install flask
gunicorn --bind 172.24.8.33:8000 app:app (<-- usikker på dette)
