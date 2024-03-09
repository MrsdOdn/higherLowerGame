from art import logo, vs
from game_data import data
import random

compare_a = {}
againts_b = {}


def random_data():
  '''Used to pull random data from dictionary'''
  return random.choice(data)

def answer_check(compare_follower, againts_follower):
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  if compare_follower == againts_follower:
    return True
  elif compare_follower < againts_follower and answer == "a":
    return False
  elif compare_follower < againts_follower and answer == "b":
    return True
  elif compare_follower > againts_follower and answer == "a":
    return True
  elif compare_follower > againts_follower and answer == "b":
    return False


def play_game():
  compare_a = random_data()
  againts_b = random_data()

  answers_count = 0
  is_game_true = True
  print(logo)
  while is_game_true:
    print(
        f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}."
    )
    print(vs)
    print(
        f"Againts B: {againts_b['name']}, {againts_b['description']}, from {againts_b['country']}."
    )
    is_game_true = answer_check(compare_a['follower_count'],
                                againts_b['follower_count'])



    if is_game_true == True:
      print(logo)
      answers_count += 1
      print(f"You're right! Current score: {answers_count}")
      compare_a = againts_b
      againts_b = random_data()
    else:
      print(logo)
      print(f"Sorry, that's wrong. Final score: {answers_count}")


play_game()
