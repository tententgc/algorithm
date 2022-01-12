import os
import github
import base64

detail = '''# tenten's Leetcode Collection

'''
head = '<table><tr><td>File Type</td><td>Number</td></tr>'
tail = '</table>'
data = dict()
sumFile = 0


class GithubController:
	def __init__(self, ACCESS_TOKEN):
		g = github.Github(ACCESS_TOKEN)
		self.repo = g.get_repo('tententgc/LeetCodeSolution')
		self.PATH = '/README.md'

	def get_data(self):
		contents = self.repo.get_contents(self.PATH, 'main')
		self.PATH = contents.path
		self.SHA = contents.sha
		base = contents.content
		base = base.replace('\n', '')
		self.file_content = base64.b64decode(base).decode('utf-8')

	def write_data(self, content):
		if content != self.file_content:
			self.repo.update_file(
				self.PATH, 'action: Update File Count :zap:', content, self.SHA)


def createRow(fileType, number):
	return '<tr><td>'+str(fileType)+'</td><td>'+str(number)+'</td></tr>'


def countFile():
	global data
	global sumFile
	for dirname, _, filenames in os.walk('.'):
		if(dirname == '.'):
			for i in filenames:
				i = i.split('.')
				if len(i) > 1:
					i = i[1]
					if i != 'md':
						sumFile += 1
						if i in data:
							data[i] += 1
						else:
							data[i] = 1
		else:
			pass


def modifyData():
	global data
	global sumFile
	if data['py']:
		data['py'] -= 1
		sumFile -= 1
	output = detail+head
	for i in data.keys():
		output += createRow(i, data[i])
	output += '<tr><td>Sum</td><td>'+str(sumFile)+'</td></tr>'
	output += tail
	return output


def main():
	countFile()
	ACCESS_TOKEN = os.getenv('TOKEN')
	controller = GithubController(ACCESS_TOKEN)
	controller.get_data()
	content = modifyData()
	controller.write_data(content)


if __name__ == '__main__':
    main()
