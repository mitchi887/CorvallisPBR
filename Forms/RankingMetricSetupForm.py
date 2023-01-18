import npyscreen as nps
from Forms.KeyShortcuts import registerFkeys
from Forms.FormText import *
from Forms.FormUtilities import *

class RankingMetricSetupForm(nps.ActionForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# registering the function keys for use
		registerFkeys(self)

	def create(self):
		self.placeholder = self.add(nps.FixedText, name=None,
									value='Ranking Metric Setup Form', editable=False)

	def on_ok(self):
		return

	def on_cancel(self):
		# otherwise go back to the previous form (splash screen)
		self.hndlBack()

	def hndlHelp(self, *args, **kwargs):
		# opening help menu in a notify window
		nps.notify_confirm('\n'.join(helpAsciiList), title='Help')

	def hndlOk(self, *args, **kwargs):
		# calling the ok handler
		self.on_ok()

	def hndlBack(self, *args, **kwargs):
		# back from this form takes us back to the splash screen
		# if they want to leave the form then notify the user their edits will be unsaved
		result = nps.notify_yes_no(
			'Return to the main screen? Unsaved Work will be lost.')

		# if yes, we switch back to the main form (splash screen)
		if result:
			self.parentApp.switchForm(FM_MAIN)

	def hndlQuit(self, *args, **kwargs):
		# notifying the user that they will exit and form edits will not be saved.
		result = nps.notify_yes_no(
			'Are you sure you want to close the application? Unsaved work will be lost.',
			title='Exit')

		# if the result is okay then we exit the application, otherwise, we stay where we are/do nothing
		if result:
			self.parentApp.switchForm(None)
