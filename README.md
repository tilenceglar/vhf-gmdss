# VHF GMDSS trener

Statična spletna stran za pripravo na izpit **VHF GMDSS** (Uprava RS za pomorstvo, Koper):

- **Gradivo** – učni načrt, snov po treh izpitnih predmetih, predloge glasovnih sporočil, kartica številk (z gumbom za tisk/PDF)
- **Simulator** – VHF DSC postaja z 9 scenariji (MAYDAY, lažni alarm, PAN PAN, SECURITE, rutinski klic, prejem alarma, MAYDAY RELAY, test), način Učenje in Izpit
- **Testi** – 86 vprašanj z razlagami, naključni testni izpit (24 vprašanj), ponavljanje napačnih
- **Ustni del** – 25 kartic z vzorčnimi odgovori

Vse je v eni datoteki `index.html`, brez strežnika in brez zunanjih knjižnic. Na telefonu jo lahko dodaš na začetni zaslon in deluje tudi brez povezave.

## Objava na GitHub Pages

1. Na GitHubu ustvari nov repozitorij (npr. `vhf-gmdss`), javen.
2. Naloži vse datoteke iz te mape (vključno s skrito `.nojekyll`):
   ```bash
   git init
   git add .
   git commit -m "VHF GMDSS trener"
   git branch -M main
   git remote add origin https://github.com/<uporabnik>/vhf-gmdss.git
   git push -u origin main
   ```
   ali preprosto *Add file → Upload files* v brskalniku.
3. **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`, mapa `/ (root)` → *Save*.
4. Po minuti je stran na `https://<uporabnik>.github.io/vhf-gmdss/`.

Neposredne povezave na zavihke: `#gradivo`, `#simulator`, `#test`, `#ustni`.

## Urejanje gradiva

Gradivo je v `src/gradivo.md` (navaden Markdown). Po spremembi zgradi stran znova:

```bash
pip install markdown
python3 build.py
```

Skripta vstavi gradivo v `src/template.html`, zapiše `index.html` in osveži verzijo offline predpomnilnika v `sw.js`. Simulator, vprašanja in kartice so v `<script>` delu `src/template.html` (seznama `Q` in `ORAL`, scenariji v `SC`).

## Struktura

```
index.html            zgrajena stran (to streže GitHub Pages)
sw.js                 offline predpomnilnik (zgrajen)
manifest.webmanifest  namestitev na telefon
icon.svg              ikona
build.py              gradnja index.html iz src/
src/gradivo.md        besedilo gradiva
src/template.html     postavitev, simulator, testi, kartice
src/sw.js             predloga za sw.js
```

## Opozorilo

Gradivo in simulator sta pripomoček za učenje. Simulator je splošna DSC postaja in se razlikuje od naprave na izpitu; postopki sledijo priporočilom ITU/IMO. Pred izpitom preveri aktualne informacije pri Upravi RS za pomorstvo.
