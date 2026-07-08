# Estrutura do Repositório Central de Conhecimento

Este documento explica a arquitetura completa. Leia antes de criar qualquer arquivo.

## 1. Árvore de pastas

```
/
├── README.md                  ← Índice geral (AUTOGERADO, não editar manualmente)
├── ESTRUTURA_REPOSITORIO.md   ← Este arquivo
├── CONTRIBUTING.md            ← Regras de governança
├── templates/
│   ├── TEMPLATE_INICIATIVA.md
│   ├── TEMPLATE_RECURSO.md
│   └── TEMPLATE_TIME.md
├── scripts/
│   └── gerar_indice.py        ← Script que gera o README.md
├── iniciativas/
│   └── <slug>.md              ← Um arquivo por iniciativa/projeto
├── recursos/
│   └── <slug>.md              ← Um arquivo por recurso compartilhado (ferramenta, doc, dataset...)
├── times/
│   └── <slug>.md              ← Uma página por time
└── outros/
    └── <subcategoria-livre>/
        └── <slug>.md          ← Única pasta onde subpastas novas são permitidas
```

**Por que "outros" existe:** as 3 categorias fixas (`iniciativas`, `recursos`, `times`) cobrem os casos previstos hoje. Qualquer coisa que não se encaixe vai para `outros/<nome-da-subcategoria>/`, criando a subpasta na hora. Isso evita duas coisas ruins: (a) gente criando pastas soltas na raiz do repo sem padrão, e (b) travar alguém que tem uma necessidade legítima não prevista.

## 2. Convenção de nomes de arquivo

- kebab-case, sem acento, sem espaço: `automacao-relatorios-dados.md`
- Sem prefixo de data ou de time no nome do arquivo — essa informação vai no front matter (seção 3), não no nome.
- Um arquivo = um item. Não agrupar múltiplas iniciativas num único `.md`.

## 3. Front matter (o que faz o índice funcionar)

Todo arquivo dentro de `iniciativas/`, `recursos/`, `times/` e `outros/` **precisa começar** com um bloco de metadados entre `---`, assim:

```
---
tipo: iniciativa
titulo: Automação de Relatórios de Dados
time_responsavel: Dados
status: em-andamento
data_criacao: 2026-07-07
---
```

Isso é o que permite ao `scripts/gerar_indice.py` varrer o repositório e montar o `README.md` automaticamente, sem precisar de CI/CD — é um script Python puro (sem bibliotecas externas) que qualquer pessoa roda localmente antes de commitar.

Os campos exatos de cada tipo estão em `templates/`.

## 4. Fluxo de trabalho (governança)

| Ação | Como fazer | Precisa de PR? |
|---|---|---|
| Adicionar um item novo | Copiar o template, preencher, criar arquivo via interface web do GitHub ou editor github.dev (tecla `.`), commit direto na main | **Não** |
| Editar um item que já existe (seu ou de outro time) | Abrir Pull Request | **Sim** |
| Apagar um item | Abrir Pull Request | **Sim** |
| Atualizar o README.md | Rodar `scripts/gerar_indice.py` e commitar o resultado junto com o novo arquivo | Não (é regeneração automática, não edição de conteúdo) |

⚠️ **Limitação técnica honesta:** o GitHub não bloqueia tecnicamente "editar" e libera "criar" — quem tem permissão de push pode fazer as duas coisas direto na main. A tabela acima é uma regra de time documentada aqui e reforçada no `CONTRIBUTING.md`, não uma trava de sistema. Se no futuro isso virar problema real (gente editando conteúdo alheio sem PR), aí sim vale configurar proteção de branch mais restritiva — mas isso tornaria a adição de itens novos também mais lenta, então por ora fica no acordo de time.

## 5. Passo a passo pra começar

1. Suba este pacote de arquivos pro repositório GitHub.
2. Adicione os marcadores `<!-- INDEX:START -->` e `<!-- INDEX:END -->` no `README.md` (já vem pronto no arquivo que estou te entregando).
3. Divulgue pros times: onde ficam os templates, a convenção de front matter, e a regra de PR pra edição.
4. Toda vez que alguém adicionar um arquivo novo, essa pessoa (ou você) roda `python3 scripts/gerar_indice.py` antes do commit final.
