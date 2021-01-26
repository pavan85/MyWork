#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk


# In[2]:


root=tk.Tk()


# In[3]:


canvas1=tk.Canvas(root,width=400,height=300)
canvas1.pack()


# In[4]:


entry1=tk.Entry(root)
canvas1.create_window(200,140,window =entry1)


# In[5]:


def getsquareroot():
    x1=entry1.get()
    label1=tk.Label(root, text=float(x1)**0.5,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200,230,window =label1)
    


# In[6]:


button1=tk.Button(text='Get the Square Root',command=getsquareroot,bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200,180,window=button1)


# In[7]:


def clear_charts():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()


# In[8]:


root.mainloop()

