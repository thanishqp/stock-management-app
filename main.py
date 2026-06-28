import tkinter as tk
from tkinter import font
from tkinter.font import Font
from tkinter import messagebox
from tkinter import ttk
from tkinter import messagebox
import sqlite3

r = tk.Tk()
win_width = 500
win_height = 400
r.title("Stock Management System")
r.config(bg="indian red")
r.iconbitmap("D:\DEVELOPER\python projects\stock_management_app\icons.ico")
txt1 = tk.StringVar()
txt2 = tk.StringVar()
v1=tk.IntVar()
v2=tk.StringVar()
v3=tk.IntVar()
v4=tk.IntVar()
v5=tk.StringVar()
v6=tk.DoubleVar()


def get_counts():
    conn = sqlite3.connect("D:\DEVELOPER\python projects\stock_management_app\stockmang.db")
    cursor = conn.cursor()
    cursor.execute("SELECT PTYPE,count(PCODE) FROM Stock GROUP BY PTYPE")
    data = cursor.fetchall()
    conn.close()

    groceries = electronics = stationery = 0
    for row in data:
        if row[0].lower() == "groceries":
            groceries = row[1] if row[1] else 0
        elif row[0].lower() == "electronics":
            electronics = row[1] if row[1] else 0
        elif row[0].lower() == "stationery":
            stationery = row[1] if row[1] else 0

    total_stock = groceries + electronics + stationery
    return total_stock, groceries, electronics, stationery



def home_window():
    global l5, l7, l9, l11
    m = tk.Toplevel()
    m.geometry("1000x800")
    m.iconbitmap("D:\DEVELOPER\python projects\stock_management_app\icons.ico")
#     m.resizable(False,False)
    mbar = tk.Menu(m)
    m.config(menu=mbar,bg="seashell2")
    l2=tk.Label(m,text="Stock Management System",font= Font(size=25,family = "Times New Roman",),bg="red",fg="yellow",relief="ridge")
    l2.pack(fill="x")
    l3 = tk.Label(m,text=" Dashboard : ", font= Font(size=20,family = "Arial",),bg="seashell2",fg="green",relief="solid")
    l3.place(x=40,y=65)

    total_stock, groceries, electronics, stationery = get_counts()

        
#---FRAME 1--#
    f2 = tk.Frame(m,bg="cyan3",height=150,width=150,padx=20,relief="ridge",highlightbackground="red",highlightthickness=5)
    l4 = tk.Label(f2,text="Total Stock",font=Font(size=20,family="times new roman"),bg="cyan3",fg="red")
    l4.pack(fill="x")
    l5 = tk.Label(f2, text=str(total_stock),bg="cyan3",fg="black",font=Font(size=22,family="Arial black"),pady=10)
    l5.pack(fill="x")
    f2.place(x=95,y=120)
    # -- FRAME 2 -- #
    f3 = tk.Frame(m,bg="lime green",height=150,width=150,padx=20,relief="ridge",highlightbackground="gold",highlightthickness=5)
    l6 = tk.Label(f3,text="Groceries",font=Font(size=20,family="times new roman"),bg="lime green",fg="white")
    l6.pack(fill="x")
    l7 = tk.Label(f3, text=str(groceries),bg="lime green",fg="black",font=Font(size=22,family="Arial black"),pady=10)
    l7.pack(fill="x")
    f3.place(x=315,y=120)
# --- FRAME 3 ---#
    f4 = tk.Frame(m,bg="orange red",height=150,width=150,padx=20,relief="ridge",highlightbackground="blue2",highlightthickness=5)
    l8 = tk.Label(f4,text="Electronics",font=Font(size=20,family="times new roman"),bg="orange red",fg="yellow")
    l8.pack(fill="x")
    l9 = tk.Label(f4, text=str(electronics),bg="orange red",fg="black",font=Font(size=22,family="Arial black"),pady=10)
    l9.pack(fill="x")
    f4.place(x=520,y=120)
