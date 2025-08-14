# welcome-message
### Descrição

Projeto em Python que busca contatos cadastrados no Supabase e envia mensagens personalizadas via Z-API.

Cada mensagem é enviada no formato específico:

```
$ Olá {{name}}, tudo bem com você?
```

## Requisitos

- Python 3.7 ou superior (3.9 ou superior recomendado) instalado
- Python-pip mínimo recomendado: 19.0
- Conta no Supabase e tabela contacts criada
- Conta na Z-API para envio de mensagens

## Instalação

### 1. Clone o projeto
```
$ git clone https://github.com/BrunoCTb/welcome-message
```

### 2. Crie o Ambiente virtual do python (venv)

```
$ python -m venv /path/to/new/virtual/environment
```

ex: "python -m venv ./venv" (coloque a pasta e o "apelido" do venv)

### 3. Ative o Ambiente virtual

#### Linux/Mac OS

```
$ source venv/bin/activate
```


#### Windows

cmd
```
$ .\venv\Scripts\activate.bat
```
powershell
```
$ .\venv\Scripts\activate.ps1
```

no windows pode ocorrer algum tipo de erro (principalmente no vscode com powershell) que pode ser resolvido na [documentação oficial](https://docs.python.org/3/library/venv.html).

### 4. Instale as dependências
```
$ pip install -r requirements.txt
```

Pode checar se tudo ocorreu corretamente

```
$ pip freeze
```

## Funcionamento

### Escanear QR code do Z-API

Cada usuário que for rodar o projeto precisa criar a própria instância Z-API e escanear o QR code.
A instância do seu projeto não será compartilhável para envio de mensagens de terceiros.

### No Supabese crie a tabela com o nome *contacts* com os seguintes campos:

| Name | Type | Default Value | Primary Key | Config |
| -- | -- | -- | -- | -- |
| id | int8 | | true | |
| name | varchar | | |
| phone_number | varchar | | | IsUnique |
| created_at | timestamp | now() | |


### Exemplo de dados fictícios:

| name |  phone_number |
| --- | --- |
| João | 5511912345678 |
| Maria | 5511912345679 |
|Pedro | 5511912345680 |

### Crie um arquivo .env na raiz do projeto:

```
SUPABASE_URL="https://your-supabase-url.supabase.co"

# secret api key
SUPABASE_KEY=""

ZAPI_INSTANCE_ID=""
ZAPI_INSTANCE_TOKEN=""
ZAPI_CLIENT_TOKEN=""
```

## Para rodar
```
$ python main.py
```

- O script buscará até 3 contatos na tabela do Supabase e enviará a mensagem personalizada para cada um.

- Caso não haja contatos, apenas printará uma mensagem informando.