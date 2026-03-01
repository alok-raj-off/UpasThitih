import customtkinter as ctk

root = ctk.CTk()
root.title("Prachin_Yantar_for_Vidhyarthi_Upasthith")
root.geometry("1200x700")

# global and main variables
total_Student = 40
total_calsses_till_now = 10
today_present = 38
weakely_data = [("Mon" , 0.7), ("Tue",0.2), ("wed",0.9),("thu",0.8),("fri",0.4),("Sat",0.3),("sun",0.6)]

#clearing the contenttstststs
def lear_content(wrapper):
    for widget in wrapper.winfo_children():
        widget.destroy()

def homePage(parentFrm):
    right_Lable = ctk.CTkLabel(parentFrm,text="Welcome to Prachin Yantar",font=("Areal",35,"bold"),text_color="black")
    right_Lable.pack(pady=10)
    right_Lable2 = ctk.CTkLabel(parentFrm,text="place where you organise student attendence and track each oone of them , NO ESCAPE ",font=("Areal",16),text_color="grey")
    right_Lable2.pack(pady=0)

  # the three inner cards for total and stuudents genral record
    main_info_box = ctk.CTkFrame(parentFrm, width=900, height=200, corner_radius=10,fg_color="transparent")
    main_info_box.pack(pady=40)
    #card 1
    card1 = ctk.CTkFrame(main_info_box, width=250, height=130, corner_radius=10,fg_color="#F0F0F0")
    card1.pack(side="left",padx=20)
    card1.pack_propagate(False)
    c1label = ctk.CTkLabel(card1,text="Total Students ",text_color="grey")
    c1label.pack(padx=10,pady=6)
    c1labe2 = ctk.CTkLabel(card1,text=f"{total_Student}",text_color="grey",font=("Areal",40,"bold"))
    c1labe2.pack(padx=10,pady=6)

    #card 2
    card2 = ctk.CTkFrame(main_info_box, width=250, height=130, corner_radius=10,fg_color="#F0F0F0")
    card2.pack(side="left",padx=20)
    card2.pack_propagate(False)
    c2label = ctk.CTkLabel(card2,text="total calsses till now ",text_color="grey")
    c2label.pack(padx=10,pady=6)
    c2labe2 = ctk.CTkLabel(card2,text=f"{total_calsses_till_now}",text_color="grey",font=("Areal",40,"bold"))
    c2labe2.pack(padx=10,pady=6)

    #card 3
    card3 = ctk.CTkFrame(main_info_box, width=250, height=130, corner_radius=10,fg_color="#F0F0F0")
    card3.pack(side="left",padx=20)
    card3.pack_propagate(False)
    c3label = ctk.CTkLabel(card3,text="today present  ",text_color="grey")
    c3label.pack(padx=10,pady=6)
    c3labe2 = ctk.CTkLabel(card3,text=f"{today_present}",text_color="grey",font=("Areal",40,"bold"))
    c3labe2.pack(padx=10,pady=6)
    

    # container to hold the graphs
    graphCont = ctk.CTkFrame(parentFrm,width=900,height=380,fg_color="transparent")
    graphCont.pack()

    #adding the graphsss why is this fells like majdurriiiiiiiiii
    for weak ,valuse in weakely_data:
        column = ctk.CTkFrame(graphCont,width=50,height=380,fg_color="transparent")
        column.pack(side="left",padx=30)
        column.pack_propagate(False)
        currentColor = "#FF7D7D" if (valuse < 0.5) else "#2ECC71"
        bar = ctk.CTkProgressBar(column,width=50,orientation="vertical",height=340,fg_color="#E1E6E5",progress_color=f"{currentColor}",corner_radius=0)
        bar.set(valuse)
        bar.pack()

        labels = ctk.CTkLabel(column,text=f"{weak}",text_color="black")
        labels.pack(side="bottom")

# def students(parent)

# creating sidebar and its label 
sidebar = ctk.CTkFrame(root, width=200, corner_radius=0,fg_color="#222831")
sidebar.pack(side="left",fill="y")
sidebar.pack_propagate(False)
pannel = ctk.CTkLabel(sidebar,text="Panel",font=("Areal",20,"bold"),text_color="white")
pannel.pack(pady=10)

#right side content area
rghtCont =  ctk.CTkFrame(root,corner_radius=0,fg_color="#D3DAD9")
rghtCont.pack(side="right",fill="both",expand=True)

sidebar_frame = ctk.CTkFrame(sidebar,width=200,height=500,fg_color="transparent")
sidebar_frame.pack()

# butoons for sidebar
home = ctk.CTkButton(sidebar_frame,text="Home",width=180,font=("Areal",18),fg_color="#222831",anchor="w",command=lear_content(rghtCont))
home.pack(pady=6)
Student = ctk.CTkButton(sidebar_frame,text="Students",width=180,font=("Areal",18),fg_color="#222831",anchor="w")
Student.pack(pady=6)
Attendence = ctk.CTkButton(sidebar_frame,text="Attendence",width=180,font=("Areal",18),fg_color="#222831",anchor="w")
Attendence.pack(pady=6)
Teams = ctk.CTkButton(sidebar_frame,text="Teams",width=180,font=("Areal",18),fg_color="#222831",anchor="w")
Teams.pack(pady=6)



homePage(rghtCont)

root.mainloop()