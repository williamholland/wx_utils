import wx

class BaseFrame(wx.Frame):
    ''' base class for simple guis built on wx frames '''

    # name of the window
    name = None

    # starting status bar
    _status = 'Loading...'

    # space between each element added
    spacing = 5

    width = 350
    height = 200

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
        self.statusbar.SetStatusText(value)

    def init_status_bar(self):
        ''' base function to init the status bar '''
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText(self.status)

    def init_menu_bar(self):
        ''' base function to init the menu bar '''
        self.menuBar = wx.MenuBar()
        self.file_menu = wx.Menu()
        m_exit = self.file_menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, lambda event: self.Close(0), m_exit)
        self.menuBar.Append(self.file_menu, "&File")
        self.SetMenuBar(self.menuBar)

    def add_to_main_panel(self, obj):
        self.main_sizer.Add(obj, wx.EXPAND)
        self.main_sizer.AddSpacer(self.spacing)

    def __init__(self):
        title = self.name if self.name is not None else self.__class__.__name__
        size = (self.width, self.height)
        super(BaseFrame, self).__init__(None, title=title, size=size)

        self.init_menu_bar()
        self.init_status_bar()

        self.main_panel = wx.Panel(self)
        self.root_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.AddStretchSpacer()
        self.root_sizer.AddSpacer(self.spacing)
        self.main_sizer.AddSpacer(self.spacing)

        self.root_sizer.Add(self.main_sizer)
        self.main_panel.SetSizer(self.root_sizer)

        self.init_gui()

        self.status = 'Ready'

        self.Show()

    def init_gui(self):
        ''' override this method to create your Frame '''
        pass
