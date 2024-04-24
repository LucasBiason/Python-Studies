import requests

class UserService:

    URL = 'https://gen-net.herokuapp.com/api/users/'

    @staticmethod
    def get_all():
        response = requests.get(UserService.URL)
        if response.status_code == 200:
            return [ UserService(**u) for u in response.json() ]
        return []
    
    @staticmethod
    def get(userid):
        response = requests.get('{}{}'.format(
            UserService.URL, userid
        ))
        if response.status_code == 200:
            return UserService(**response.json())
        return None

    @staticmethod
    def create(name, email, password):
        response = requests.post(UserService.URL, {
            "name": name,
            "email": email,
            "password": password
        })
        returns = response.content
        if response.status_code == 200:
            print("Seu código é:", returns.get('id'))
        else:
            print("Ocorreu um problema:", returns.message)
        return response.json()
    
if __name__ == '__main__':
    #response = requests.get(UserService.URL)
    #print(response.json())
    
    name, email, passoword = '', '', ''

    while(True):
        name = input('Insira seu nome:')
        if name:
            break
        
    while(True):
        email = input('Insira seu e-mail:')
        if name:
            break
    
    while(True):
        password = input('Insira sua senha:')
        if name:
            break
    
    if all([name, email, password]):
        response = requests.post('https://gen-net.herokuapp.com/api/users/', {
           "name": name,
            "email": email,
            "password": password
        })
        returns = response.content
        if response.status_code == 200:
            print("Seu código é:", returns.get('id'))
        else:
            print("Ocorreu um problema:", returns.message)
    else:
        print("Dados inválidos....")