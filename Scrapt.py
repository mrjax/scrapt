import sublime, sublime_plugin
from time import gmtime, strftime
from datetime import date, timedelta

class ScraptCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
	
		today = date.today()


		if args['op'] == 'date':
			s = self.view.sel()[0]
			start = s.begin()
			
			while(start > 0 and self.view.substr(start - 1) != '\n'):
				start -= 1

			line = self.view.substr(sublime.Region(start,s.begin()))

			if(line == ""):
				self.view.insert(edit, self.view.sel()[0].begin(), strftime("%m/%d/%y", today.timetuple()) + "\n" + strftime("%A", today.timetuple()) + "\n-------\n\n")

			elif (line.split(" ")[0].isdigit()):
				day = today - timedelta(int(line.split(" ")[0]))

				self.view.insert(edit, s.begin(), strftime("%m/%d/%y", day.timetuple()) + "\n" + strftime("%A", day.timetuple()) + "\n-------\n\n")
				self.view.erase(edit, sublime.Region(start,s.begin()))
			else:
				print "inside else"