'''
The `server-config.ini` file is being opened in read mode in the Python code provided.
The code reads the contents of this configuration file using the `configparser` module
in Python. The configuration file is parsed to extract the sections and items within
those sections, and the information is stored in a dictionary named `output_dict`. 
The code then prints the configuration details and the resulting JSON file containing the
parsed configuration information. 

'''
import configparser
from flask import Flask
app = Flask(__name__)

fileName = "server-config.ini"
config_object = configparser.ConfigParser()

try:
    file = open(fileName,"r")
except FileNotFoundError:
    raise FileNotFoundError(f"No such file : {fileName} exists")

config_object.read_file(file)
output_dict = dict()
sections = config_object.sections()
print("Configuration File Parser Results :")
for section in sections:
    items = config_object.items(section)
    print(f"{section}: ")
    for item,value in items:
        print(f"- {item} : {value}")
    output_dict[section] = dict(items)

print(f" Json file :  {output_dict}")

# GET API to fetch the config information
@app.route("/getConfigInfo", methods=['GET'])
def getAllTasks():
    return output_dict


if __name__== '__main__':
    app.run(debug=True)

