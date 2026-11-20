# VHF GMDSS izpit — učni načrt in gradivo

## Kako poteka izpit

Izpit opravljaš na Upravi RS za pomorstvo (URSP) v Kopru; traja največ 30 minut, teorija je ustna, praktični del pa na postaji VHF GMDSS ali simulatorju ([SPOT](https://spot.gov.si/sl/dejavnosti-in-poklici/poklici-in-strokovni-kadri/voditelj-in-upravljavec-colna)).

| Predmet (iz zapisnika izpita) | Kako se preverja | Kaj morajo slišati od tebe |
| --- | --- | --- |
| 1. Pravila o radijski službi | ustno | GMDSS, morska področja, MMSI, dovoljenja, tajnost, prioritete, straža |
| 2. Osnove radiotelefonije | ustno | kanali, doseg VHF, črkovalna abeceda, proceduralne besede |
| 3. Delo na VHF GMDSS postaji ali simulatorju | praktično | DSC alarm, MAYDAY na glas, preklic lažnega alarma, PAN PAN, SECURITE, rutinski DSC klic |

Predmeti so povzeti po uradnem obrazcu zapisnika ([Uradni list](https://www.uradni-list.si/files/RS_-2005-042-01649-OB~P008-0000.PDF)); če padeš en predmet, obstaja popravni izpit iz tega predmeta. Stroški: upravna taksa 18,14 € + pristojbina 22,00 €, s seboj osebni dokument in fotografija 3,5 × 4,5 cm ([SPOT](https://spot.gov.si/sl/dejavnosti-in-poklici/dovoljenja/potrdilo-o-usposobljenosti-za-upravljanje-s-postajo-vhf-gmdss)).

Praktični del je jedro: komisija ti da scenarij (npr. požar na čolnu) in pričakuje pravilen vrstni red tipk na DSC postaji ter glasovno sporočilo v angleščini. Dodaten brezplačen spletni tečaj s simulatorjem (tudi v slovenščini) je [eGMDSS](https://www.egmdss.com/gmdss-courses) — v njem kot obalna postaja nastopa MRCC Koper (MMSI 002780200).

## Učni načrt

Pet dni po približno 60–90 minut zadostuje; šesti dan je samo ponavljanje in testni izpit. Če imaš manj časa, združi dneva 1+2 in 3+4.

| Dan | Tema | Kaj narediš | Mejnik (preden greš naprej) |
| --- | --- | --- | --- |
| 1 | Pravila o radijski službi | Preberi predmet 1; nariši si morska področja A1–A4 | Znaš razložiti GMDSS, A1 in sestavo MMSI za ladjo, skupino in obalno postajo |
| 2 | Osnove radiotelefonije | Preberi predmet 2; črkovalno abecedo na glas črkuj svoje ime in ime čolna | Na pamet: kanali 16, 70, 6, 13, 12; doseg; 10 proceduralnih besed |
| 3 | Postopki v sili | Preberi predmet 3 (DSC + MAYDAY); simulator: način Učenje, scenarija MAYDAY in lažni alarm | MAYDAY sporočilo veš na glas brez lista |
| 4 | Nujnost, varnost, rutina | PAN PAN, SECURITE, rutinski DSC klic; simulator: ostali scenariji | Vsi scenariji v simulatorju brez napak |
| 5 | Prejem alarma, EPIRB, SART, NAVTEX | Prejem tujega DSC alarma, MAYDAY RELAY, EPIRB, SART in NAVTEX; testni izpit 1 in 2 | ≥ 85 % na testnem izpitu |
| 6 | Ponovitev | Kartica številk; simulator v načinu Izpit (brez namigov); testni izpit 3 | 2× zapored scenarij brez napake in test ≥ 90 % |

Največ točk se izgubi pri vrstnem redu v MAYDAY sporočilu in pri tem, kaj narediti, ko sam prejmeš DSC alarm. Ta dva dela vadi na glas, ne samo v glavi.

Simulator postaje, testni izpiti in kartice za ustni del so v zavihkih [Simulator](#simulator), [Testni izpit](#test) in [Ustni del](#ustni).

## Predmet 1: Pravila o radijski službi

### GMDSS

GMDSS (Global Maritime Distress and Safety System) je svetovni sistem za alarmiranje in reševanje na morju, določen v SOLAS, poglavje IV, v celoti uveden 1. 2. 1999. Cilj: ob nesreči takoj alarmirati obalni reševalni center (RCC) in ladje v bližini, ne glede na to, kje si.

Devet funkcij GMDSS (pogosto vprašanje):

1. Alarmiranje ladja → obala
2. Alarmiranje obala → ladja
3. Alarmiranje ladja → ladja
4. Komunikacije za koordinacijo iskanja in reševanja (SAR)
5. Komunikacije na kraju nesreče (on-scene)
6. Signali za določanje položaja (SART, AIS-SART)
7. Pomorske varnostne informacije (MSI: navigacijska in vremenska opozorila)
8. Splošne radijske komunikacije
9. Komunikacije most–most (bridge-to-bridge)

### Morska področja

| Področje | Pokritost | Doseg (približno) | Oprema |
| --- | --- | --- | --- |
| A1 | vsaj ena obalna postaja VHF DSC s stalno stražo na kanalu 70 | 20–30 NM | VHF DSC |
| A2 | obalna postaja MF DSC (2187,5 kHz) | 100–150 NM | + MF DSC |
| A3 | satelitsko pokritje Inmarsat | med 70° S in 70° J | + satelitska postaja ali HF |
| A4 | vse ostalo (polarna območja) | — | + HF DSC |

Slovensko morje in ves vzhodni Jadran sta v področju **A1**. Zato zadostuje VHF DSC postaja in izpit VHF GMDSS (ekvivalent SRC – Short Range Certificate).

### Kdo je kdo v Sloveniji

- **URSP** (Uprava RS za pomorstvo, Koper) — izpit in potrdilo o usposobljenosti operaterja.
- **AKOS** — dovoljenje za radijsko postajo na plovilu; s tem dobiš klicni znak (predpona S5) in MMSI ([AKOS](https://arhiv.akos-rs.si/radios-on-vessels-and-aircrafts)).
- **MRCC Koper** — center za iskanje in reševanje; VHF kanala 16 in 12, DSC kanal 70, MMSI 002780200 ([Luka Koper, Port Info Book](https://www.luka-kp.si/wp-content/uploads/2024/02/PORT-info-BOOK-2024.pdf)).
- Mednarodno: **ITU** (Radijski pravilnik – Radio Regulations) in **IMO** (SOLAS, SMCP).

### Identifikacija: MMSI

MMSI (Maritime Mobile Service Identity) je 9-mestna številka, vpisana v DSC postajo in poslana samodejno ob vsakem DSC klicu. Prve tri števke so MID (Maritime Identification Digits) = koda države: **Slovenija 278**, Hrvaška 238, Italija 247.

| Vrsta postaje | Oblika | Primer |
| --- | --- | --- |
| Ladijska postaja | MID + 6 števk | 278123456 |
| Skupina ladij | 0 + MID + 5 števk | 027812345 |
| Obalna postaja | 00 + MID + 4 števke | 002780200 (MRCC Koper) |
| SAR letalo | 111 + MID + 3 števke | 111278123 |
| AIS-SART | 970 + 6 števk | 970123456 |
| MOB naprava (AIS/DSC) | 972 + 6 števk | 972123456 |
| EPIRB z AIS | 974 + 6 števk | 974123456 |

MMSI vneseš v postajo enkrat; večina naprav ga po vnosu zaklene. Brez MMSI tipka DISTRESS ne pošlje alarma.

### Prioritete sporočil

| Prioriteta | Klic | Kdaj | DSC kategorija |
| --- | --- | --- | --- |
| 1. Stiska | MAYDAY | resna in neposredna nevarnost za plovilo ali osebo, potrebna takojšnja pomoč | Distress |
| 2. Nujnost | PAN PAN | nujno sporočilo o varnosti plovila ali osebe, brez neposredne nevarnosti (okvara motorja brez neposredne nevarnosti, medicinski nasvet ali prevoz poškodovanca) | Urgency |
| 3. Varnost | SECURITE | pomembno navigacijsko ali vremensko opozorilo (plavajoč zabojnik, ugasnjen svetilnik, nevihta) | Safety |
| 4. Rutina | — | vse ostalo | Routine |

Sporočilo višje prioritete ima vedno prednost: ko slišiš MAYDAY, prekineš vse ostalo.

### Pravila obratovanja

- **Tajnost zvez**: vsebine zvez, ki niso namenjene tebi, ne smeš razkrivati, zapisovati za druge ali izkoriščati.
- **Prepovedano**: nepotrebne ali lažne oddaje, oddaje brez identifikacije, nespodobno izražanje, motenje drugih postaj, klepet na kanalu 16, preverjanje postaje (radio check) na kanalih 16 ali 70.
- **Avtoriteta**: radijska postaja je pod nadzorom poveljnika oz. voditelja čolna; alarm v stiski se pošlje le po njegovem ukazu.
- **Čas**: v zvezah v sili se uporablja UTC (Slovenija = UTC+1 pozimi, UTC+2 poleti).
- **Straža**: med plovbo mora biti VHF DSC postaja vklopljena in mora neprekinjeno poslušati DSC kanal 70 (to dela samodejno), in kolikor je mogoče, kanal 16.
- **Dovoljenje** za postajo in **potrdilo** operaterja morata biti na plovilu.

## Predmet 2: Osnove radiotelefonije

### Lastnosti VHF

Pomorski VHF deluje v pasu 156–174 MHz in se širi **premočrtno** (kot svetloba), zato je doseg odvisen predvsem od višine anten, ne od moči.

<p class="formula">d [NM] ≈ 2,5 × ( √h<sub>1</sub> [m] + √h<sub>2</sub> [m] )</p>

Primer: čoln z anteno na 4 m in obalna postaja na 100 m → 2,5 × (2 + 10) = 30 NM. Dva čolna s 4 m antenama → približno 10 NM. Ročna postaja v roki (~1,5 m) doseže drug čoln le nekaj milj.

- **Moč**: fiksna postaja 25 W (HIGH) ali 1 W (LOW); ročna 5–6 W. V marini in na kratke razdalje uporabljaj LOW. Alarm v stiski gre vedno z 25 W.
- **Simpleks**: oddaja in sprejem na isti frekvenci, govori le eden naenkrat (tipka PTT). Vse zveze ladja–ladja.
- **Dupleks**: dve frekvenci (oddaja in sprejem ločeno), za javne zveze z obalnimi radijskimi postajami, npr. kanali 24–28.
- **Squelch** (SQ) izklopi šum, ko ni signala; nastavi ga ravno toliko, da šum izgine — previsoko pomeni, da ne slišiš šibkih postaj.

### Kanali, ki jih moraš znati

| Kanal | Frekvenca | Namen |
| --- | --- | --- |
| 70 | 156,525 MHz | **samo DSC** (digitalni klici) — nikoli govor |
| 16 | 156,800 MHz | stiska, nujnost, varnost in klicanje z govorom |
| 06 | 156,300 MHz | med ladjami; komunikacija na kraju nesreče (SAR z letali) |
| 13 | 156,650 MHz | most–most, navigacijska varnost, 1 W |
| 12 | 156,600 MHz | pristaniške operacije; MRCC Koper |
| 08, 72, 77 | — | delovni kanali med ladjami |
| 15, 17 | — | komunikacije na krovu, 1 W |
| AIS 1 / AIS 2 | 161,975 / 162,025 MHz | samodejni AIS (kanala 87B in 88B) |

Kanal 16 je samo za klic in sporočila v sili; po vzpostavljeni zvezi takoj preideš na delovni kanal.

### Mednarodna črkovalna abeceda

| A–I | J–R | S–Z | Številke |
| --- | --- | --- | --- |
| A Alfa | J Juliett | S Sierra | 0 Zero |
| B Bravo | K Kilo | T Tango | 1 One (wun) |
| C Charlie | L Lima | U Uniform | 2 Two (too) |
| D Delta | M Mike | V Victor | 3 Three (tree) |
| E Echo | N November | W Whiskey | 4 Four (fower) |
| F Foxtrot | O Oscar | X X-ray | 5 Five (fife) |
| G Golf | P Papa | Y Yankee | 6 Six |
| H Hotel | Q Quebec | Z Zulu | 7 Seven |
| I India | R Romeo | | 8 Eight (ait), 9 Nine (niner) |

Številke izgovarjaš posamično: kanal 72 = “seven two”, 45°32,5' N = “four five degrees three two decimal five minutes north”. Ime čolna črkuješ z “I SPELL”, npr. “SIRENA, I spell: Sierra India Romeo Echo November Alfa”.

### Proceduralne besede

| Beseda | Pomen |
| --- | --- |
| THIS IS | sledi ime postaje, ki kliče |
| ALL STATIONS | klic vsem postajam |
| OVER | končal sem, čakam odgovor |
| OUT | zveza je končana, odgovor ni pričakovan (nikoli “over and out”) |
| RECEIVED | sporočilo sprejeto |
| SAY AGAIN | ponovi |
| I SAY AGAIN | ponavljam |
| I SPELL | črkujem |
| CORRECTION | popravek zadnje besede/stavka |
| WAIT … MINUTES | počakaj |
| STATION CALLING | postaja, ki me kliče (ko ne razumeš imena) |
| HOW DO YOU READ | kako me slišiš; odgovor “I read you five” (lestvica 1–5) |
| SEELONCE MAYDAY | tišina — ukaz postaje v stiski ali koordinatorja (RCC) |
| SEELONCE DISTRESS | tišina — ukaz druge postaje blizu nesreče |
| PRUDONCE | omejen promet je spet dovoljen |
| SEELONCE FEENEE | promet v stiski je končan, kanal je prost |

IMO SMCP doda še označevalce sporočil (QUESTION, ANSWER, REQUEST, INFORMATION, INSTRUCTION, ADVICE, WARNING, INTENTION); izrečeš jih na začetku stavka, da sogovornik takoj ve, kakšno sporočilo sledi.

### Rutinski glasovni klic

1. Poslušaj, ali je kanal prost.
2. “[ime klicane postaje] ×3, THIS IS [tvoje ime] ×3, [klicni znak], OVER.”
3. Ko odgovori: predlagaj delovni kanal (“channel seven two”), preklopi in nadaljuj tam.
4. Če ni odgovora: klic največ trikrat v razmaku 2 minut, nato ponoviš šele po vsaj 3 minutah ([ITU-R M.1171](https://www.itu.int/rec/R-REC-M.1171/en)).

## Predmet 3: Delo na postaji VHF DSC

### Kontrole postaje

| Tipka | Kaj naredi |
| --- | --- |
| PWR / VOL | vklop in glasnost |
| SQ | squelch — odpravi šum |
| CH (gumb) | izbira kanala |
| 16/9 | takoj na kanal 16 |
| H/L | moč 25 W / 1 W |
| DW (TW) | dvojno (trojno) spremljanje: 16 + izbrani kanal |
| SCAN | pregledovanje kanalov |
| DISTRESS | pod rdečim pokrovom; drži 3–5 s = alarm v stiski |
| CALL / MENU | DSC meni: individualni, skupinski, vsem ladjam, test, preklic |
| PTT | tipka na mikrofonu — drži med govorom, spusti za poslušanje |

### Kaj je DSC

DSC (Digital Selective Calling) je kratek digitalni klic na kanalu 70, ki samodejno vsebuje tvoj MMSI. Alarm v stiski vsebuje še položaj in čas (UTC) iz GPS ter naravo stiske. DSC samo **napove** klic; pravo sporočilo vedno sledi z govorom na kanalu, navedenem v klicu.

| DSC klic | Komu | Kategorija | Govor nato |
| --- | --- | --- | --- |
| Distress alert | vsem (samodejno) | Distress | kanal 16 |
| All ships | vsem v dosegu | Urgency ali Safety | kanal 16 (varnostno sporočilo nato na delovnem kanalu) |
| Individual | eni postaji (MMSI) | Routine (ali Urgency/Safety) | predlagani delovni kanal, npr. 72 |
| Group | skupini (0 + MID …) | Routine | delovni kanal |
| Test | obalni postaji, npr. 002780200 | Safety – Test | brez govora |

Narava stiske, ki jo lahko izbereš: Fire/Explosion, Flooding, Collision, Grounding, Listing/Capsizing, Sinking, Disabled and adrift, Abandoning ship, Piracy/Armed attack, Man overboard, Undesignated (nedoločeno).

### Pošiljanje alarma v stiski (MAYDAY)

1. Preveri, da ima postaja položaj (GPS) — če ga nima, ga vneseš ročno.
2. **Hitra pot (nedoločen alarm)**: dvigni pokrov, drži DISTRESS 3–5 s.
3. **Če je čas (določen alarm)**: DISTRESS kratko ali MENU → izberi naravo stiske → drži DISTRESS 3–5 s.
4. Postaja sama preklopi na kanal 16 in moč 25 W. Počakaj na DSC potrditev (do približno 15 s).
5. Oddaj glasovni klic in sporočilo MAYDAY na kanalu 16 (predloga spodaj).
6. Alarm se brez potrditve samodejno ponavlja vsakih 3,5–4,5 min ([ITU-R M.541](https://www.itu.int/rec/R-REC-M.541/en)). Ostani na kanalu 16.

### Ko sam prejmeš tuj DSC alarm

1. Utišaj zvočni alarm, postaja preklopi na kanal 16 — **poslušaj**.
2. Zapiši MMSI, položaj, čas in naravo stiske.
3. **Ne potrjuj z DSC** — v področju A1 to stori obalna postaja oz. MRCC.
4. Če MRCC potrdi: sledi navodilom, pomagaj, če lahko.
5. Če si blizu in lahko pomagaš: po potrditvi obalne postaje (ali če te ni) potrdi prejem po govoru na kanalu 16 in obvesti MRCC Koper.
6. Če po približno 5 min ni potrditve obalne postaje in ni govora: obvesti MRCC z glasovnim MAYDAY RELAY na kanalu 16. DSC potrditev ali DSC relay pošlješ samo na zahtevo MRCC.

### Potrditev MAYDAY po govoru

“MAYDAY, [ime ponesrečenca] ×3, THIS IS [tvoje ime] ×3, RECEIVED MAYDAY.” Nato povej svoj položaj, hitrost in predviden čas prihoda.

### MAYDAY RELAY

Pošlješ ga, ko plovilo v stiski samo ne more oddajati (vidiš rakete, nima radia), ali ko na MAYDAY ni nihče odgovoril. Začneš z “MAYDAY RELAY ×3”, nasloviš “ALL STATIONS ×3” ali “MRCC KOPER ×3”, nato “THIS IS [tvoje ime] ×3” in posreduješ vse znane podatke o plovilu v stiski.

### Lažni alarm

**Postaje ne ugasni.** Takoj prekliči:

1. DSC: MENU → Cancel distress (če ga naprava ima).
2. Govor na kanalu 16: “ALL STATIONS ×3, THIS IS [ime] ×3, [klicni znak], MMSI […], POSITION […], CANCEL MY DISTRESS ALERT OF [datum] AT [čas] UTC, MASTER [ime], [ime čolna], [klicni znak], MMSI […], [datum, čas UTC].”
3. Obvesti MRCC Koper. Pravočasno preklican lažni alarm ni prekršek, nepreklican pa sproži iskanje.

### PAN PAN, SECURITE in rutinski DSC klic na postaji

- **PAN PAN**: MENU → All ships → Urgency → kanal 16 → pošlji; nato glasovno PAN PAN na kanalu 16.
- **SECURITE**: MENU → All ships → Safety → kanal 16 → pošlji; na kanalu 16 napoved z delovnim kanalom, sporočilo nato na tem delovnem kanalu.
- **Rutina**: MENU → Individual → vnesi MMSI → Routine → predlagaj kanal (npr. 72) → pošlji → počakaj potrditev (Able to comply) → preklopi na kanal in kliči po govoru.

### Druga oprema GMDSS

| Naprava | Kaj je | Ključno za izpit |
| --- | --- | --- |
| EPIRB | satelitska boja za alarm | 406 MHz prek Cospas-Sarsat (+ 121,5 MHz za iskanje); vklop ročno ali samodejno, ko se v globini 1,5–4 m sproži hidrostatski sprostilec; mora biti registrirana; ob lažni aktivaciji izklopi in obvesti MRCC |
| PLB | osebna boja | kot EPIRB, ročni vklop, nosiš jo na sebi |
| SART (radarski) | radarski odzivnik v reševalnem splavu | 9 GHz (radar X, 3 cm); na radarju 12 pik od položaja navzven; bližje kot ~1 NM pike preidejo v loke in kroge; doseg ~5 NM do ladje, več do letala |
| AIS-SART | AIS odzivnik | MMSI 970…; na plotterju krog s križem |
| NAVTEX | sprejemnik varnostnih sporočil | 518 kHz (angleščina) in 490 kHz (nacionalno); doseg do ~400 NM; ID sporočila B1 = postaja, B2 = vrsta (A navigacijsko opozorilo, B vremensko opozorilo, D SAR/pirati, E vremenska napoved; A, B, D ne moreš izklopiti) |

## Predloge glasovnih sporočil

Vsako predlogo preberi na glas, dokler je ne poveš brez lista. Primer plovila: **SIRENA**, klicni znak S5AB2 (Sierra Five Alfa Bravo Two), MMSI 278123456.

### MAYDAY (klic + sporočilo) — kanal 16

Mnemotehnika **MIPDANIO**: Mayday – Identiteta – Položaj – (Distress) narava – Assistance pomoč – Number oseb – Informacije – Over.

```
MAYDAY, MAYDAY, MAYDAY
THIS IS SIRENA, SIRENA, SIRENA
CALL SIGN SIERRA FIVE ALFA BRAVO TWO
MMSI TWO SEVEN EIGHT ONE TWO THREE FOUR FIVE SIX
MAYDAY SIRENA, CALL SIGN S5AB2, MMSI 278123456
MY POSITION FOUR FIVE DEGREES THREE TWO DECIMAL FIVE MINUTES NORTH,
ZERO ONE THREE DEGREES THREE ZERO DECIMAL ZERO MINUTES EAST
I AM ON FIRE, FIRE IN ENGINE ROOM OUT OF CONTROL
I REQUIRE IMMEDIATE ASSISTANCE
THREE PERSONS ON BOARD, PREPARING TO ABANDON TO LIFERAFT
WHITE MOTOR YACHT, NINE METRES
OVER
```

Položaj lahko podaš tudi glede na znano točko: “TWO NAUTICAL MILES WEST OF PIRAN LIGHTHOUSE”.

### Potrditev prejema MAYDAY

```
MAYDAY
SIRENA, SIRENA, SIRENA
THIS IS ALBATROS, ALBATROS, ALBATROS
RECEIVED MAYDAY
MY POSITION ... I AM PROCEEDING TO YOUR POSITION, ETA ONE FIVE MINUTES
OVER
```

### MAYDAY RELAY

```
MAYDAY RELAY, MAYDAY RELAY, MAYDAY RELAY
ALL STATIONS, ALL STATIONS, ALL STATIONS
THIS IS ALBATROS, ALBATROS, ALBATROS
CALL SIGN ..., MMSI ...
FOLLOWING RECEIVED FROM SAILING YACHT MARE:
MAYDAY MARE, POSITION ..., DISMASTED AND TAKING WATER,
FOUR PERSONS ON BOARD, REQUIRES IMMEDIATE ASSISTANCE
OVER
```

### Preklic lažnega alarma

```
ALL STATIONS, ALL STATIONS, ALL STATIONS
THIS IS SIRENA, SIRENA, SIRENA
CALL SIGN S5AB2, MMSI 278123456
POSITION ...
CANCEL MY DISTRESS ALERT OF 19 NOVEMBER AT 1015 UTC
MASTER [IME IN PRIIMEK], SIRENA, S5AB2, MMSI 278123456
19 NOVEMBER, 1017 UTC
OUT
```

### PAN PAN — kanal 16

```
PAN PAN, PAN PAN, PAN PAN
ALL STATIONS, ALL STATIONS, ALL STATIONS
THIS IS SIRENA, SIRENA, SIRENA
CALL SIGN S5AB2, MMSI 278123456
MY POSITION ...
ENGINE FAILURE, DRIFTING, NO IMMEDIATE DANGER
I REQUIRE A TOW
THREE PERSONS ON BOARD
OVER
```

Za zdravniški nasvet nasloviš “MRCC KOPER ×3” namesto ALL STATIONS in na koncu poveš “I REQUIRE MEDICAL ADVICE”.

### SECURITE — napoved na 16, sporočilo na delovnem kanalu

```
(kanal 16)
SECURITE, SECURITE, SECURITE
ALL STATIONS, ALL STATIONS, ALL STATIONS
THIS IS SIRENA, SIRENA, SIRENA
CALL SIGN S5AB2, MMSI 278123456
FOR NAVIGATIONAL WARNING LISTEN ON CHANNEL SEVEN TWO
OUT

(kanal 72)
SECURITE, SECURITE, SECURITE
ALL STATIONS, ALL STATIONS, ALL STATIONS
THIS IS SIRENA, SIRENA, SIRENA
FLOATING CONTAINER, DANGER TO NAVIGATION
IN POSITION ...
OUT
```

### Rutinski klic in preverjanje postaje (ne na 16)

```
ALBATROS, ALBATROS, ALBATROS
THIS IS SIRENA, SIRENA, SIRENA
RADIO CHECK, HOW DO YOU READ? OVER
— SIRENA, THIS IS ALBATROS, I READ YOU FIVE. OVER
— ALBATROS, THIS IS SIRENA, RECEIVED, THANK YOU. OUT
```

## Kartica za zadnji dan

| Kaj | Številka |
| --- | --- |
| DSC kanal | 70 (156,525 MHz) — nikoli govor |
| Stiska / klic govor | 16 (156,800 MHz) |
| SAR na kraju nesreče | 06 |
| Most–most | 13 (1 W) |
| MRCC Koper | kanala 16 in 12, MMSI 002780200 |
| MID Slovenija | 278 (Hrvaška 238, Italija 247) |
| MMSI obalne postaje | 00 + MID + 4 |
| MMSI skupine | 0 + MID + 5 |
| AIS-SART / MOB / EPIRB-AIS | 970 / 972 / 974 |
| Moč | 25 W / 1 W |
| Držanje DISTRESS | 3–5 s |
| Ponavljanje DSC alarma | vsakih 3,5–4,5 min |
| Prejem tujega alarma | čakaj ~5 min na obalno postajo, DSC potrditev le na zahtevo MRCC |
| Rutinski klic | 3× v razmaku 2 min, nato pavza ≥ 3 min |
| EPIRB | 406 MHz + 121,5 MHz, sprostitev 1,5–4 m |
| SART | 9 GHz, 12 pik, ~5 NM |
| NAVTEX | 518 kHz / 490 kHz; A, B, D obvezni |
| Morsko področje Slovenije | A1 |
| Doseg | 2,5 × (√h1 + √h2) NM |

Vrstni red prioritet: MAYDAY → PAN PAN → SECURITE → rutina. Tišina: SEELONCE MAYDAY / SEELONCE DISTRESS → PRUDONCE → SEELONCE FEENEE.

---

*Gradivo je pripomoček za učenje in ne nadomešča uradnih predpisov. Pred izpitom preveri aktualne informacije pri Upravi RS za pomorstvo ([SPOT](https://spot.gov.si/sl/dejavnosti-in-poklici/dovoljenja/potrdilo-o-usposobljenosti-za-upravljanje-s-postajo-vhf-gmdss)).*
