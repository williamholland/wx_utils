import wx

class MainFrame(wx.Frame):
    def __init__(self, title):
        super(MainFrame, self).__init__(None, title=title, size=(350,200))

if __name__ == "__main__":
    app = wx.App(redirect=True)
    top = MainFrame("Hello World")
    top.Show()
    app.MainLoop()