# --- FRAME 4 ---#
    f5 = tk.Frame(m,bg="lemon chiffon",height=150,width=150,padx=20,relief="ridge",highlightbackground="maroon1",highlightthickness=5)
    l10 = tk.Label(f5,text="Stationery",font=Font(size=20,family="times new roman"),bg="lemon chiffon",fg="red")
    l10.pack(fill="x")
    l11 = tk.Label(f5, text=str(stationery),bg="lemon chiffon",fg="black",font=Font(size=22,family="Arial black"),pady=10)
    l11.pack(fill="x")
    f5.place(x=725,y=120)
#---Separator--#
    sf =tk.Frame(m,height=1,bg="red")
    sf.pack(fill="x",pady=250)

        ###- DISPLAYING THE STOCK-------------##
    style = ttk.Style()
    style.theme_use("default")
    tree_font = font.Font(family="Arial", size=14)
    style.configure("Treeview", background="black", foreground="white",
                    fieldbackground="lime green", font=tree_font)
    style.configure("Treeview.Heading", background="VioletRed1",
                    foreground="white", font=("Arial", 16, "bold"))

    a = tk.Label(m, text="STOCKS", font=my, bg="red", fg="yellow")
    a.place( y=320,anchor="center",relx=0.5)

    # --- Treeview + Scrollbar (placed, not packed) ---
    global tree
    tree = ttk.Treeview(
        m,
        columns=("PCODE", "PNAME", "PQTY", "PRICE", "PTYPE", "Amt"),
        show="headings"
    )
    s = tk.Scrollbar(m, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=s.set)

    tree.heading("PCODE", text="Product Code")
    tree.heading("PNAME", text="Product Name")
    tree.heading("PQTY", text="Product QTY")
    tree.heading("PRICE", text="PRODUCT PRICE")
    tree.heading("PTYPE", text="Product TYPE")
    tree.heading("Amt", text="TOTAL AMOUNT")

    tree.column("PCODE", width=100, anchor="center")
    tree.column("PNAME", width=150, anchor="center")
    tree.column("PQTY", width=100, anchor="center")
    tree.column("PRICE", width=120, anchor="center")
    tree.column("PTYPE", width=120, anchor="center")
    tree.column("Amt", width=120, anchor="center")

    # ---- RESIZER (works with .place) ----
    LEFT_MARGIN = 140      
    RIGHT_MARGIN = 40      
    TOP_Y = 360            
    BOTTOM_MARGIN = 40     
    SCROLLBAR_W = 18       

    def resize_tree(event=None):
        
        w = m.winfo_width()
        h = m.winfo_height()

        # compute available size
        tw = max(200, w - LEFT_MARGIN - RIGHT_MARGIN - SCROLLBAR_W)
        th = max(160, h - TOP_Y - BOTTOM_MARGIN)

        # place tree and scrollbar
        tree.place(x=LEFT_MARGIN, y=TOP_Y, width=tw, height=th)
        s.place(x=LEFT_MARGIN + tw, y=TOP_Y, width=SCROLLBAR_W, height=th)

    # place once now, and whenever window resizes
    resize_tree()
    m.bind("<Configure>", resize_tree)

    # --- Load data ---
    conn = sqlite3.connect(r"D:\DEVELOPER\python projects\stock_management_app\stockmang.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Stock")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

    def on_tree_select(event):
        sel = tree.selection()
        if sel:
            vals = tree.item(sel)["values"]
            v1.set(vals[0]); v2.set(vals[1]); v3.set(vals[2])
            v4.set(vals[3]); v5.set(vals[4]); v6.set(vals[5])

    tree.bind("<<TreeviewSelect>>", on_tree_select)


    file = tk.Menu(mbar, tearoff=0)
    edit = tk.Menu(mbar, tearoff=0)
    file.add_command(label="new",font=Font(size=14,family="Arial"),command=new_window)
    file.add_separator()

    edit.add_command(label="Update",command=update_window,font=Font(size=14,family="Arial"))
    edit.add_command(label="Delete",command=delete_window,font=Font(size=14,family="Arial"))
    edit.add_separator()

    file.add_command(label="Exit", command=m.destroy,font=Font(size=14,family="Arial"))

    mbar.add_cascade(label="  File  ",menu=file)
    mbar.add_cascade(label="  Edit  ", menu=edit)
    mbar.add_cascade(label="  Refresh  ",command=refresh_dashboard)
    
