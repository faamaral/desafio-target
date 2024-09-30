# Desafio Target

## Resolução das atividades 1 e 2 do desafio

A rosulução das atividades 1 e 2 do desafio foi implementada através de uma aplicação web baseada no microframework flask e está disponivel [Aqui](https://desafio-target.onrender.com/).

## Como Executar o Projeto Localmente

### Pré-requisitos

- **Python 3.x** instalado.
- **Pip** (gerenciador de pacotes do Python).
- Virtualenv (recomendado para criação de ambiente virtual).

### Passos para execução local

1. Clone o repositório:

   ```shell
   git clone https://github.com/seu-usuario/projeto-flask-desafio.git
   cd projeto-flask-desafio
   ```

2. Crie um ambiente virtual e ative-o:

    ```shell
        python -m venv venv
        source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```shell
        pip install -r requirements.txt
    ```

4. Configure variaveis de ambiente:

    ```shell
        export FLASK_ENV=development
        export FLASK_DEBUG=True
        export FLASK_APP=app
    ```

5. Execute a aplicação:

    ```shell
        flask run
    ```

    executando com gunicorn

    ```shell
        gunicorn -w 4 'app:app'
    ```