import tkinter as tk
from WebAutomation49 import WebAutomation

class App:
    def __init__(self,root):
        self.root=root
        self.root.title("Web Automation GUI")
        #login frame
        self.login_frame=tk.Frame(self.root)
        self.login_frame.pack(padx=50,pady=50)

        tk.Label(self.login_frame,text="Username").grid(row=0,column=0,sticky='w')
        self.entry_username=(tk.Entry(self.login_frame))
        self.entry_username.grid(row=0,column=1,sticky="ew")

        tk.Label(self.login_frame,text="Password").grid(row=1,column=0,sticky='w')
        self.entry_password=(tk.Entry(self.login_frame,show="*"))
        self.entry_password.grid(row=1,column=1,sticky="ew")

        # from submission button
        self.from_frame=tk.Frame(self.root)
        self.from_frame.pack(padx=50,pady=50)

        tk.Label(self.login_frame, text="Full Name").grid(row=0, column=0, sticky='w')
        self.entry_full_name = tk.Entry(self.from_frame)
        self.entry_full_name.grid(row=0, column=1, sticky="ew")

        tk.Label(self.from_frame,text="Email").grid(row=1,column=0,sticky="w")
        self.entry_email=tk.Entry(self.from_frame)
        self.entry_email.grid(row=1,column=1,sticky="ew")

        tk.Label(self.from_frame,text="Current Address").grid(row=2,column=0,sticky="w")
        self.entry_current_address=tk.Entry(self.from_frame)
        self.entry_current_address.grid(row=2,column=1,sticky="ew")

        tk.Label(self.from_frame,text="Permanent Address").grid(row=3,column=0,sticky="w")
        self.entry_permanent_address=tk.Entry(self.from_frame)
        self.entry_permanent_address.grid(row=3,column=1,sticky="ew")

        #button
        self.button_frame=tk.Frame()
        self.button_frame.pack(padx=50,pady=50)
        tk.Button(self.button_frame,text="Submit",command=self.submit_data).grid(row=0,column=0,padx=10)
        tk.Button(self.button_frame,text="Close browser",command=self.close_browser).grid(row=1,column=0,padx=10)

    def submit_data(self):
        username=self.entry_username.get()
        password=self.entry_password.get()
        full_name=self.entry_full_name.get()
        email=self.entry_email.get()
        current_address=self.entry_current_address.get()
        permanent_address=self.entry_permanent_address.get()

        self.automation=WebAutomation()
        self.automation.login(username,password)
        self.automation.fill_form(full_name,email,current_address,permanent_address)

    def close_browser(self):
        self.automation.close()








root1=tk.Tk()
app=App(root1)
root1.mainloop()
