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

### 2. Instale as dependências
```
$ pip install -r requirements.txt
```


## Funcionamento

### Escanear QR code do Z-API

Cada usuário que for rodar o projeto precisa criar a própria instância Z-API e escanear o QR code.
A instância do seu projeto não será compartilhável para envio de mensagens de terceiros.

### Crie a tabela no *Supabase* contacts com os seguintes campos:

| Name | Type | Default Value | Primary Key |
| -- | -- | -- | -- |
| id | int8 | | true |
| name | varchar | 
| phone_number | varchar | | |
| created_at | timestamp | now() |


### Exemplo de dados fictícios:

| name |  phone_number |
| --- | --- |
| João | 5511912345678 |
| Maria | 5511912345679 |
|Pedro | 5511912345680 |

### Crie um arquivo .env na raiz do projeto:

```
SUPABASE_URL=https://your-supabase-url.supabase.co
SUPABASE_KEY="
ZAPI_INSTANCE_ID= 
ZAPI_INSTANCE_TOKEN= 
ZAPI_CLIENT_TOKEN=
```

## Para rodar
```
$ python main.py
```

- O script buscará até 3 contatos na tabela do Supabase e enviará a mensagem personalizada para cada um.

- Caso não haja contatos, apenas printará uma mensagem informando.