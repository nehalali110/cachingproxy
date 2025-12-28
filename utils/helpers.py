from models.args_model import arguments_model
from pydantic import ValidationError, BaseModel
import requests

def validate_arguments(args):
	if not len(args) == 5 or not args[1] == "--port" or not args[3] == "--origin":
		raise ValueError

	arg_obj = arguments_model(port=args[2], remote_url = args[4])
	return arg_obj.port, arg_obj.remote_url


def validate_domain_connectivity(url):
	r = requests.get(url)
	print(r)

temp_url = "https://google.com"
print(validate_domain_connectivity(temp_url))