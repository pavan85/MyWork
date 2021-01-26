#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import pyodbc
from tkinter import * 
root=Tk()


# In[22]:


def Submit():
    Name=e1.get()
    Phone=e2.get()
    Email=e3.get()
    Course=e4.get()
    df= pd.DataFrame.from_records([{"Name_of_the_Student":Name, "Contact_Number":Phone,"Email_id":Email,"Course":Course}])
    print(df)
    df['Contact_Number'] = df['Contact_Number'].astype(int)
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server= Enter your Server details;"
                      "Database=Enter your Databasename;"
                      "Trusted_Connection=yes;")
    cursor = conn.cursor()
    for index,row in df.iterrows():
        cursor.execute("INSERT INTO Tablename (column1,column2,column3,column4)values(?,?,?,?)",
                       row[0],row[1],row[2],row[3])
    cursor.commit()
    conn.close()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


# In[23]:


root.geometry("400x300")
root.title("Student Management System")
Label(root,text="Name_of_the_Student").grid(row=0)
Label(root,text="Contact_Number").grid(row=1)
Label(root,text="Email_id").grid(row=2)
Label(root,text="Course").grid(row=3)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)


# In[24]:


submitButton = Button(root, text="Submit",command=Submit,bg='red').grid(row=5, column=1,pady=6)


# In[25]:


root.mainloop()


# In[ ]:




