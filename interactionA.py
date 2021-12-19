continuation = ""
while(1):
  print("Enter the genre of the Story")
  genre = input()
  if(genre == '0'):
    break
  print("Seed of the Story")
  seed = continuation + input()
  print("Enter the length of the generated story")
  length = int(input())
  story = story_generator("<BOS> <"+genre+"> "+seed, max_length= length) 
  result = (story[0]["generated_text"])
  mySent = nlp(result)
  print(result)
  for sentence in mySent.sents:
    continuation = str(sentence)