import sys
#models module is not the path therefore add it
models_path = "/home/nehal/workspace/github/cachingproxy"
sys.path.insert(0,models_path)



from models.args_model import arguments_model
from pydantic import ValidationError, BaseModel
import requests



def validate_arguments(args):
	if not len(args) == 5 or not args[1] == "--port" or not args[3] == "--origin":
		raise ValueError
	arg_obj = arguments_model(port=args[2], remote_url=args[4])
	validate_domain_connectivity(arg_obj.remote_url)
	return arg_obj.port, arg_obj.remote_url


def validate_domain_connectivity(url):
	r = requests.get(url)
	print(r)


def validate_port_connectivity(port):
	localhost = "http://127.0.0.1"
	r = requests.get(f"{localhost}:{port}")
	print(r)

# print(validate_port_connectivity(8000))

# temp_url = "https://invaliddomain.com"
# print(validate_domain_connectivity(temp_url))
# print("helper module running")