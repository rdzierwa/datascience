import fruit
import math
from time import sleep # poleca się importować te funkcje które korzystamy
#os.system('ls')
#print(os.listdir())
#print(str(math.pi))
#print("Hello")
#sleep(2)
#print("Bye Bye")

#print(math.sin(math.radians(90)))
#ruit.lemon(2)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
