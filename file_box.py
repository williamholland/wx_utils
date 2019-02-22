import os
import wx
from base_frame import BaseFrame

NoMessage = type('NoMessage', (), {})

class FileBox(wx.Panel):
    ''' 2 ListBoxes connected with buttons to move items between either side.
    
        On init give a list of choices which populate the left box
        Call GetSelection to get the contents of the right box
    '''

    _path = None

    def GetPath(self):
        '''Returns the full path (directory and filename) of the selected file.'''
        return self.filepath

    def SetPath(self, value):
        self.filepath = value

    def _find(self, event):
        with wx.FileDialog(self,
                           message=self.message,
                           defaultDir=self.defaultDir,
                           defaultFile=self.defaultFile,
                           **self.kwargs) as fileDialog:
            if fileDialog.ShowModal() != wx.ID_CANCEL:
                self.filepath = fileDialog.GetPath()

    @property
    def filepath(self):
        '''Returns the full path (directory and filename) of the selected file.'''
        return self.text.GetValue()

    @filepath.setter
    def filepath(self, value):
        self.text.SetValue(value)
        self.text.SetToolTip(wx.ToolTip(self.filepath))

    def __init__(self, parent, label="", message=NoMessage, defaultDir="", defaultFile="", **kwargs):
        super(FileBox, self).__init__(parent)

        if message is NoMessage:
            message = label

        self.message = message
        self.defaultDir = defaultDir
        self.defaultFile = defaultFile
        self.kwargs = kwargs

        box = wx.StaticBox(self, -1, label)
        vsizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer.Add(self.sizer)
        self.sizer.AddSpacer(5)

        self.text = wx.TextCtrl(self, size=(200,-1))
        self.filepath = os.path.join(defaultDir, defaultFile)
        self.text.SetValue(self.filepath)
        self.text.SetToolTip(wx.ToolTip(self.filepath))
        self.sizer.Add(self.text)

        button = wx.Button(self, label='Find', style=wx.BU_EXACTFIT)
        self.sizer.Add(button)
        button.Bind(wx.EVT_BUTTON, self._find)

        self.sizer.AddSpacer(5)
        vsizer.AddSpacer(5)

        self.SetSizerAndFit(vsizer)

class MainFrame(BaseFrame):

    name = 'File Box Test'

    def init_gui(self):
        self.box = FileBox(
            self.main_panel,
            label='File box test'
        )
        self.box.SetPath(os.path.realpath(__file__))
        self.add_to_main_panel(self.box)

if __name__ == "__main__":
    app = wx.App()
    top = MainFrame()
    app.MainLoop()
