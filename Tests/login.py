user_info = {
    "user1234pasc": "1112224jgt",
    "elwdfhue": "1skk23¿?¿"
}

def correct_login(given_user: str, given_password: str) -> bool:
    return user_info[given_user] == given_password

def login(user: str, password:str):
    result = False
    try:
        if correct_login(user, password):
            result_msg = "El inicio de sesión finalizó correctamente."
            result = True
        else:
            result_msg = "La contraseña es incorrecta."
    except(KeyError):
        result_msg = f'El usuario "{user}" no existe.'
    print(result_msg)
    return result

if __name__=="__main__":

    given_user = input("Usuario: ")
    given_password = input("Contraseña: ")
    login(given_user, given_password)
