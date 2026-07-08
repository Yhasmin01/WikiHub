# Prompt para preencher templates com IA

Use este prompt em qualquer IA (Gemini, ChatGPT, Claude). Cole o template vazio correspondente junto e substitua o contexto de exemplo pelo seu.

---

```
Atue como um redator técnico. Preencha o template Markdown abaixo com as
informações que vou te dar. Regras:
- Mantenha o bloco de front matter (entre as linhas ---) intacto na estrutura,
  só preenchendo os valores.
- Não invente informação que eu não passei — se algum campo não se aplica,
  escreva "não informado".
- Use kebab-case sem acento pra sugerir um nome de arquivo no final da resposta.
- Devolva só o Markdown final, sem explicações antes ou depois.

TEMPLATE:
[cole aqui o conteúdo de TEMPLATE_INICIATIVA.md, TEMPLATE_RECURSO.md ou TEMPLATE_TIME.md]

CONTEXTO DO MEU ITEM:
[descreva em texto livre: o que é, time responsável, tecnologias, status,
links relevantes — quanto mais contexto, melhor o preenchimento]
```

---

**Exemplo de uso real:**

> CONTEXTO DO MEU ITEM: Estamos criando uma automação de relatórios em Python
> que roda todo domingo às 6h, lê dados do PostgreSQL e manda um PDF por e-mail
> pro time comercial. O repositório oficial é gitlab.com/empresa/relatorio-auto,
> o time responsável é Dados, status é em-andamento, e o responsável é a Maria.

A IA devolve o `.md` pronto. A pessoa só precisa criar o arquivo no GitHub ("Add file → Create new file" ou editor github.dev), colar o resultado, salvar com o nome sugerido na pasta certa (`iniciativas/`, `recursos/`, `times/` ou `outros/<subcategoria>/`), e — se tiver como — rodar `python3 scripts/gerar_indice.py` antes do commit.
