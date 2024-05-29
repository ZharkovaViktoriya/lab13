from tkinter import *
import requests

def z1():
    root=Tk()
    root['bg']='#98f5ff'
    root.title('Прогноз погоды')
    root.geometry('600x500')
    root.resizable(width=False, height=False)

    def get_minmax_temp():
        city=cityField.get()
        key='4bcbb12ee0abef005cedbd1937955156'
        url='http://api.openweathermap.org/data/2.5/weather'
        params={'APPID':key, 'q':city, 'units':'metric'}
        result=requests.get(url, params=params)
        temp=result.json()
        info1['text']=f'{temp["main"]['temp_max']}'
        info2['text'] = f'{temp["main"]['temp_min']}'

    frame = Frame(root, bg='#ff69b4', bd=5)
    frame.place(relx=0.10, rely=0.10, relwidth=0.8,relheight=0.8)
    title = Label(frame, text='Прогноз погоды', font=40)
    title.pack()

    frame_top = Frame(root, bg='#ffb700', bd=5)
    frame_top.place(relx=0.15, rely=0.20, relwidth=0.7, relheight=0.3)

    frame_bottom = Frame(root, bg='#ffb700', bd=5)
    frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.2)

    cityField = Entry(frame_top, bg='white', font=30)
    cityField.place(relx=0.15, rely=0.30, relwidth=0.7, relheight=0.2)

    btn = Button(frame_top, text='Узнать прогноз погоды', command=get_minmax_temp)
    btn.place(relx=0.25, rely=0.55, relwidth=0.5, relheight=0.3)

    info1 = Label(frame_bottom, text='Максимальная температура', bg='#ffb700', font=40)
    info1.pack()
    info2 = Label(frame_bottom, text='Минимальная температура', bg='#ffb700', font=40)
    info2.pack()

    root.mainloop()
def z2():
    root=Tk()
    root['bg']='#98f5ff'
    root.title('Генерация рандомных пользователей')
    root.geometry('600x500')
    root.resizable(width=False, height=False)

    def get_random_user():
        response = requests.get("https://randomuser.me/api/")
        data = response.json()
        user_data = data["results"][0]
        info1['text']=(f"Name: {user_data['name']['first']} {user_data['name']['last']}")
        info2['text']=(f"Email: {user_data['email']}")
        info3['text']=(f"Phone: {user_data['phone']}")

    frame = Frame(root, bg='#ff69b4', bd=5)
    frame.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=0.8)

    info1=Label(frame,font=40)
    info1.pack()

    info2=Label(frame, font=40)
    info2.pack()

    info3=Label(frame, font=40)
    info3.pack()

    btn=Button(frame, text="Сгенерировать пользователя", command=get_random_user)
    btn.place(relx=0.10, rely=0.50, relwidth=0.8, relheight=0.2)

    root.mainloop()

z1()
z2()

