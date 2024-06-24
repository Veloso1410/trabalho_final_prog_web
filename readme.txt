VHL ARMAS DE FOGO API

1. Introdução

Este é o README do projeto de API web VHL Armas de Fogo, desenvolvido para a disciplina de Programação Web. 
A API é uma ferramenta para catalogar e armazenar dados de armas de fogo.
Nele, há informações satíricas sobre a empresa fictícia VHL e suas atividades. 
Este projeto foi desenvolvido para fins acadêmicos por estudantes dedicados de Análise e Desenvolvimento de Sistemas.

2. Funcionalidades:
● Cadastro de Armas: Permite o registro de novas armas no sistema, incluindo detalhes como modelo, fabricante e calibre.
● Atualização de Dados: Permite a atualização das informações das armas já cadastradas.
● Remoção de Armas: Permite a exclusão de registros de armas do sistema.
● Exibição de mapa: Exibe um mapa com os principais pontos de compra.
● Conexão com Banco de Dados Externo: A aplicação se conecta a um banco de dados PostgreSQL para armazenamento persistente dos dados.
● Navegação Estruturada: Suporte para navegação através de múltiplas ramificações partindo de uma mesma raiz (home), facilitando a organização e acesso hierárquico às diferentes seções da aplicação.

3. Requisitos
● Python 3.8+: Linguagem de programação utilizada.
● Django 3.2: Framework web para desenvolvimento da API.
● PostgreSQL: Banco de dados utilizado para armazenamento das informações.
● Visual Studio Code: Editor de códigos para auxiliar na configuração do ambiente.

4. Instalação
4.1 Requisitos pré-requisitos:
● Python 3.8+: Instale o Python a partir do site (https://www.python.org/downloads/).
● PostgreSQL: Instale o PostgreSQL a partir do site (https://www.postgresql.org/download/).
● Visual Studio Code: Instale o Visual Sudio Code a partir do site (https://code.visualstudio.com/download).

4.2 Instalação da API:
4.2.1. Clone o repositório:

    git clone: https://github.com/Veloso1410/trabalho_final_prog_web.git

4.2.2. Navegue até o diretório do projeto:

    cd trabalho_final_prog_web
 
4.2.3. Crie um ambiente virtual:

    python -m venv venv

4.2.4. Ative o ambiente virtual:
    - No Windows:
        
        venv\Scripts\activate
        

4.2.5. Instale as dependências:
    
    pip install fastapi uvicorn sqlalchemy alembic asyncpg psycopg2
    
4.2.6. Configure o banco de dados PostgreSQL no arquivo `settings.py`:
    python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nome_do_banco',
            'USER': 'seu_usuario',
            'PASSWORD': 'sua_senha',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    
4.2.7. Configure o banco de dados PosgreSQL no SGBD:
    a. Abra o pgAdmin (PostgreSQL) na porta 5432;
    b. Crie uma tabela com o nome "armas".
    
4.2.8. Inicie o app:
    
    python -m main.py
    

4.3. Uso da API
4.3.1 Endpoints:
● /api/armas/: Endpoint para listar e criar armas.
● /api/armas/{id}/: Endpoint para visualizar, atualizar e deletar uma arma específica.

4.3.2. Parâmetros:
● id: Identificador único da arma.

4.3.3. Exemplos de uso:
- Listar armas:
    
    GET /api/armas/
    
- Criar uma nova arma:
    
    POST /api/armas/
    {
        "modelo": "CTT",
        "fabricante": "Taurus",
        "calibre": ".40"
    }
    
- Atualizar uma arma existente:
    
    PUT /api/armas/1/
    {
        "modelo": "24/7",
        "fabricante": "Taurus",
        "calibre": ".40"
    }
    
- Deletar uma arma:
    
    DELETE /api/armas/1/
    
5. Possíveis erros e soluções:
● Erro de Conexão com o Banco de Dados:
    - Descrição: A aplicação não consegue se conectar ao banco de dados PostgreSQL.
    - Solução: Verifique se o PostgreSQL está rodando e se as credenciais no arquivo `settings.py` estão corretas. Confira se as migrações foram aplicadas corretamente.

● Erro ao executar -m main.py:
- Caso ocorra erro relacionado ao UTF-8, considerar as instuções a seguir:
    No Windows: Acesse o Painel de Controle -> Região -> Administrativo -> Alterar localidade do sistema -> 
marcar o box Beta - Usar Unicode UTF-8 -> reiniciar a máquina.

6. Testes
● Teste de Cadastro: Verifica se uma nova arma pode ser cadastrada corretamente.
● Teste de Consulta: Verifica se a consulta de armas retorna os resultados esperados.
● Teste de Atualização: Verifica se a atualização de dados de uma arma funciona corretamente.
● Teste de Remoção: Verifica se uma arma pode ser removida do sistema.

7. Contribuições
● Vitor Veloso Beckenkamp (Desenvolvedor)
● Henrique Barros Brandão (Desenvolvedor)
● Lucas O.C. Drumond (Desenvolvedor)

8. Agradecimentos
● Ao Professor PhD Lucas dos Santos Althoff, pela presteza e dedicação na transmissão do conhecimento.
