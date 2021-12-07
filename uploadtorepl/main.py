from flask import Flask, send_file
import hashlib

rooms = 'rooms/'
users = 'users/'



app = Flask(__name__, static_folder='rooms')


@app.route('/', methods = ['GET', 'POST'])
def Index():
 return "ello"

@app.route('/wchat/<string:room>/<string:message>/<string:username>/<string:pw>/<string:join>')
def chat(room, message, username, pw, join):
  
  hashpass = hashlib.sha512(username.encode())
  hasheduser = hashpass.hexdigest()
  with open(f'{users}user.txt') as f:
    if hasheduser in f.read():
      hashpass = hashlib.sha512(pw.encode())
      hashedpass = hashpass.hexdigest()
      check = f"{hasheduser}:{hashedpass}"
      with open(f'{users}user.txt') as f:
        if check in f.read():
          if len(message) > 100:
            return "your message was longer then 100 characters"
          else:
            if len(join) > 2:
              f = open(f"{rooms}{room}.txt", "w")
              f.write(f"{username} joined the chat\n")
              f.close()
            else:
             f = open(f"{rooms}{room}.txt", "w")
             f.write(f"{username}: {message}\n")
             f.close()
        else:
          return "wrong password"  
    else:
      return "username not registered"


@app.route('/register/<string:username>/<string:pw>')
def register(username, pw):
  hashpass = hashlib.sha512(username.encode())
  hasheduser = hashpass.hexdigest()
  with open(f'{users}user.txt') as f:
    if hasheduser in f.read():
      return "Username already registerd"
    else:
      hashpass = hashlib.sha512(pw.encode())
      hashedpass = hashpass.hexdigest()
      f = open(f"{users}user.txt", "a")
      f.write(f"{hasheduser}:{hashedpass}\n")
      f.close()     
      return "account registerd"








  

@app.route('/rchat/<string:room>')
def rchat(room):
  return send_file(f"{rooms}{room}.txt")


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=8000)