# Curling Quiz - Snabbkommandon

## För mig (fisken):

```bash
# Lägg till nytt quiz
python3 /home/fg/clawd/quiz/add_quiz.py

# Snabb-statistik
python3 -c "
import json
with open('/home/fg/clawd/quiz/quiz-data.json') as f:
    quizzes = json.load(f)
print(f'{len(quizzes)} quiz, {sum(len(q[\"questions\"]) for q in quizzes)} frågor')
for q in quizzes:
    print(f'  • {q[\"title\"]}: {len(q[\"questions\"])} frågor')
"
```

## För Carlos (hosting):

### 1. Skapa GitHub-konto
Gå till https://github.com/signup

### 2. Skapa nytt repo
- Klicka "+" → "New repository"
- Namn: `curling-quiz`
- Kryssa i "Public"
- Klicka "Create repository"

### 3. Ladda upp filerna:
```bash
cd /home/fg/clawd/quiz

# Initiera git
git init

# Lägg till alla filer
git add .

# Commit
git commit -m "Initial quiz"

# Koppla till GitHub (ersätt med ditt användarnamn)
git remote add origin https://github.com/DITT-GITHUB-NAMN/curling-quiz.git
git branch -M main
git push -u origin main
```

### 4. Aktivera Pages
1. Gå till https://github.com/DITT-GITHUB-NAMN/curling-quiz/settings/pages
2. Under "Source" välj "Deploy from a branch"
3. Välj "main" och "/(root)"
4. Klicka "Save"

### 5. Klart!
Efter 1-2 minuter är sidan live på:
`https://DITT-GITHUB-NAMN.github.io/curling-quiz/`

## Uppdatera efter ändringar:
```bash
cd /home/fg/clawd/quiz
git add quiz-data.json
git commit -m "Nya frågor"
git push
```
