# 🥌 Curling Quiz

Ett webbaserat quiz om curling-statistik från curling.db-databasen.

## Snabbstart för utveckling

```bash
# Kör quiz manager för att lägga till frågor
python3 quiz/add_quiz.py

# Starta lokal server för test
cd quiz
python3 -m http.server 8080
# Öppna http://localhost:8080
```

## Publicera på GitHub Pages (GRATIS)

### 1. Skapa GitHub-repo

```bash
# Initiera git-repo i quiz-mappen
cd quiz
git init
git add .
git commit -m "Initial quiz commit"

# Skapa repo på GitHub (gör detta på github.com)
# Namnge det t.ex. "curling-quiz"

# Koppla till GitHub
git remote add origin https://github.com/DITT-NAMN/curling-quiz.git
git branch -M main
git push -u origin main
```

### 2. Aktivera GitHub Pages

1. Gå till repo-inställningar på GitHub
2. Klicka på "Pages" i menyn till vänster
3. Under "Source" välj "Deploy from a branch"
4. Välj "main" branch och "/ (root)" mapp
5. Klicka "Save"

Efter någon minut är sidan live på:
`https://DITT-NAMN.github.io/curling-quiz/`

### 3. Uppdatera quiz

Varje gång du vill lägga till nya frågor:

```bash
cd quiz
python3 add_quiz.py
# Lägg till dina frågor...

git add quiz-data.json
git commit -m "La till nya frågor"
git push
```

GitHub Pages uppdateras automatiskt inom någon minut!

## Använda Quiz Manager

```bash
python3 quiz/add_quiz.py
```

**Menyval:**
1. **Skapa nytt quiz** — Skapa helt nytt quiz med titel och frågor
2. **Lägg till frågor i befintligt quiz** — Utöka existerande quiz
3. **Snabb-add Nyman-fråga** — Snabbväg för Fredrik Nyman-frågor
4. **Visa statistik** — Se översikt över alla quiz

## Filstruktur

```
quiz/
├── index.html          # Huvudsida (frontend)
├── quiz-data.json      # Quiz-databas (JSON)
├── add_quiz.py         # CLI-verktyg för att lägga till quiz
└── README.md           # Denna fil
```

## Quiz-data format

```json
[
  {
    "id": "20260223000000",
    "title": "Quiz-titel",
    "date": "2026-02-23",
    "questions": [
      {
        "question": "Frågan?",
        "options": ["Alt A", "Alt B", "Alt C", "Alt D"],
        "correct": 1,
        "explanation": "Förklaring som visas efter svar"
      }
    ]
  }
]
```

## Features

- ✅ Responsiv design (mobil & desktop)
- ✅ JSON-baserad databas (enkelt att redigera)
- ✅ Omedelbar feedback efter svar
- ✅ Arkiv med alla tidigare quiz
- ✅ Poängberäkning & betyg
- ✅ Gratis hosting via GitHub Pages

## Befintliga quiz

| Quiz | Frågor | Tema |
|------|--------|------|
| Fredrik Nyman Special | 3 | Nymans fail & statistik |
| Databasens Stjärnor | 3 | Toppspelare |
| Svensk Curling | 3 | Daniel Magnusson & svenskar |

## Tips för nya frågor

Hitta intressant statistik:

```bash
# Öppna databasen
sqlite3 curling.db

# Exempel-queries:
SELECT name, COUNT(*) FROM teams GROUP BY name ORDER BY COUNT(*) DESC LIMIT 10;
SELECT * FROM games WHERE score1 = 0 OR score2 = 0 ORDER BY score1 + score2 DESC;
```

---

*"Man ska inte ha alla ägg i samma korg, men man ska ha alla quiz på samma sida."*
