 # self.bg_img=Image.open(r"images\dbg10.jfif")
        # self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        # self.bg_img=ImageTk.PhotoImage(self.bg_img)   # again open image bcz it resize image during runtime and 
        #                                               #  dont define (file='path') coz we dont know the path of resized image
        # self.lbl_bg=Label(self.root,image=self.bg_img).place(x=220, y=180 ,width=920,height=350)