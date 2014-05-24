import sublime, sublime_plugin, json, codecs

class MegaReplace(sublime_plugin.TextCommand):
	def run(self, edit, replacement_file):
		# open file
		from os.path import join
		file_path = join(sublime.packages_path(), "MegaReplace/" + replacement_file)
		json_data = codecs.open(file_path, 'r', 'UTF-8')
		data = json.load(json_data)

		for item in data:
			replacement = item['replacement']
			find_list = item['finds']
			self.find_and_replace(edit, find_list, replacement)

	def find_and_replace(self, edit, find_list, replace):
		for region in self.view.sel():
			if not region.empty():
				doc = self.view.substr(region)
				for find in find_list:
					doc = doc.replace(find, replace)
				self.view.replace(edit, region, doc)