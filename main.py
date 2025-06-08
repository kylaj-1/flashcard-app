class Flashcard:
  def __init__(self, question, answer):
    self.question = question
    self.answer = answer


flashcards = []

def add_flashcard():
  question = input("Enter the question: ")
  answer = input("Enter the answer: ")
  flashcard = Flashcard(question, answer)
  flashcards.append(flashcard)
  print("\nFlashcard added!")


def view_flashcards():
  if not flashcards:
    print("Not a flashcard yet.")
  for i, card in enumerate(flashcards):
    print(f"\nCard {i+1}")
    print("Q:", card.question)
    input("Press Enter to flip...")
    print("A:", card.answer)


def main():
  while True:
    print("\n==== Flashcard App ====")
    print("1. Add Flashcard")
    print("2. View Flashcards")
    print("3. Quiz Mode")
    print("4. Exit")
    choice = input("Choose an option: ")


    if choice == "1":
      add_flashcard()
    elif choice == "2":
      view_flashcards()
    elif choice == "3":
      quiz_user()
    elif choice == "4":
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")


import random

def quiz_user():
  if not flashcards:
    print("No flashcards available for quiz.")
    return

  print("\n--- Quiz Mode ---")
  random.shuffle(flashcards)

  for card in flashcards:
    print("\nQuestion:", card.question)
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == card.answer.strip().lower():
      print("Correct!")
    else:
      print(f"No, the correct answer was: {card.answer}")
main()