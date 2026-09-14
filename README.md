# nDm — Nova Dádiva da Madeira

Бесплатные инструкции по португальской бюрократии. Пять языков: PT · EN · RU · DE · ES.
Домен: **https://ajuda.seedwave.pt**

## Что где лежит

| Путь | Что это |
| --- | --- |
| `index.html` | «Damos o Caminho» — корень домена: обложка с анимацией, чекер «Положено ли мне?», гид в шесть шагов, новость о законе (`?p=home|check|guia|news`) |
| `subsidio/index.html` | выпуск 2 — «Подача: пять шагов» (каждый экран портала + счёт TAP) |
| `subsidio/dinheiro/`, `subsidio/rejeitado/`, `subsidio/familia/` | три справочных выпуска 2 |
| `subsidio/img/*.jpg` | размеченные экраны портала ssm.gov.pt и счёта TAP |
| `subsidio/og-image.png` | обложка 1200×630 выпуска 2 (её же использует корень) |
| `tap/index.html` | выпуск 1 — «Documentos TAP» |
| `tap/img/s1…s8.jpg`, `tap/og-image.png` | экраны и обложка выпуска 1 |
| `ndm-icon.svg`, `icon.svg`, `*.png`, `manifest.webmanifest` | брендмарк, фавикон, иконки телефона, PWA-манифест |
| `CNAME` | ajuda.seedwave.pt |
| `_src/` | исходники: тела страниц, тексты по языкам, сборка, генераторы картинок |

## Как пересобрать страницы

Тела страниц: `_src/root-body.html` (корень, тексты пяти языков внутри), `_src/tap-body.html` (выпуск 1),
`_src/subsidio-body.html` (подача), `_src/ref-body.html` (общее тело трёх справочных).
Тексты выпуска 2 — по файлам `_src/i18n/<страница>.<язык>.js` (`subsidio`, `dinheiro`, `rejeitado`, `familia` × `pt en ru de es`).
Общие стили и движок выпуска 2 — `_src/ndm.css`, `_src/ndm.js`.

Из корня репозитория:

```
python3 _src/build.py
```

Скрипт оборачивает тела в `<head>` с метатегами, OG и иконками, вклеивает CSS, движок и тексты
и перезаписывает все `index.html`. Руками готовые `index.html` не правятся.

`_src/mkicons.py` пересобирает PNG-иконки, `_src/cover.py` — обложку выпуска 1,
`_src/cover2.py` — обложку выпуска 2, `_src/annotate.py` — размеченные скриншоты.
