email = input("Introduce tu dirección de email: ")

'''if email.count("@") != 1 or email.find("@") == 0 or email.find("@") == len(email) - 1:
        print("La dirección de email es incorrecta")
else:
    print("La dirección de email es correcta")'''

#---- SI ES VERDAD ----------------------------------- CONDICION --------------------------------------------- SI ES FALSO ----------
print("Email incorrecto" if email.count("@") != 1 or email.find("@") == 0 or email.find("@") == len(email) - 1 else "Email correcto")
