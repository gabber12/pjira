from os.path import expanduser
import os
import json
class ConfigManager(object):
	"Manages Client connection details"
	def __init__(self):
		pass

	@classmethod
	def prepare_config_dir(cls):
		home  = os.path.join(expanduser("~"),  ".jira")
		if not os.path.exists(home):
			os.makedirs(home)
		return home

	@classmethod
	def get_config_file_name(cls):
		home = cls.prepare_config_dir()
		return os.path.join(home, "config.json")

	@classmethod
	def save_details(cls, host, user, password):
		config_file = cls.get_config_file_name();
		details = {'user': user, 'host':host, 'password':password}
		save_json_to_file(details, config_file)

	@classmethod	
	def get_details(cls):
		config_file = cls.get_config_file_name();
		return get_json_from_file(config_file)



def save_json_to_file(json_obj, file):
	with open(file, 'w') as config:
		config.write(json.dumps(json_obj))


def get_json_from_file(file):
	with open(file, 'r') as config:
		return json.loads(config.read())
