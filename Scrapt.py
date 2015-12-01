import sublime, sublime_plugin
from time import gmtime, strftime

class ScraptCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
	
		if args['op'] == 'date':
			self.view.insert(edit, self.view.sel()[0].begin(), strftime("%m/%d/%y", gmtime()) + "\n" + strftime("%A", gmtime()) + "\n-------")