def refresh_stock():
        conn = sqlite3.connect(r"D:\DEVELOPER\python projects\stock_management_app\stockmang.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Stock")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

        def on_tree_select(event):
            sel = tree.selection()
            if sel:
                vals = tree.item(sel)["values"]
                v1.set(vals[0]); v2.set(vals[1]); v3.set(vals[2])
                v4.set(vals[3]); v5.set(vals[4]); v6.set(vals[5])

        tree.bind("<<TreeviewSelect>>", on_tree_select)

# ===== Refresh Dashboard Counts =====
def refresh_dashboard():
    total_stock, groceries, electronics, stationery = get_counts()
    l5.config(text=str(total_stock))
    l7.config(text=str(groceries))
    l9.config(text=str(electronics))
    l11.config(text=str(stationery))
    if "tree" in globals():
        for row in tree.get_children():
            tree.delete(row)
        conn = sqlite3.connect(r"D:\DEVELOPER\python projects\stock_management_app\stockmang.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Stock")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

def new_window():
    m = tk.Toplevel()
    m.geometry("750x450")
    mbar = tk.Menu(m)
    m.config(menu=mbar,bg="sky blue")
    m.resizable(False,False)
    m.iconbitmap("D:\DEVELOPER\python projects\stock_management_app\icons.ico")

   ###Connecting Database ----#
    def upload() :
        s1=v1.get()
        s2=v2.get().strip()
        s3=v3.get()
        s4=v4.get()
        s5=v5.get().strip()

         
        if not s1 or not s2 or not s3 or not s4 or not s5:
            messagebox.showerror("Error", "Please fill all the fields before uploading.")
            return

        s6=s3*s4
        v6.set(s6)
        conn = sqlite3.connect("D:\DEVELOPER\python projects\stock_management_app\stockmang.db")
        cursor = conn.cursor()
        cursor.execute("insert into Stock (PCODE,PNAME,PQTY,PRICE,PTYPE,Amt)values(?,?,?,?,?,?)",(s1,s2,s3,s4,s5,s6))
        conn.commit()
        messagebox.showinfo("this message says","successfully registered")
        print("Product Code :",v1.get())
        print("Product Name:",v2.get())
        print("Product Qty :",v3.get())
        print("Product  Price : Rs.",v4.get())
        print("Product Type : ",v5.get())
        print("Total Amount",v6.get())

    l3 = tk.Label(m, text="STOCKY ENTRY", font=Font(size=20),bg="red",fg="white")
    l3.grid(row=0, column=1, pady=10,)

    # Configure column 1 to expand horizontally
    # m.grid_columnconfigure(1, weight=1)   
        
    l1=tk.Label(m,text="PRODUCT ID :",font= Font(size=20),bg="sky blue",fg="brown1")
    l1.grid(row=1,column=0,pady=10,padx=10)
    e1=tk.Entry(m,width=20,font= Font(size=20),textvariable=v1,highlightbackground="SeaGreen1",highlightthickness=5)
    e1.grid(row=1,column=1,padx=10,pady=10)
    l1=tk.Label(m,text="PRODUCT NAME :",font= Font(size=20),bg="sky blue",fg="brown1")
    l1.grid(row=2,column=0,pady=10,padx=10)
    e1=tk.Entry(m,width=20,font= Font(size=20),textvariable=v2,highlightbackground="black",highlightthickness=5)
    e1.grid(row=2,column=1,padx=10,pady=10)

    l1=tk.Label(m,text="PRODUCT Qty :",font= Font(size=20),bg="sky blue",fg="brown1")
    l1.grid(row=3,column=0,pady=10,padx=10)
    e1=tk.Entry(m,width=20,font= Font(size=20),textvariable=v3,highlightbackground="orange",highlightthickness=5)
    e1.grid(row=3,column=1,padx=10,pady=10)

    l1=tk.Label(m,text="PRODUCT PRICE :",font= Font(size=20),bg="sky blue",fg="brown1")
    l1.grid(row=4,column=0,pady=10,padx=10)
    e1=tk.Entry(m,width=20,font= Font(size=20),textvariable=v4,highlightbackground="salmon",highlightthickness=5)
    e1.grid(row=4,column=1,padx=10,pady=10)
    l1=tk.Label(m,text="PRODUCT TYPE :",font= Font(size=20),bg="sky blue",fg="brown1")
    l1.grid(row=5,column=0,pady=10,padx=10)
    opt= tk.OptionMenu(m,v5,"Groceries","Electronics","Stationery")
    opt.grid(row=5,column=1,padx=10,pady=10,ipadx=20)
    lb=tk.Button(m, text="UPLOAD",font= Font(family="ArialBlack",size=14),bg="red",fg="gold",
                 command=upload,width=50,height=1,activebackground="green",activeforeground="white")
    lb.place(y=170,relx=0.5, rely=0.5, anchor="center")    

