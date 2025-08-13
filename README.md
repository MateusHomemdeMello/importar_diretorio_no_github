📦 Exportador de Arquivos .py para GitHub com QtPy

Este script permite exportar automaticamente todos os arquivos .py de um diretório e suas subpastas para um repositório GitHub já existente, preservando a estrutura original das pastas.
A interface gráfica é feita com QtPy, permitindo selecionar facilmente a pasta de origem, o link completo do repositório e o token pessoal de acesso (PAT) do GitHub.

🚀 Funcionalidades

Seleção gráfica da pasta a ser exportada.

Preservação da estrutura original de pastas e subpastas.

Filtragem para enviar somente arquivos .py.

Integração com GitHub via Personal Access Token (PAT).

Compatível com Windows (e outros SOs com Git instalado).

Interface amigável usando QtPy.

📋 Pré-requisitos

Antes de executar o script, verifique se você possui:

Python 3.8+ instalado.

Git instalado e configurado no sistema.

Biblioteca QtPy instalada:

pip install qtpy


Um repositório GitHub já criado (link completo, exemplo:

https://github.com/usuario/repositorio.git


Um Personal Access Token (PAT) do GitHub, com permissão de leitura e escrita em repositórios.

🛠️ Como usar

Clone ou baixe este script para seu computador.

Abra o terminal e execute:

python exportar_py_para_github.py


Na interface:

Clique em Selecionar Pasta e escolha a pasta raiz do projeto.

Insira o link completo do repositório GitHub.

Insira o token pessoal de acesso.

Clique em Exportar para GitHub.

Aguarde a mensagem de sucesso.

⚙️ O que o script faz

Percorre a pasta selecionada e copia somente arquivos .py para uma pasta temporária.

Preserva toda a estrutura de subpastas.

Inicializa um repositório Git temporário.

Adiciona o remote do GitHub com autenticação via token.

Realiza commit e push para a branch main.

Remove a pasta temporária após o envio.

📌 Observações

O script força o push (--force) para a branch main. Isso pode sobrescrever commits anteriores.

Caso queira apenas adicionar arquivos sem sobrescrever histórico, o script pode ser adaptado.

Somente arquivos .py são enviados — outros tipos de arquivos serão ignorados.

Por questões de segurança, o token não é salvo no sistema.

📄 Licença

Este projeto é distribuído sob a licença MIT.
Sinta-se livre para modificar e adaptar conforme necessário.
