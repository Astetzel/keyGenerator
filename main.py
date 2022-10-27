from replit import clear as cls
import string
import random
import hashlib

def main():
  choice = input("[SYSTEM] Would you like to generate (g) a key or use (u) a key?\n> ")
  
  choices = ["u", "g"]
  cls()
  
  if choice in choices:
    if choice == "g":
      randomStuff = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
      notEncoded = "".join(random.choice(randomStuff) for i in range(20))
      encoded = notEncoded.encode()
      key = hashlib.sha256(encoded).hexdigest()
      keys = open("./keys/keys.txt", "a")
      keys.write(f"{key}\n")
      keys.close()
      print(f"[SYSTEM] Successfully generated key\n\n{key}")
      return
      
    if choice == "u":
      key = input("[SYSTEM] Please input a key\n> ")+"\n"

      cls()

      used = open('./keys/used.txt', 'r')
      lused = used.readlines()

      for line in lused:
        if line == key:
          print("[SYSTEM] Key already used")
          return

      used.close()
      
      keys = open('./keys/keys.txt', 'r')
      lkeys = keys.readlines()

      for line in lkeys:
        if line == key:
          key = key.replace("\n", "")
          print(f"[SYSTEM] Redeemed {key}")
          usedKeys = open('./keys/used.txt', 'a')
          usedKeys.write(key + "\n")
          usedKeys.close()
          return
          
      keys.close()

      print("[SYSTEM] Invalid key")
      return

        
  else:
    print("[SYSTEM] Invalid choice!")
    return

if __name__ == "__main__":
  main()
