
# 🏋️‍♂️ Sistema de Gerenciamento de Alunos - Academia

Este projeto é uma aplicação em Python para gerenciar alunos de uma academia. O sistema permite controlar informações de alunos, pagamentos e gerar relatórios simples via terminal.

---

## 📋 Funcionalidades

- Cadastro e listagem de alunos
- Registro de pagamentos
- Identificação de inadimplentes
- Geração de relatórios `.txt`
- Interface em terminal

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute o sistema com o comando abaixo:

```bash
python código_principal_1.py
```

---

## 🧠 Diagrama Simples de Funcionamento

```text
[Usuário no Terminal]
        │
        ▼
[interface.py] → Menu com opções
        │
        ├──▶ [aluno.py] - Cadastra/lista alunos
        │
        ├──▶ [pagamento.py] - Marca pagamento
        │
        ├──▶ [pagamento_pendente.py] - Lista inadimplentes
        │
        └──▶ [gerar_arquivo.py] - Gera relatórios .txt
```

---

## 📁 Estrutura dos Arquivos

- `aluno.py` – Classe `Aluno` com dados e métodos de manipulação
- `pagamento.py` – Funções de controle de pagamento
- `pagamento_pendente.py` – Relatório de alunos com mensalidade atrasada
- `gerar_arquivo.py` – Geração de arquivos `.txt` com dados dos alunos
- `interface.py` – Interface com menus e interações
- `código_principal_1.py` – Script que integra tudo e inicia o sistema

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙋‍♂️ Autor

Pedro Duarte – [@Pedrao01](https://github.com/Pedrao01)
