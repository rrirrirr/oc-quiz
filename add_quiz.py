#!/usr/bin/env python3
"""
Curling Quiz Manager - Lägg till nya quiz enkelt
Användning: python3 add_quiz.py
"""

import json
import os
from datetime import datetime

QUIZ_FILE = "/home/fg/clawd/quiz/quiz-data.json"

def load_quizzes():
    """Ladda befintliga quiz"""
    if os.path.exists(QUIZ_FILE):
        with open(QUIZ_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_quizzes(quizzes):
    """Spara quiz till fil"""
    with open(QUIZ_FILE, 'w', encoding='utf-8') as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)
    print(f"✓ Sparat {len(quizzes)} quiz till {QUIZ_FILE}")

def get_input(prompt, required=True):
    """Hämta input från användaren"""
    while True:
        value = input(f"{prompt}: ").strip()
        if value or not required:
            return value
        print("  (Obligatoriskt fält)")

def get_options():
    """Hämta 4 alternativ från användaren"""
    print("\nAnge 4 alternativ:")
    options = []
    for i in range(4):
        opt = get_input(f"  Alternativ {chr(65+i)}")
        options.append(opt)
    
    # Fråga vilket som är rätt
    while True:
        correct = get_input("Vilket är rätt svar? (A/B/C/D)").upper()
        if correct in ['A', 'B', 'C', 'D']:
            return options, ord(correct) - ord('A')
        print("  Ange A, B, C eller D")

def add_question():
    """Lägg till en enskild fråga"""
    print("\n" + "="*50)
    print("NY FRÅGA")
    print("="*50)
    
    question = get_input("Fråga")
    options, correct = get_options()
    explanation = get_input("Förklaring (visas efter svar)")
    
    return {
        "question": question,
        "options": options,
        "correct": correct,
        "explanation": explanation
    }

def create_quiz():
    """Skapa ett helt nytt quiz"""
    print("\n" + "="*60)
    print("🥌 SKAPA NYTT CURLING QUIZ")
    print("="*60)
    
    title = get_input("Quiz-titel (t.ex. 'SM 2026 Special')")
    
    questions = []
    while True:
        questions.append(add_question())
        
        more = get_input("\nLägg till en fråga till? (j/n)", required=False).lower()
        if more not in ['j', 'ja', 'y', 'yes']:
            break
    
    if not questions:
        print("Inga frågor tillagda. Avbryter.")
        return None
    
    return {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "title": title,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "questions": questions
    }

def add_to_existing_quiz(quizzes):
    """Lägg till frågor i befintligt quiz"""
    print("\nBefintliga quiz:")
    for i, q in enumerate(quizzes, 1):
        print(f"  {i}. {q['title']} ({len(q['questions'])} frågor)")
    
    while True:
        try:
            choice = int(get_input("\nVälj quiz att lägga till frågor i (nummer)"))
            if 1 <= choice <= len(quizzes):
                selected = quizzes[choice - 1]
                print(f"\nValt: {selected['title']}")
                
                while True:
                    selected['questions'].append(add_question())
                    more = get_input("\nLägg till en fråga till? (j/n)", required=False).lower()
                    if more not in ['j', 'ja', 'y', 'yes']:
                        break
                
                return quizzes
            print("Ogiltigt nummer")
        except ValueError:
            print("Ange ett nummer")

def quick_add_nyman_question(quizzes):
    """Snabb-add för Fredrik Nyman-frågor"""
    print("\n🎯 SNABB-ADD: Fredrik Nyman-fråga")
    
    # Hitta eller skapa Nyman-quiz
    nyman_quiz = None
    for q in quizzes:
        if 'Nyman' in q['title']:
            nyman_quiz = q
            break
    
    if not nyman_quiz:
        print("Inget Nyman-quiz hittat. Skapa ett först.")
        return quizzes
    
    print(f"Lägger till i: {nyman_quiz['title']}")
    nyman_quiz['questions'].append(add_question())
    return quizzes

def list_stats(quizzes):
    """Visa statistik om quiz"""
    print("\n" + "="*60)
    print("📊 QUIZ-STATISTIK")
    print("="*60)
    print(f"Totalt antal quiz: {len(quizzes)}")
    print(f"Totalt antal frågor: {sum(len(q['questions']) for q in quizzes)}")
    print("\nPer quiz:")
    for q in quizzes:
        print(f"  • {q['title']}: {len(q['questions'])} frågor (uppdat. {q['date']})")

def main():
    """Huvudmeny"""
    quizzes = load_quizzes()
    
    while True:
        print("\n" + "="*60)
        print("🥌 CURLING QUIZ MANAGER")
        print("="*60)
        print(f"Nuvarande quiz: {len(quizzes)} st")
        print("\nVad vill du göra?")
        print("  1. Skapa nytt quiz")
        print("  2. Lägg till frågor i befintligt quiz")
        print("  3. Snabb-add Nyman-fråga")
        print("  4. Visa statistik")
        print("  5. Avsluta")
        
        choice = get_input("\nVälj (1-5)", required=False) or "5"
        
        if choice == "1":
            new_quiz = create_quiz()
            if new_quiz:
                quizzes.append(new_quiz)
                save_quizzes(quizzes)
                print(f"\n✓ Quiz '{new_quiz['title']}' skapat med {len(new_quiz['questions'])} frågor!")
                
        elif choice == "2":
            if not quizzes:
                print("Inga quiz finns än. Skapa ett först.")
                continue
            quizzes = add_to_existing_quiz(quizzes)
            save_quizzes(quizzes)
            print("\n✓ Frågor tillagda!")
            
        elif choice == "3":
            quizzes = quick_add_nyman_question(quizzes)
            save_quizzes(quizzes)
            print("\n✓ Nyman-fråga tillagd!")
            
        elif choice == "4":
            list_stats(quizzes)
            
        elif choice == "5":
            print("\nHej då! 🥌")
            break
        else:
            print("Ogiltigt val")

if __name__ == "__main__":
    main()
