# -*- coding: utf-8 -*-
"""Собирает готовые к заливке страницы репозитория ndm из исходников."""
import io, os, re

SITE = "https://ajuda.seedwave.pt"

HEAD = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{root}icon.svg?v=1" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="manifest" href="{root}manifest.webmanifest">
<meta name="apple-mobile-web-app-title" content="{app}">
<meta name="theme-color" content="#FAF6F1">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_PT">
<meta name="twitter:card" content="summary_large_image">
<style>html{{color-scheme:light dark}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
"""
FOOT = "\n</body>\n</html>\n"


def wrap(body, **kw):
    return HEAD.format(**kw) + body.strip() + FOOT


# ---------- /tap/ ----------------------------------------------------
tap = io.open("_src/tap-body.html", encoding="utf-8").read()
# в артефакте <title> идёт первой строкой — на сайте он живёт в <head>
tap = re.sub(r"^<title>.*?</title>\s*", "", tap, count=1, flags=re.S)
# брендмарк ведёт на витрину nDm, а не в Хаб (Хаб — в футере)
tap = tap.replace('<a class="brand" href="https://seedwave.pt/hub/">',
                  '<a class="brand" href="../">')

DESC_TAP = ("Como pedir à TAP a fatura e o comprovativo de viagem para o subsídio de "
            "mobilidade — passo a passo, com imagens. PT · EN · RU · DE · ES.")

os.makedirs("tap", exist_ok=True)
io.open("tap/index.html", "w", encoding="utf-8").write(wrap(
    tap, lang="pt", title="Documentos TAP — nDm", desc=DESC_TAP,
    app="Documentos TAP", root="../", ogtitle="Documentos TAP — Damos o caminho",
    og=SITE + "/tap/og-image.png", url=SITE + "/tap/"))

# ---------- / --------------------------------------------------------
root = io.open("_src/root-body.html", encoding="utf-8").read()
DESC_ROOT = ("Guias gratuitos sobre a burocracia portuguesa, em cinco línguas. "
             "nDm — Nova Dádiva da Madeira.")
io.open("index.html", "w", encoding="utf-8").write(wrap(
    root, lang="pt", title="nDm — Nova Dádiva da Madeira", desc=DESC_ROOT,
    app="nDm", root="", ogtitle="nDm — Damos o caminho",
    og=SITE + "/tap/og-image.png", url=SITE + "/"))

print("built: index.html, tap/index.html")
