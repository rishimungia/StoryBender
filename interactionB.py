from random import randrange
print("<<<\tStory Bender\t>>>\n\n")

full_story = " "
genre_arr = ["superhero", "action", "drama", "thriller", "horror", "sci_fi"]

print("Select Genre of Story [ superhero | action | drama | thriller | horror | sci_fi ]")
genre = input()

print("\nSeed of Story [Prologue]: ")
seed = input()

story = story_generator("<BOS> <"+genre+"> "+seed, max_length = 75) 
result = (story[0]["generated_text"])
full_story = result
print(result)


next_seed = " "
while(True):
  mySent = nlp(result)
  for sentence in mySent.sents:
    continuation = str(sentence)
  next_seed = continuation
  rand_genre = genre_arr[randrange(0,6)]

  print("Select option to continue story:\n")

  genreA = genre_arr[randrange(0,6)]
  genreB = genre_arr[randrange(0,6)]
  genreC = genre_arr[randrange(0,6)]

  story = story_generator("<BOS> <"+genreA+"> "+next_seed, max_length = len(continuation) + 75)
  result_optA = (story[0]["generated_text"])
  print("[1]: "+ " ".join(result_optA.split()[0:len(continuation)+25]))
  story = story_generator("<BOS> <"+genreB+"> "+next_seed, max_length = len(continuation) + 75)
  result_optB = (story[0]["generated_text"])
  print("[2]: "+ " ".join(result_optB.split()[0:len(continuation)+25]))
  story = story_generator("<BOS> <"+genreC+"> "+next_seed, max_length = len(continuation) + 75)
  result_optC = (story[0]["generated_text"])
  print("[3]: "+ " ".join(result_optC.split()[0:len(continuation)+25]))
  print("\nEnter your option: ")
  select_opt = int(input())
  if(select_opt == 0):
    break
  elif(select_opt == 1):
    print("\n")
    full_story = full_story + " " + result_optA
    result = result_optA
    print(result)
  elif(select_opt == 2):
    print("\n")
    full_story = full_story + " " + result_optB
    result = result_optB
    print(result)
  elif(select_opt == 3):
    print("\n")
    full_story = full_story + " " + result_optC
    result = result_optC
    print(result)

print("<<<\tFull Story\t>>>\n")
print(full_story)