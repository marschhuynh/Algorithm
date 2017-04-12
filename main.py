HammingDistance = __import__("Hamming Distance")
IslandPerimeter = __import__("Island Perimeter")
KeyboardRow = __import__("Keyboard Row")
NextGreaterElementI = __import__("Next Greater Element I")
NumberComplement = __import__("Number Complement")
ReverseStringII = __import__("Reverse String II")

result = HammingDistance.Solution().hammingDistance(1,4)
print(result)

result = IslandPerimeter.Solution().islandPerimeter( [[0, 1, 0, 0],
                                             [1, 1, 1, 0],
                                             [0, 1, 0, 0],
                                             [1, 1, 0, 0]])
print(result)

result = KeyboardRow.Solution().fizzBuzz(15)
print(result)

result = NextGreaterElementI.Solution().nextGreaterElement([1,4,2],[1,4,2,4,5,7])
print(result)

result = NumberComplement.Solution().findComplement(5)
print(result)

result = ReverseStringII.Solution().reverseStr("abcdefghi", 2)
print(result)