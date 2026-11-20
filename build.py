#!/usr/bin/env python3
"""Zgradi index.html iz src/template.html + src/gradivo.md.

Uporaba:  pip install markdown   (enkrat)
          python3 build.py
"""
import hashlib, pathlib, re, unicodedata
import markdown

ROOT = pathlib.Path(__file__).parent


def slug(value, separator="-"):
    v = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    v = re.sub(r"[^\w\s-]", "", v).strip().lower()
    return re.sub(r"[\s_-]+", separator, v)


def main():
    md = (ROOT / "src" / "gradivo.md").read_text(encoding="utf-8")
    m = markdown.Markdown(extensions=["tables", "fenced_code", "toc"],
                          extension_configs={"toc": {"slugify": slug}})
    html = m.convert(md)
    # tabele v drsni okvir (mobilni zaslon)
    html = re.sub(r"<table>(.*?)</table>", r'<div class="tw"><table>\1</table></div>', html, flags=re.S)
    # zunanje povezave v novem zavihku
    html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', html)
    # kazalo iz naslovov 2. ravni
    toc = "".join(f'<a href="#{t["id"]}">{t["name"]}</a>'
                  for top in m.toc_tokens for t in top.get("children", []))
    tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    out = tpl.replace("<!--GRADIVO-->", html).replace("<!--TOC-->", toc)
    (ROOT / "index.html").write_text(out, encoding="utf-8")

    ver = hashlib.sha1(out.encode()).hexdigest()[:10]
    sw = (ROOT / "src" / "sw.js").read_text(encoding="utf-8").replace("__VER__", ver)
    (ROOT / "sw.js").write_text(sw, encoding="utf-8")
    print(f"index.html in sw.js zgrajena (verzija {ver})")


if __name__ == "__main__":
    main()