def disp_window():  
     

    d=tk.Toplevel(r)
    d.geometry("1000x400")
    style = ttk.Style()     
    style.theme_use("default")

    tree_font = font.Font(family="Arial", size=14)

# Set background and text color for Treeview
    style.configure("Treeview",background="black",foreground="white",fieldbackground="lime green",font=tree_font)

# Change header style too
    style.configure("Treeview.Heading",background="VioletRed1",foreground="white",font=("Arial",16,"bold"))

    # Treeview for displaying student details
    s= tk.Scrollbar(d,orient="vertical")
    s.pack(fill="y",side="right")
    
    a =tk.Label(d,text="STOCKS",font=my,bg="red",fg="yellow")
    a.pack(fill="x")
    tree = ttk.Treeview(d, columns=("PCODE", "PNAME", "PQTY", "PRICE", "PTYPE", "Amt"), show="headings",padding=10,yscrollcommand=s.set,)
    tree.heading("PCODE", text="Product Code")
    tree.heading("PNAME", text="Product Name")
    tree.heading("PQTY", text="Product QTY")
    tree.heading("PRICE", text="PRODUCT PRICE ")
    tree.heading("PTYPE", text="Product TYPE")
    tree.heading("Amt", text="TOTAL AMOUNT ")
    tree.column("PCODE", width=100)
    tree.column("PNAME", width=150)
    tree.column("PQTY", width=100)
    tree.column("PRICE", width=120)
    tree.column("PTYPE", width=80)
    tree.column("Amt", width=120)
    tree.pack(fill="both",ipadx=20)
    s.config(command=tree.yview)
    # Clear previous treeview entries
    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("D:\DEVELOPER\python projects\stock_management_app\stockmang.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Stock")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)
    def on_tree_select(event):
        selected_item = tree.selection()
        if selected_item:
            values = tree.item(selected_item)["values"]
            v1.set(values[0])
            v2.set(values[1])
            v3.set(values[2])
            v4.set(values[3])
            v5.set(values[4])
            v6.set(values[5])

    tree.bind("<<TreeviewSelect>>", on_tree_select)

    conn.close()


