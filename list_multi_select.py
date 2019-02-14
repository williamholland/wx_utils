import wx
from base_frame import BaseFrame

class MainFrame(BaseFrame):
    def init_gui(self):
        b = wx.Button(self.main_panel, -1, "test button")
        self.add_to_main_panel(b)

if __name__ == "__main__":
    app = wx.App()
    top = MainFrame("Hello World")
    app.MainLoop()
