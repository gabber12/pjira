from distutils.core import setup
setup(
  name = 'pjira',
  packages = ['pjira'],
  version = '0.1',
  description = 'A simple Atlassian jira cli client written in python',
  author = 'Shubham Sharma',
  author_email = 'shubham.sha12@gmail.com',
  url = 'https://github.com/gabber12/python-jira',
  download_url = 'https://github.com/gabber12/python-jira/archive/0.3.tar.gz',
  keywords = ['client', 'cli', 'jira'], 
  classifiers = [],
  install_requires=[
        'Click','jira'
  ],
  entry_points='''
        [console_scripts]
        pjira=main:cli
    '''
)