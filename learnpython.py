#This is a comment syntax
if 5> 2: #กำหนดเงื่อนไขว่า หาก 5 มากกว่า 2 ให้แสดงผล
    print ("Five is greater then two") # print แสดงค่า string ว่า Five is greater then two

name = "Panakan" #ประกาศค่าตัวแปร name เท่ากับค่า string ว่า Panakan
age = 29 #ประกาศค่าตัวแปร age เป็นค่า int ว่า 29
print(name)#คำสั่งให้แสดงค่า name ใน Terminal
print("My Name is "+ name)#คำสั่งให้แสดงค่า String My Name is กับตัวแปร name 
print("I'm "+ str(age) + " years old")#คำสั่งให้แสดงค่า String I'm และคำสั่ง str() ที่ใช้แปลงค่าในวงเล็บเป็น String 

x, y, z = "orange","banana" ,"apple"
print(x)
print(y)
print(z)

fruits = ["apple" , "banana", "orange"] # ประกาศ list ชื่อ fruits **python ไม่มี build in array แต่เราสามารถใช้ list แทนได้

a = "awesome"

def myfunc(): #คำสั่ง def ที่ใช้ในการสร้าง Function ตั้งชื่อว่า myfunc()
    a = "fantastic"#Local variables เป็นตัวแปรที่สามารถใช้ได้แค่ใน Function ที่ประกาศเท่านั้น นอกจากว่าจะใช้คำสั่ง global a
    print("Python is "+ a)

myfunc() #คำสั่งเรียกใช้ Function mufunc()
