#WordCount.py
#Name: Meg Aerni
#Date: 10.5.2025
#Assignment: Lab 6, Part 2

def main():
  textFile = open("fish.txt", 'r')

  lineCount = 0
  wordCount = 0
  letterCount = 0
  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      character = words.split("")
      for char in character:
        charCount = charCount + 1
    #print(line)
  
  print("Lines: ", lineCount)
  print("Words: ", wordCount)
  print("Characters: ", charCount)

if __name__ == '__main__':
  main()
