from utils import InvalidConfiguration
if __name__ == '__main__':
	try:
		cli()
	except InvalidConfiguration, e:
		print "Error: " + str(e)
		print "To reconfigure client run - \n'jira configure'"
		print cli.get_help(click.Context(cli))