#WordCount.py
#Name: Meg Aerni
#Date: 10.5.2025
#Assignment: Lab 6, Part 2

def main():
  textFile = open("gettysberg.txt", 'r')

  lineCount = 0
  wordCount = 0
  letterCount = 0
  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      letter = w
      for l in letter:
        letterCount = letterCount + 1
    #print(line)
  
  print("Lines: ", lineCount)
  print("Words: ", wordCount)
  print("Characters: ", letterCount)

if __name__ == '__main__':
  main()
