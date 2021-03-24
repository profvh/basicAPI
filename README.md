# Basic REST API 
### Feito em python flask

### Instalação

```sh
$ sudo apt-get update && sudo apt-get install python3-dev python3-virtualenv python3-pip
```

#### Virtual env

```sh
$ virtualenv venv ./venv -p python3
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r reqs.txt
```

#### Rodando
#### Virtual env

```sh
$ python manage.py runserver -h 0.0.0.0 -p 5000
```

Uma saída parecida com essa abaixo indica que está tudo rodando OK:

````
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
````

Basta abrir o endereço no browser.

### Serviços disponíveis

````
http://localhost:5000/events GET
Chamada CURL
curl --request GET --url http://localhost:5000/events
Resposta:
{
  "events": [
    {
      "data": "24/03/2021",
      "titulo": "Semana acadêmica"
    },
    {
      "data": "30/08/2021",
      "titulo": "Semana da computação"
    },
    {
      "data": "30/08/2022",
      "titulo": "Maratona de programação"
    }
  ]
}
````

````
http://localhost:5000/events POST
Chamada CURL
curl --request POST --url http://localhost:5000/events --header 'Content-Type: application/json' --data '{"titulo":"Novo Evento Cadastrado","data":"10/10/2021"}'
````