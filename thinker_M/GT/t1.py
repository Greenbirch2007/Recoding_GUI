# # # # # # # #!/usr/bin/python
# # # # # # # #-*- coding: utf-8 -*-
# # # # # # #
# # # # # # #
# # # # # # # # 安装  sudo apt search python3-tk
# # # # # # #
# # # # # # #
# # # # # # # # import tkinter
# # # # # # # #
# # # # # # # # top = tkinter.Tk()
# # # # # # # # # 进入消息循环
# # # # # # # # top.mainloop()
# # # # # # #
# # # # # # # from tkinter import * # 导入tkinter库
# # # # # # # root = Tk()   # 创建窗口对象的背景色
# # # # # # #
# # # # # # # # 创建两个列表
# # # # # # #
# # # # # # #
# # # # # # # li = ['C','python','php','html','sql','java']
# # # # # # # movie = ['css','jquery','bootstrap']
# # # # # # #
# # # # # # # lista = Listbox(root) #创建两个列表组件
# # # # # # # listb = Listbox(root)
# # # # # # #
# # # # # # #
# # # # # # # for item in li:
# # # # # # #     lista.insert(0,item)  # 第一个小部件插入数据
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # for item in movie:
# # # # # # #     listb.insert(0,item)  # 第二个小部件插入数据
# # # # # # #
# # # # # # #
# # # # # # # lista.pack()   # 将叫部件放置到主窗口中
# # # # # # # listb.pack()
# # # # # # # Button()
# # # # # # #
# # # # # # # root.mainloop()    # 进入消息循环
# # # # # #
# # # # # # import tkinter # 导入thinter库
# # # # # #
# # # # # # tkinter._test()  # 使用内置的test进行车市
# # # # # #
# # # # # #
# # # # # #
# # # # # # # 创建一个简单的窗口
# # # # # #
# # # # # import tkinter as tk
# # # # #
# # # # # root = tk.Tk()   # 对Tk这个类实例化，即创建root实例
# # # # #
# # # # # root.title('~~~~电力窗口名') # 设置窗口
# # # # # root.geometry("400x200+100+100")  # 设置窗口大小，窗口的初始位置
# # # # # root.resizable(False,True)   # 设置只能调整窗口的Y方向大小
# # # # # root.mainloop() # 进行事件循环，把它当做内部的一个执行动作
# # # #
# # # #
# # # # # “标签”组件的使用
# # # #
# # # # import tkinter as tk
# # # # root = tk.Tk()
# # # # root.title("使用标签～～～")
# # # # root.geometry("400x200+100+100")
# # # # root.resizable(False,False) #禁止调整窗口大小
# # # # my_label = tk.Label(root,text="标签内容放在这里",background="green",font=("Arial",12),width=15,height=2)
# # # # my_label.pack()   # 放置标签my_label
# # # #
# # # # root.mainloop()
# # # # #
# # #
# # # # 按钮的使用
# # #
# # # import tkinter as tk
# # # root = tk.Tk()
# # # root.title("使用按钮")
# # # root.geometry("400x200")
# # #
# # # # 定义单击按钮动作，注意：定义按钮动作的代码要在写在放置按钮的前面
# # #
# # #
# # # # 竟然可以命名汉字的函数
# # # def 单击按钮():
# # #     lb = tk.Label(root,text="单击按钮后显示的内容！",background="yellow",font=("Arial",12),width=18,height=2) # 设置Label对象及属性
# # #     lb.pack()
# # #
# # # # 设置Button对象及属性
# # #
# # # my_button = tk.Button(root,text='按钮上的内容！',background="pink",font=("Arial",12),width=18,height=2,command=单击按钮)
# # #
# # #
# # # # 放置按钮
# # #
# # # my_button.pack()
# # # root.mainloop()
# # #
# # # #
# # #
# # # pack方法是tkinter中的一个布局方式
# #
# # from tkinter import *
# # root = Tk()
# # root.title("pack布局～～～")
# # Button(root,text="A",background="pink").pack(side=LEFT,expand=NO,fill=Y,anchor=W)
# # Button(root,text="B",background="#FFFFFF").pack(side=TOP,expand=YES,fill=BOTH,anchor=E)
# # Button(root,text="C",background="grey").pack(side=RIGHT,expand=YES,fill=NONE,anchor=NE)
# # Button(root,text="D",background="#63B8FF").pack(side=LEFT,expand=NO,fill=Y,anchor=E)
# # Button(root,text="E",background="#00FA9A").pack(side=TOP,expand=NO,fill=BOTH)
# # Button(root,text="F",background="#00CDCD").pack(side=BOTTOM,expand=YES)
# # Button(root,text="G",background="#8B3E2F").pack(anchor=SE)
# # root.mainloop()
# #
# # # background是设置按钮(其他组件一样)的背景颜色
# # # green,也可以设置为16进制的事
# #
# # #.pack()，有left,top,right,bottom，四个方向，表示当前按钮靠哪一边
# #
# # # expand,是展开的意思，YES,NO表示是否允许按钮在窗口大小调整时自动扩展按钮的大小，要结合fill使用
# # #fill，填充的意思，X,Y,BOTH,x表示水平方向，Y表示竖直方向，BOTH是两个方向
# # # 都允许，NO当然表示都不允许了
# #
# # # anchor，是锚点，表示磁力粘贴到哪，有E东，S南，W西，N背以及两两结合的参数
# #
# # 使用grid进行布局
#
#
# import tkinter as tk
#
# root = tk.Tk()
#
# tk.Label(root,text="账号：").grid(row=0,sticky='W')
# tk.Entry(root).grid(row=0,column=1,stick='E')
# tk.Label(root,text="密码：”").grid(row=1,sticky='w')
# tk.Entry(root).grid(row=1,column=1,sticky='E')
# tk.Button(root,text="登录").grid(row=2,column=1,sticky="E")
# root.mainloop()
#
# # grid布局相对直观容易使用，就是网格和表格化，
# # sticky参数跟anchor参数类似，也是东西南北磁力媳妇放置组件的相对维护之
# # Entry是tkinter中的一个常用组件，用于输入框组件
#
#
#
# 总结：在tkinter中有三种布局方式：
# 1. pack布局：不用设置，直接使用pack函数即可
# 2. grid布局：grid即为网格，它可以把界面设置为几行几列的
# 网格，我们再网格里插入我们想要的元素。
# 这种布局的好处是不管我们怎么拖动窗口，相对位置是不会变的
#
# 3.place布局：它直接使用死板的位置来布局，这样做的做大问题在于我们向窗口
# 添加一个新部件时，又得重新测一遍数据，且我们不能随便地变大或缩小窗口

# get()函数获得Entry中用户输入的内容，使用弹窗提示消息


import tkinter as tk

from tkinter.messagebox import *

root =tk.Tk()
root.title("登录")
def login():
    s1 = ent1.get()
    s2 = ent2.get()
    if s1 =="zxh" and s2 =="123":
        showinfo("祝贺","登录成功！")
    else:
        showerror("警告","账号或密码错误！")
        ent1.delete(0,len(s1))
        ent2.delete(0,len(s2))
tk.Label(root,text="账号：").grid(row=0,sticky="W")
ent1=tk.Entry(root)
ent1.grid(row=0,column=1,sticky="E")
tk.Label(root,text="密码：").grid(row=1,sticky="W")
ent2= tk.Entry(root)
ent2.grid(row=1,column=1,sticky="E")
tk.Button(root,text="登录",command=login).grid(row=2,column=1,sticky="E")
root.mainloop()

# get()方法获得Entry输入框的内容，showinfo和showerror弹窗
#