def delete_window():
    de = tk.Toplevel()
    de.geometry("750x450")
    mbar = tk.Menu(de)
    de.iconbitmap("D:\DEVELOPER\python projects\stock_management_app\icons.ico")
    de.config(menu=mbar,bg="MediumPurple1")
    de.resizable(False,False)

     ###Connecting Database ----#

  
    def delete() :
        s1=v1.get()
        conn = sqlite3.connect("D:\DEVELOPER\python projects\stock_management_app\stockmang.db")
        cursor = conn.cursor()
        cursor.execute("delete from Stock where PCODE=?",(s1,))
        conn.commit()
        messagebox.showinfo("this message says","successfully deleted")
        refresh_dashboard()



    l3 = tk.Label(de, text="DELETING STOCK ENTRY", font=Font(size=20),bg="red",fg="white")
    l3.grid(row=0, column=1, pady=10,)

   
    l1=tk.Label(de,text="PRODUCT ID :",font= Font(size=20),bg="MediumPurple1",fg="white")
    l1.grid(row=1,column=0,pady=10,padx=10)
    e1=tk.Entry(de,width=20,font= Font(size=20),textvariable=v1,highlightbackground="SeaGreen1",highlightthickness=5)
    e1.grid(row=1,column=1,padx=10,pady=10)
    l1=tk.Label(de,text="PRODUCT NAME :",font= Font(size=20),bg="MediumPurple1",fg="white")
    l1.grid(row=2,column=0,pady=10,padx=10)
    e1=tk.Entry(de,width=20,font= Font(size=20),textvariable=v2,highlightbackground="black",highlightthickness=5)
    e1.grid(row=2,column=1,padx=10,pady=10)

    l1=tk.Label(de,text="PRODUCT Qty :",font= Font(size=20),bg="MediumPurple1",fg="white")
    l1.grid(row=3,column=0,pady=10,padx=10)
    e1=tk.Entry(de,width=20,font= Font(size=20),textvariable=v3,highlightbackground="orange",highlightthickness=5)
    e1.grid(row=3,column=1,padx=10,pady=10)

    l1=tk.Label(de,text="PRODUCT PRICE :",font= Font(size=20),bg="MediumPurple1",fg="white")
    l1.grid(row=4,column=0,pady=10,padx=10)
    e1=tk.Entry(de,width=20,font= Font(size=20),textvariable=v4,highlightbackground="salmon",highlightthickness=5)
    e1.grid(row=4,column=1,padx=10,pady=10)
    l1=tk.Label(de,text="PRODUCT TYPE :",font= Font(size=20),bg="MediumPurple1",fg="brown1")
    l1.grid(row=5,column=0,pady=10,padx=10)
    opt= tk.OptionMenu(de,v5,"Groceries","Electronics","Stationery")
    opt.grid(row=5,column=1,padx=10,pady=10,ipadx=20)
    lb=tk.Button(de, text="DELETE",font= Font(family="ArialBlack",size=14),bg="red",fg="gold",command=delete,width=50,height=1,activebackground="green",activeforeground="white")
    lb.place(y=170,relx=0.5, rely=0.5, anchor="center")

def update_window():
    up = tk.Toplevel()
    up.geometry("750x450")
    mbar = tk.Menu(up)
    up.config(menu=mbar,bg="spring green")
    up.resizable(False,False)
    up.iconbitmap("D:\DEVELOPER\python projects\stock_management_app\icons.ico")

     ###Connecting Database ----#
    def update():
        s1 = v1.get()  
        s2 = v2.get()  
        s3 = v3.get()  
        s4 = v4.get()  
        s5 = v5.get()  
         
        if not s1 or not s2 or not s3 or not s4 or not s5:
            messagebox.showerror("Error", "Please fill all the fields before uploading.")
            return
        
        s6=s3*s4
        v6.set(s6)
        conn = sqlite3.connect("D:\DEVELOPER\python projects\stock_management_app\stockmang.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE Stock set PNAME=?, PQTY=?, PRICE=?, PTYPE=?, Amt=? WHERE PCODE=? ", (s2, s3, s4, s5, s6,s1)) 
        conn.commit()
        messagebox.showinfo("Success", "Successfully updated the record")
        refresh_dashboard()
        conn.close()



    l3 = tk.Label(up, text="UPDATING STOCK ENTRY", font=Font(size=20),bg="red",fg="white")
    l3.grid(row=0, column=1, pady=10,)

   
    l1=tk.Label(up,text="PRODUCT ID :",font= Font(size=20),bg="spring green",fg="black")
    l1.grid(row=1,column=0,pady=10,padx=10)
    e1=tk.Entry(up,width=20,font= Font(size=20),textvariable=v1,highlightbackground="SeaGreen1",highlightthickness=5)
    e1.grid(row=1,column=1,padx=10,pady=10)
    l1=tk.Label(up,text="PRODUCT NAME :",font= Font(size=20),bg="spring green",fg="black")
    l1.grid(row=2,column=0,pady=10,padx=10)
    e1=tk.Entry(up,width=20,font= Font(size=20),textvariable=v2,highlightbackground="black",highlightthickness=5)
    e1.grid(row=2,column=1,padx=10,pady=10)

    l1=tk.Label(up,text="PRODUCT Qty :",font= Font(size=20),bg="spring green",fg="black")
    l1.grid(row=3,column=0,pady=10,padx=10)
    e1=tk.Entry(up,width=20,font= Font(size=20),textvariable=v3,highlightbackground="orange",highlightthickness=5)
    e1.grid(row=3,column=1,padx=10,pady=10)

    l1=tk.Label(up,text="PRODUCT PRICE :",font= Font(size=20),bg="spring green",fg="black")
    l1.grid(row=4,column=0,pady=10,padx=10)
    e1=tk.Entry(up,width=20,font= Font(size=20),textvariable=v4,highlightbackground="salmon",highlightthickness=5)
    e1.grid(row=4,column=1,padx=10,pady=10)
    l1=tk.Label(up,text="PRODUCT TYPE :",font= Font(size=20),bg="spring green",fg="black")
    l1.grid(row=5,column=0,pady=10,padx=10)
    opt= tk.OptionMenu(up,v5,"Groceries","Electronics","Stationery")
    opt.grid(row=5,column=1,padx=10,pady=10,ipadx=20)
    lb=tk.Button(up, text="UPDATE",font= Font(family="ArialBlack",size=14),bg="red",fg="gold",command=update,width=50,height=1,activebackground="green",activeforeground="white")
    lb.place(y=170,relx=0.5, rely=0.5, anchor="center")

