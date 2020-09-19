######################################################################
#                      App envoyeur de gmail                         #
#                      cree par Bras Tsg                           #
#                          19/09/2020                                #
######################################################################

import tkinter,email_sender
import webbrowser

def auto():
    webbrowser.open("myaccount.google.com/lesssecureapps")

def mise_a_jour(*args):
        msg.set(msg_entre.get())
def envoie():
    s=sender.get()
    r=recv.get()
    email_receiver=r.strip(" ")
    le_email_sender=s[:s.find(" ")].strip(" ")
    password=s[s.find(" "):].strip(" ")
    _mesg=message.get()
    accuse=email_sender.send(le_email_sender,password,_mesg,email_receiver)
    msg.set(accuse)
bg="light gray"
#le main
fenetre_principale=tkinter.Tk()
fenetre_principale.geometry("800x450")
fenetre_principale.minsize(width=600,height=400)
fenetre_principale.title("Email_sender 0.01")
fenetre_principale.configure(bg=bg)

        
    #frame
frame_principale=tkinter.Frame(fenetre_principale,bg=bg)
frame_haut=tkinter.LabelFrame(frame_principale,bg=bg)
frame_centre=tkinter.LabelFrame(frame_principale,bg=bg)
frame_bras=tkinter.LabelFrame(frame_principale,bg=bg)
frame_2bas=tkinter.Frame(frame_bras,bg=bg)
frame_3bas=tkinter.Frame(frame_bras,bg=bg)
        #information de champ de saisie
frame_message=tkinter.Label(frame_centre,bg=bg)
frame_recv=tkinter.Label(frame_centre,bg=bg)
frame_send=tkinter.Label(frame_centre,bg=bg)
frame_grand_msg=tkinter.Label(frame_centre,bg=bg)

    #variable
msg=tkinter.StringVar()
msg_entre=tkinter.StringVar()
        #update
msg_entre.trace("w",mise_a_jour)


    #texte
titre=tkinter.Label(frame_haut,text="EMAIL-SENDER",fg="gray",font="robot 42 bold",bg=bg,justify="center")
sous_titre=tkinter.Label(frame_2bas,text="Version : 0.01 Beta \nCree le: 19/09/2020\nPar: BraS TsG ",fg="gray",font="robot 10",bg=bg,justify="left")
titre_message=tkinter.Label(frame_message,fg="gray",font="robot 8 bold",text=" le message a envoyer :".upper(),bg=bg)
titre_recv=tkinter.Label(frame_recv,fg="gray",font="robot 8 bold",text="            Email recepteur :".upper(),bg=bg)
titre_send=tkinter.Label(frame_send,fg="gray",font="robot 8 bold",text="Email envoyeur et Mdp :".upper(),bg=bg)
titre_autoriser=tkinter.Label(frame_3bas,bg=bg,fg="gray",font="robot 8 bold",text="Pour utiliser cette app il faut l'autoriser")
    #bouton
bouton_envoyer=tkinter.Button(frame_grand_msg,text="Envoyer",width=14,height=4,command=envoie)
bout_oui=tkinter.Button(frame_3bas,text="autoriser",command=auto)
    #champe de saisie
message=tkinter.Entry(frame_message,width=50,textvariable=msg_entre)
sender=tkinter.Entry(frame_send,width=50)
recv=tkinter.Entry(frame_recv,width=50)
    #le afficheur message
grd_msg=tkinter.Message(frame_grand_msg,bg="light yellow",relief="groove",textvariable=msg)



    #placement
        #frame

frame_principale.pack(fill="both",expand=1)
frame_haut.pack(fill="x")
frame_centre.pack(expand=1,fill="both")
frame_bras.pack(expand=0,fill="x")
frame_recv.pack(side="top",pady=10)
frame_send.pack(side="top",pady=10)
frame_message.pack(side="top",pady=10)
frame_grand_msg.pack(side="top",fill="both",expand=1)
frame_2bas.pack(side="left",fill="both",expand=1)
frame_3bas.pack(side="left",fill="both",expand=1)
        #texte
titre.pack()
sous_titre.pack(side="left",fill="x")
titre_message.pack(side="left")
titre_recv.pack(side="left")
titre_send.pack(side="left")

        #saisie
message.pack(side="left",padx=16)
recv.pack(side="left",padx=16)
sender.pack(side="left",padx=16)    
        
        #grand message
grd_msg.pack(side="left",fill="both",expand=1,padx=18,pady=8)

        #bouton
bouton_envoyer.pack(side="left",padx=10)
bout_oui.pack(side="right",padx=8)
#titre bouton oui
titre_autoriser.pack(side="right")
    #le boucle principale
fenetre_principale.mainloop()

