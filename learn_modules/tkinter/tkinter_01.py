import tkinter as tk

# 建立窗口
window = tk.Tk()

# 窗口的名称
window.title('My firt window')

# 窗口大小
window.geometry('500x300')

# 写一个标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()
 
# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = True
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('Miss')


# 按钮标签
b = tk.Button(window, text='My First Button', width=20, height=2, command=hit_me )
b.pack()

window.mainloop()