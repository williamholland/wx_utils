import wx
from base_frame import BaseFrame

class DoubleListBox(wx.Panel):
    ''' 2 ListBoxes connected with buttons to move items between either side.
    
        On init give a list of choices which populate the left box
        Call GetSelection to get the contents of the right box
    '''

    def GetSelections(self):
        '''Fill an array of ints with the positions of the currently selected items.'''
        return self.l2.GetItems()

    def _all_right(self, event):
        items = self.l1.GetItems()
        for item in items:
            self.l2.Append(item)
        self.l1.Clear()

    def _all_left(self, event):
        items = self.l2.GetItems()
        for item in items:
            self.l1.Append(item)
        self.l2.Clear()

    def _move_right(self, event):
        selected_item_indices = self.l1.GetSelections()
        for i in selected_item_indices:
            self.l2.Append(self.l1.GetString(i))
            self.l1.Delete(i)

    def _move_left(self, event):
        selected_item_indices = self.l2.GetSelections()
        for i in selected_item_indices:
            self.l1.Append(self.l2.GetString(i))
            self.l2.Delete(i)

    def __init__(self, parent, choices, label=''):
        super(DoubleListBox, self).__init__(parent)

        box = wx.StaticBox(self, -1, label)
        vsizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer.Add(self.sizer)
        self.sizer.AddSpacer(5)

        button_sizer = wx.BoxSizer(wx.VERTICAL)

        b_right = wx.Button(self, -1, '>', size=(30,25))
        b_right.Bind(wx.EVT_BUTTON, self._move_right) 
        button_sizer.Add(b_right)

        b_left = wx.Button(self, -1, '<', size=(30,25))
        b_left.Bind(wx.EVT_BUTTON, self._move_left) 
        button_sizer.Add(b_left)

        b_rright = wx.Button(self, -1, '>>', size=(30,25))
        b_rright.Bind(wx.EVT_BUTTON, self._all_right) 
        button_sizer.Add(b_rright)

        b_lleft = wx.Button(self, -1, '<<', size=(30,25))
        b_lleft.Bind(wx.EVT_BUTTON, self._all_left) 
        button_sizer.Add(b_lleft)

        self.l1 = wx.ListBox(self, choices=choices, style=wx.LB_MULTIPLE)
        self.l2 = wx.ListBox(self, choices=[], style=wx.LB_MULTIPLE)
        self.l1.SetMinSize((-1, 100))
        self.l2.SetMinSize((self.l1.GetSize()[0], 100))

        self.sizer.Add(self.l1)
        self.sizer.Add(button_sizer)
        self.sizer.Add(self.l2)

        self.sizer.AddSpacer(5)
        vsizer.AddSpacer(5)

        self.SetSizerAndFit(vsizer)

class MainFrame(BaseFrame):

    name = 'Double List Box Test'

    def init_gui(self):
        items = [
            'test1',
            'test2',
        ]
        self.lst = DoubleListBox(self.main_panel, choices=items, label='Double list box')
        self.add_to_main_panel(self.lst)

if __name__ == "__main__":
    app = wx.App()
    top = MainFrame()
    app.MainLoop()
