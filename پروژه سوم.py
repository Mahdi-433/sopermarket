import sqlite3
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("modiriat kala")
root.geometry("310x300")
root.resizable(False,False)
root.config( bg = "seashell2" )
#===================================================================================================#
data = sqlite3.connect("library.db")
xdata = data.cursor()

xdata.execute("""
CREATE TABLE IF NOT EXISTS supermarket (
   id INTEGER PRIMARY KEY,
   Product_Name TEXT,
   Number_Of_Product INTEGER,
   Price_Of_Product INTGER,
   Final_Price TEXT NOT NULL
)
""")
#===================================================================================================#
def Save_data():
   name = Product_name_entry.get()
   number = Number_of_goods_entry.get()
   price = The_price_of_goods_entry.get()
   total_price =Total_price_entry.get()
   if name and number and price and total_price:
      xdata.execute('''
      INSERT INTO supermarket (name, Number, Price, Total_price)
      VALUES (?, ?, ?, ?)
      ''', (name, number, price, total_price))
      data.commit()
      messagebox.showinfo("موفق", ". کالا با موفقيت ذخيره شد")
      Product_name_entry.delete(0, END)
      Number_of_goods_entry.delete(0, END)
      The_price_of_goods_entry.delete(0, END)
      Total_price_entry.delete(0, END)
   else:
      messagebox.showwarning("خطاي ورودي", ". لطفا تمام فيلد هارا پر کنيد")
#===================================================================================================#
def show_info():
   file_name = "library.db"
   data = sqlite3.connect(file_name)
   xdata = data.cursor()
   xdata.execute("SELECT * FROM supermarket")
   record = xdata.fetchall()
   records = []
   for i in record:
      records.append(i)
      messagebox.showinfo("اطلاعات", f"{records}")
      records.clear()
   data.close()
#===================================================================================================#
      
Product_name = Label (root , text = " نام کالا " , font = 20 , bg = "seashell2")
Product_name.place(x = 230 , y = 30 )

Product_name_entry = Entry ( root , text = "" , font = 20 )
Product_name_entry.place(width = 150 , x = 65 , y = 30 )
#===================================================================================================#

Number_of_goods = Label (root , text = " تعداد کالا " , font = 20 , bg = "seashell2")
Number_of_goods.place(x = 230 , y = 70 )

Number_of_goods_entry = Entry ( root , text = "" , font = 20 )
Number_of_goods_entry.place(width = 150 , x = 65 , y = 70 )
#===================================================================================================#

The_price_of_goods = Label (root , text = " قيمت کالا " , font = 20 , bg = "seashell2")
The_price_of_goods.place(x = 230 , y = 110 )

The_price_of_goods_entry = Entry ( root , text = "" , font = 20 )
The_price_of_goods_entry.place(width = 150 , x = 65 , y = 110 )
#===================================================================================================#

Total_price = Label (root , text = "قيمت کل" , font = 20 , bg = "seashell2" )
Total_price.place(x = 230 , y = 150 )

Total_price_entry = Entry ( root , text = "" , font = 20 )
Total_price_entry.place(width = 150 , x = 65 , y = 150 )

#===================================================================================================#
add_button = Button( root , text = " ذخيره در db " , font = 20 , bg = "seashell3" , command = Save_data)
add_button.place(width = 100 , x = 30 , y = 200)
#===================================================================================================#
delete_button = Button( root , text = " مشاهده اطلاعات " , font = 20 , bg = "seashell3" , command = show_info )
delete_button.place(width = 100 , x = 150 , y = 200)
#===================================================================================================#
close_button = Button( root , text = " خروج " , font = 20 , bg = "seashell3" ,  command = quit)
close_button.place(width = 100 , x = 90 , y = 250)
#===================================================================================================#


root.mainloop()
