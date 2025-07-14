# Que Gato Sou Eu? 🐱
Um projeto divertido e interativo que exibe uma imagem aleatória de gato a cada clique, utilizando uma API externa. Desenvolvido com **Flask**, **HTML**, **CSS** e **Python**, o principal objetivo deste projeto foi treinar o consumo de **APIs** e integrar dados externos em uma aplicação web.

---

## 🚀 Tecnologias Utilizadas

- Frontend:
HTML5: Estrutura da página web.
CSS3: Estilização da interface, garantindo um visual agradável e responsivo.

- Backend:
Python: Linguagem de programação para a lógica de negócio e consumo da API.
Flask: Microframework web para roteamento, renderização de templates e comunicação entre o frontend e a API externa.

- API Externa:
The Cat API: Utilizada para buscar imagens aleatórias de gatos.

---

## ✨ Recursos Principais
- Geração de Imagens Aleatórias: A cada recarregamento da página ou clique em um botão, uma nova imagem de gato é exibida.

- Consumo de API: Demonstração prática de como fazer requisições HTTP para uma API externa e processar seus retornos.

- Interface Simples e Intuitiva: Um design limpo que foca na imagem do gato e na interação do usuário.

- Design Responsivo: Adapta-se a diferentes tamanhos de tela, proporcionando uma boa experiência em dispositivos móveis e desktops.

---

## 💡 Propósito do Projeto
Este projeto foi desenvolvido com o objetivo de praticar e aprimorar as habilidades em:

- Consumo de APIs: Entender o processo de fazer requisições (GET) a APIs RESTful e manipular os dados retornados (JSON).

- Integração Frontend-Backend: Conectar a lógica Python (Flask) que consome a API com a interface HTML/CSS.

- Desenvolvimento Web com Flask: Utilizar o Flask para criar rotas, renderizar templates e gerenciar o fluxo da aplicação.

- Manipulação de Dados: Extrair informações relevantes de respostas de API para exibição na interface.

---

## 💻 Como Executar o Projeto
Para configurar e rodar o projeto em sua máquina local, siga estes passos:

1. Clone o repositório:

```Bash

git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Navegue até a pasta do projeto:

```Bash

cd nome-do-repositorio
```

3. Crie e ative um ambiente virtual:

```Bash

python -m venv venv
```
### No Windows:
.\venv\Scripts\activate
### No macOS/Linux:
source venv/bin/activate

4. Instale as dependências:

```Bash

pip install -r requirements.txt
```

5. Execute a aplicação Flask:

```Bash

python app.py
```

6. Acesse a aplicação:
Abra seu navegador e vá para http://127.0.0.1:5000/ (ou o endereço que o terminal indicar).

---

## 🛠️ Estrutura do Projeto
- app.py (ou main.py): Contém a lógica principal da aplicação Flask, as rotas e a função para consumir a API de gatos.

- templates/: Pasta com os arquivos HTML (index.html).

- static/: Pasta para arquivos estáticos como CSS (style.css).

- requirements.txt: Lista das dependências Python do projeto.

---

## 👨‍💻 Criador
Projeto desenvolvido por Richard de Oliveira Ribeiro
- Github: https://github.com/Richard15151
- Linkedin: https://www.linkedin.com/in/richard-oliveira-b30a10315/
