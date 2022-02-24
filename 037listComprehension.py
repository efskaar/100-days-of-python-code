words = ['Testing','List','Comprehension']
fiveLetters = [word for word in words if len(word)>4]

#squaring
numbers = [1,2,3,4,5,6,7,8,9,10]
squared = [n*n for n in numbers]

#cubed
cubed = [n**3 for n in numbers]

#filter even
oddCubed = [cube for cube in cubed if cube%2]

#overlap 
overlap = [cube for cube in cubed if cube in squared]


if __name__ == '__main__':
  print(fiveLetters)
  print(squared)
  print(cubed)
  print(oddCubed)
  print(overlap)