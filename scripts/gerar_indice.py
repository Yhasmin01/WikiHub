#!/usr/bin/env python3
"""
Gera o índice automático do README.md a partir do front matter
dos arquivos .md em iniciativas/, recursos/, times/ e outros/.

Uso:
    python3 scripts/gerar_indice.py

Não usa nenhuma biblioteca externa de propósito — só precisa de Python 3
instalado, sem pip install de nada.

O script:
1. Varre as pastas de conteúdo.
2. Lê o bloco de front matter (entre as duas primeiras linhas "---") de cada .md.
3. Agrupa os itens por tipo (iniciativa / recurso / time / outro).
4. Substitui o conteúdo entre os marcadores <!-- INDEX:START --> e
   <!-- INDEX:END --> no README.md, preservando tudo o que estiver fora deles.
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(RAIZ, "README.md")

PASTAS_CONTEUDO = ["iniciativas", "recursos", "times", "outros"]
ARQUIVOS_IGNORADOS = {"README.md"}
PREFIXOS_IGNORADOS = ("TEMPLATE_",)

MARCADOR_INICIO = "<!-- INDEX:START -->"
MARCADOR_FIM = "<!-- INDEX:END -->"

TITULOS_POR_TIPO = {
    "iniciativa": "## 🚀 Iniciativas",
    "recurso": "## 📚 Recursos Compartilhados",
    "time": "## 👥 Times",
    "outro": "## 🗂️ Outros",
}


def parse_front_matter(caminho_arquivo):
    """Lê o bloco --- ... --- no topo do arquivo e retorna um dict simples.
    Suporta apenas pares 'chave: valor' de uma linha (sem listas YAML aninhadas
    de propósito, pra não precisar de biblioteca externa de parsing)."""
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", conteudo, re.DOTALL)
    if not m:
        return None

    bloco = m.group(1)
    dados = {}
    for linha in bloco.splitlines():
        linha = linha.strip()
        if not linha or ":" not in linha:
            continue
        chave, valor = linha.split(":", 1)
        dados[chave.strip()] = valor.strip()
    return dados


def coletar_itens():
    itens_por_tipo = {"iniciativa": [], "recurso": [], "time": [], "outro": []}

    for pasta in PASTAS_CONTEUDO:
        caminho_pasta = os.path.join(RAIZ, pasta)
        if not os.path.isdir(caminho_pasta):
            continue

        for atual, _subpastas, arquivos in os.walk(caminho_pasta):
            for nome_arquivo in arquivos:
                if not nome_arquivo.endswith(".md"):
                    continue
                if nome_arquivo in ARQUIVOS_IGNORADOS:
                    continue
                if nome_arquivo.startswith(PREFIXOS_IGNORADOS):
                    continue

                caminho_completo = os.path.join(atual, nome_arquivo)
                dados = parse_front_matter(caminho_completo)
                if not dados:
                    print(f"[aviso] sem front matter válido, pulando: {caminho_completo}")
                    continue

                tipo = dados.get("tipo", "outro")
                if tipo not in itens_por_tipo:
                    tipo = "outro"

                caminho_relativo = os.path.relpath(caminho_completo, RAIZ).replace(os.sep, "/")
                titulo = dados.get("titulo") or dados.get("nome_time") or nome_arquivo

                extra = ""
                if tipo == "iniciativa" and dados.get("time_responsavel"):
                    extra = f" — _{dados['time_responsavel']}_"
                elif tipo == "iniciativa" and dados.get("status"):
                    extra = f" — _{dados['status']}_"
                elif tipo == "time" and dados.get("lider"):
                    extra = f" — líder: _{dados['lider']}_"

                itens_por_tipo[tipo].append((titulo, caminho_relativo, extra))

    for tipo in itens_por_tipo:
        itens_por_tipo[tipo].sort(key=lambda x: x[0].lower())

    return itens_por_tipo


def montar_bloco_indice(itens_por_tipo):
    linhas = [MARCADOR_INICIO]
    for tipo, titulo_secao in TITULOS_POR_TIPO.items():
        itens = itens_por_tipo.get(tipo, [])
        linhas.append("")
        linhas.append(titulo_secao)
        if not itens:
            linhas.append("_Nenhum item cadastrado ainda._")
            continue
        for titulo, caminho, extra in itens:
            linhas.append(f"- [{titulo}]({caminho}){extra}")
    linhas.append("")
    linhas.append(MARCADOR_FIM)
    return "\n".join(linhas)


def atualizar_readme(bloco_novo):
    if not os.path.isfile(README_PATH):
        print("[erro] README.md não encontrado na raiz do repositório.")
        sys.exit(1)

    with open(README_PATH, "r", encoding="utf-8") as f:
        conteudo = f.read()

    if MARCADOR_INICIO not in conteudo or MARCADOR_FIM not in conteudo:
        print(
            "[erro] README.md não tem os marcadores "
            f"{MARCADOR_INICIO} / {MARCADOR_FIM}. Adicione-os manualmente uma vez."
        )
        sys.exit(1)

    padrao = re.compile(
        re.escape(MARCADOR_INICIO) + r".*?" + re.escape(MARCADOR_FIM), re.DOTALL
    )
    conteudo_novo = padrao.sub(bloco_novo, conteudo)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(conteudo_novo)


def main():
    itens_por_tipo = coletar_itens()
    bloco = montar_bloco_indice(itens_por_tipo)
    atualizar_readme(bloco)
    total = sum(len(v) for v in itens_por_tipo.values())
    print(f"[ok] Índice regenerado em {README_PATH} — {total} itens encontrados.")


if __name__ == "__main__":
    main()
