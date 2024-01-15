from src.services.main_service import MainService
from src.ui.main_ui import MainUI
from src.ui.prints import PrintMessages
from src.gui.main_gui import start_gui

printf=PrintMessages()
service=MainService()
ui=MainUI(printf,service)


# START APP

#ui.run()
start_gui()
