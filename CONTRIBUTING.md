# Como contribuir

## Regra de ouro
- **Adicionar item novo → commit direto na `main`.** Não precisa de Pull Request.
- **Editar ou apagar um item que já existe → Pull Request obrigatório**, mesmo que o item seja seu. Isso existe pra qualquer mudança em conteúdo já publicado passar por um segundo par de olhos.

> Nota: o GitHub não impõe essa distinção tecnicamente — é um acordo de time. Se alguém commitar uma edição direto na main por engano, não é o fim do mundo, mas reforce a regra com a pessoa.

## Passo a passo pra adicionar um item novo

1. Escolha o template certo em `templates/`:
   - Projeto/automação/iniciativa de um time → `TEMPLATE_INICIATIVA.md`
   - Ferramenta, documentação ou dataset compartilhado → `TEMPLATE_RECURSO.md`
   - Página de apresentação de um time → `TEMPLATE_TIME.md`
   - Não se encaixa em nenhum dos três → crie uma subpasta em `outros/<nome-da-subcategoria>/` e use o front matter com `tipo: outro`
2. Copie o template, preencha o front matter (bloco entre `---`) e o corpo do arquivo.
3. Salve com nome em `kebab-case-sem-acento.md` na pasta correspondente.
4. Rode `python3 scripts/gerar_indice.py` na raiz do repositório antes de commitar (ele atualiza o `README.md` automaticamente).
5. Commit e push direto na `main`. Pronto.

### Se você não tem terminal/Python disponível
Pode criar o arquivo direto pela interface web do GitHub: botão "Add file → Create new file", ou aperte a tecla `.` dentro do repositório pra abrir o editor completo (github.dev). Nesse caso o `README.md` vai ficar temporariamente desatualizado até alguém rodar o script — normal, é o custo do modelo "semi-automático" que escolhemos em troca de não ter CI/CD.

## Passo a passo pra editar ou apagar um item existente

1. Crie uma branch a partir da `main`.
2. Faça a alteração.
3. Se a edição mudar dados do front matter, rode o script de índice de novo.
4. Abra um Pull Request e peça aprovação de quem é dono do conteúdo (ou do repositório, se não tiver dono claro).

## Convenção de front matter (obrigatório em todo arquivo de conteúdo)

Cada tipo tem seus próprios campos — veja o template correspondente. O único campo que **todo arquivo precisa ter** é `tipo:` (`iniciativa`, `recurso`, `time` ou `outro`), porque é ele que o script usa pra categorizar no índice.

## Usando IA (Gemini/ChatGPT/Claude) pra preencher os templates

Veja `PROMPT_IA_PREENCHIMENTO.md` — é o prompt pronto pra qualquer pessoa do time colar junto com o contexto do projeto dela e receber o Markdown já formatado.
