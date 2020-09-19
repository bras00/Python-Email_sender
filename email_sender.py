######################################################################
#                      App envoyeur de gmail                         #
#                      cree par Bras Vador                           #
#                          19/09/2020                                #
######################################################################


import smtplib, ssl

def send(sender,passw,msg,receiver):
    mms=f"""\
    Subject: Message

    {msg}."""
    try:
        cont=ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=cont) as serveur:
            serveur.login(sender,passw)
            serveur.sendmail(sender,receiver,mms)
            return "message envoyer"

    except:
        return "erreur de l'envoie"

