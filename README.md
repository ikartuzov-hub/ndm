# nDm — Nova Dádiva da Madeira

Бесплатные инструкции по португальской бюрократии. Пять языков: PT · EN · RU · DE · ES.
Домен: **https://ajuda.seedwave.pt**

## Что где лежит

| Путь | Что это |
| --- | --- |
| `index.html` | витрина nDm — список выпусков |
| `tap/index.html` | выпуск «Documentos TAP» |
| `tap/img/s1…s8.jpg` | размеченные экраны формы TAP |
| `tap/og-image.png` | обложка 1200×630 для превью ссылки |
| `ndm-icon.svg` | брендмарк серии (D + волна) |
| `icon.svg` | фавикон-тайл (D на фирменном фоне) |
| `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` | иконки для телефона |
| `manifest.webmanifest` | PWA-манифест |
| `CNAME` | ajuda.seedwave.pt |
| `_src/` | исходники: тела страниц, сборка, генераторы картинок |

## Как пересобрать страницы

Правится **`_src/root-body.html`** (витрина) или **`_src/tap-body.html`** (выпуск),
затем из корня репозитория:

```
python3 _src/build.py
```

Скрипт оборачивает тела страниц в `<head>` с метатегами, OG и иконками
и перезаписывает `index.html` и `tap/index.html`. Руками эти два файла не правятся.

`_src/mkicons.py` пересобирает PNG-иконки, `_src/cover.py` — обложку,
`_src/annotate.py` — размеченные скриншоты.