def save() :
    us = txt1.get()
    pwd = txt2.get()
    if  (us == "" and pwd == ""):
       messagebox.showwarning("Stock Management System","! Fill the Fields to login !")
    elif (us == "admin" and pwd == "1234"):
       ls ="Login Success"
       messagebox.showinfo("Stock Management System",ls)
       home_window()
    elif (us =="admin" and pwd == ""):
        messagebox.showwarning("Stock Management System"," !!Please will the password fields !!")  
    elif (us =="" and pwd == "1234"):
        messagebox.showwarning("Stock Management System"," !!Please will the username fields !!")         
    else :
           print("invalid login")
           messagebox.showerror("Stock Management System","! Invalid Username and Password !")    
def clear():
    txt1.set("")    
    txt2.set("")    
def exit():
    r.destroy()    

my = Font(family="Arial", size=20, weight="bold")
mine = Font(family="Times New Roman", size=22, weight="bold",)
fon = Font(family="times new roman",size=18,weight="bold")
# Frame for login form
frame = tk.LabelFrame(r, bg="salmon",text="Login Details", font=("Arial", 12, "bold"), fg="white",bd=3, relief="groove")
frame.pack(expand=True,padx=20, pady=20,fill="both")
# Username
lu=tk.Label(frame, text="Username:", bg="salmon", font=my)
lu.grid(row=1, column=1, pady=10, sticky="w")
eu=tk.Entry(frame,textvariable=txt1,width=30,font=fon,fg="blue")
eu.grid(row=1, column=2, pady=10,padx=10)
# Password
lp=tk.Label(frame, text="Password:", bg="salmon", font=my)
lp.grid(row=2, column=1, pady=10, sticky="w")
ep=tk.Entry(frame,textvariable=txt2,width=30,show="*",font=fon,fg="red")
ep.grid(row=2, column=2, pady=10,padx=10)
# Login Button and Clear button
lb=tk.Button(frame, text="Login", bg="green", fg="white",padx=20, font=my,command=save)
lb.grid(row=3, column=1, rowspan=2, pady=20)
lbc=tk.Button(frame, text="Clear", bg="orange", fg="white",padx=20,font=my,command=clear)
lbc.grid(row=3, column=1, columnspan=2, pady=20)
lbc=tk.Button(frame, text="Exit", bg="red", fg="white",padx=20,font=my,command=exit)
lbc.place(x=400,y=135)

r.mainloop()
