# crack.py
import os

class CaesarCracker:
    def __init__(self, dict_file="google-10000-english-no-swears.txt"):
        self.dict_file = dict_file
        self.dictionary = self.load_dictionary()
    
    def load_dictionary(self):
        """加载词典"""
        if not os.path.exists(self.dict_file):
            return set()
        
        with open(self.dict_file, 'r', encoding='utf-8') as f:
            return {line.strip().lower() for line in f if line.strip()}
    
    def crack(self, ciphertext, top_n=3):
        """破解凯撒密码"""
        from cipher import caesar_cipher
        
        if not self.dictionary:
            return []
        
        results = []
        for shift in range(26):
            plaintext = caesar_cipher(ciphertext, shift, mode='decrypt')
            words = plaintext.lower().split()
            
            if words:
                score = sum(1 for w in words if w in self.dictionary) / len(words)
            else:
                score = 0
            
            results.append((score, shift, plaintext))
        
        results.sort(key=lambda x: x[0], reverse=True)
        return results[:top_n]

# 测试代码
if __name__ == "__main__":
    cracker = CaesarCracker()
    cipher = "khoor zruog"
    results = cracker.crack(cipher)
    for score, shift, text in results:
        print(f"shift={shift}, score={score:.1%}: {text}")