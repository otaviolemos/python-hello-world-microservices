# Python Hello World Microservices (clonado de [To-Do Application](https://github.com/h4xr/todo))
### Como rodar o exemplo

1. Clone o código na sua máquina executando `git clone https://github.com/otaviolemos/python-hello-world-microservices.git todo`
2. Agora, entre no diretório que foi criado com o passo anterior `cd <path_to_directory>`
3. O próximo passo é configurar um ambiente virtual para o projeto (isso vai nos ajudar a manter as dependências isoladas do resto do sistema). Para criar o ambiente virtual, podemos executar o seguinte comando `virtualenv venv`. Isso criará um ambiente virtual chamado *venv* dentro da pasta do projeto.
4. O próximo passo é ativar o ambiente virtual. Para isso, execute `source venv/bin/activate`
5. Depois precisamos baixar as dependências necessárias para executar o exemplo. As dependências estão listadas em *requirements.txt*. A ferramente pip pode ajudá-lo a instalar as dependências requeridas. Execute o seguinte comando para configurar as dependências: `pip install -r requirements.txt`
6. Agora temos todas as dependências configuradas no sistema. É hora de rodar nossos microsserviços. Para isso, execute os seguintes comandos, um em cada terminal, para que você possa ter controle de cada um dos serviços: `python services/users/users.py` e `python services/todo/todo.py`. Quando quiser *matar* o serviço, basta digitar CTRL+C.
7. Você pode verificar se os serviços estão rodando corretamente visitando `http://localhost:5000` no seu browser.
