import wx

# ---------- Event handler ----------
def on_click(event):
    if terms_check.GetValue():
        firstname=first_name_entry.GetValue()
        lastname=last_name_entry.GetValue()
        if firstname and lastname:
            title=title_combobox.GetValue()
            age=age_spinbox.GetValue()
            nationality=nationality_combobox.GetValue()
            numcourses=numcourses_spin.GetValue()
            semesters=sem_spin.GetValue()
            reg=registered_check.GetValue()
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ",title,"Age: ",age,"Nationality: ",nationality)
            print("Courses: ",numcourses,"Semesters: ",semesters)
            if reg:
                print("Currently registered")
            else:
                print("Not registered")
            print("----------------------------------")
        else:
            wx.MessageBox(
            "First name and last name are required",
            "Warning",
            wx.OK | wx.ICON_WARNING)

    else:
        wx.MessageBox(
            "You cannot enter data without agreeing to the terms and conditions",
            "Warning",
            wx.OK | wx.ICON_WARNING)

        
# ---------- App & Frame ----------
app = wx.App()
frame = wx.Frame(None, title="Data Entry Form")
panel = wx.Panel(frame)

main_sizer = wx.BoxSizer(wx.VERTICAL)

# --------- User Information ---------
user_info_box = wx.StaticBox(panel, label="User Information")
user_info_sizer = wx.StaticBoxSizer(user_info_box, wx.VERTICAL)

grid1 = wx.GridBagSizer(10, 10)

first_name_label = wx.StaticText(panel, label="First Name")
last_name_label = wx.StaticText(panel, label="Last Name")
title_label = wx.StaticText(panel, label="Title")
age_label = wx.StaticText(panel, label="Age")
nationality_label = wx.StaticText(panel, label="Nationality")

first_name_entry = wx.TextCtrl(panel)
last_name_entry = wx.TextCtrl(panel)
title_combobox = wx.ComboBox(panel, choices=["", "Mr", "Ms", "Dr"], style=wx.CB_READONLY)
age_spinbox = wx.SpinCtrl(panel, min=18, max=110, initial=18)
nationality_combobox = wx.ComboBox(
    panel,
    choices=["Argentina", "Australia", "Brazil", "Canada", "China", "Egypt", "Ethiopia", "France", "Germany", "India", "Indonesia", "Italy", "Japan", "Mexico", "New Zealand", "Nigeria", "Russia", "South Africa", "South Korea", "United Kingdom", "United States","Others"],
    style=wx.CB_READONLY
)

grid1.Add(first_name_label, (0, 0))
grid1.Add(last_name_label, (0, 1))
grid1.Add(title_label, (0, 2))

grid1.Add(first_name_entry, (1, 0), flag=wx.EXPAND)
grid1.Add(last_name_entry, (1, 1), flag=wx.EXPAND)
grid1.Add(title_combobox, (1, 2), flag=wx.EXPAND)

grid1.Add(age_label, (2, 0))
grid1.Add(nationality_label, (2, 1))

grid1.Add(age_spinbox, (3, 0), flag=wx.EXPAND)
grid1.Add(nationality_combobox, (3, 1), flag=wx.EXPAND)

grid1.AddGrowableCol(0)
grid1.AddGrowableCol(1)
grid1.AddGrowableCol(2)

user_info_sizer.Add(grid1, 1, wx.EXPAND | wx.ALL, 10)
main_sizer.Add(user_info_sizer, 0, wx.EXPAND | wx.ALL, 10)

# --------- Courses ---------
courses_box = wx.StaticBox(panel, label="Courses / Registration Status")
courses_sizer = wx.StaticBoxSizer(courses_box, wx.VERTICAL)

grid2 = wx.GridBagSizer(10, 10)

registration_label = wx.StaticText(panel, label="Registration Status")
registered_check = wx.CheckBox(panel, label="Currently registered")

numcourses_label = wx.StaticText(panel, label="Completed courses")
numcourses_spin = wx.SpinCtrl(panel, min=0, max=1000)

sem_label = wx.StaticText(panel, label="Semesters")
sem_spin = wx.SpinCtrl(panel, min=0, max=10)

grid2.Add(registration_label, (0, 0))
grid2.Add(numcourses_label, (0, 1))
grid2.Add(sem_label, (0, 2))

grid2.Add(registered_check, (1, 0))
grid2.Add(numcourses_spin, (1, 1))
grid2.Add(sem_spin, (1, 2))

courses_sizer.Add(grid2, 1, wx.EXPAND | wx.ALL, 10)
main_sizer.Add(courses_sizer, 0, wx.EXPAND | wx.ALL, 10)

# --------- Terms ---------
terms_box = wx.StaticBox(panel, label="Terms & Conditions")
terms_sizer = wx.StaticBoxSizer(terms_box, wx.VERTICAL)

terms_check = wx.CheckBox(panel, label="I accept the terms and conditions")
terms_sizer.Add(terms_check, 0, wx.ALL, 10)

main_sizer.Add(terms_sizer, 0, wx.EXPAND | wx.ALL, 10)

# --------- Button ---------
btn_box = wx.StaticBox(panel)
btn_sizer = wx.StaticBoxSizer(btn_box, wx.VERTICAL)

btn = wx.ToggleButton(panel, label="Enter data")
btn.Bind(wx.EVT_TOGGLEBUTTON, on_click)

btn_sizer.Add(btn, 0, wx.ALL, 10)
main_sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)

# ---------- Final ----------
panel.SetSizer(main_sizer)
frame.SetSize((900, 600))
frame.Centre()
frame.Show()
app.MainLoop()