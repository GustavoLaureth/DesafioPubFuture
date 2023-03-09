# DesafioPubFuture
 
# Como rodar a aplicação

- Crie uma pasta no Windows
- Aperte o botão direito e em Git Bash Here
- Executar os comandos: git init e git clone https://github.com/GustavoLaureth/DesafioPubFuture.git
- Entrar na pasta criada e abrir o Visual Studio Code
- Abrir o PowerShell do Windows como administrador
- Executar o comando: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
- Abrir o terminal do Visual Studio Code
- Executar o comando: python -m venv env
- Depois execute este comando: .\env\Scripts\Activate.ps1
- Agora vamos instalar todas as bibliotecas necessárias com o comando: pip install -r requirements.txt
- Agora devemos fazer as migrações do banco de dados: python manage.py makemigrations e python manage.py migrate
- Agora é so rodar a aplicação: python manage.py runserver

