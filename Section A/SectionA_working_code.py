class Solution:
   
    def groupAnagrams(self, strs): #Indentation problem
       
     # Creating an empty dictionary.
      result = {}
      
      for i in strs:
         # Sorting the string and then joining the characters to form a string.
         x = "".join(sorted(i)) #Syntax problem
         
         # Checking if the sorted string is already present in the dictionary. If it is present, then
         # it is appending the string to the list of values.
         if x in result:
            result[x].append(i) 
         # If the sorted string is not present in the dictionary, then it is creating a new key with
         # the sorted string as the key and the string as the value.
         else:
            result[x] = [i] 
            
      # Returning the values of the dictionary.
      return list(result.values())
   
   
# Calling the function groupAnagrams with the list ["eat", "tea", "tan", "ate", "nat", "bat"] as the
# argument.
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))