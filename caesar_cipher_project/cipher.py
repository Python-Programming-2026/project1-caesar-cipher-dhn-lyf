def caesar_cipher(text, shift, mode="encrypt"):
    """
    参数:
        text: 需要加密/解密的文本
        shift : 偏移量
        mode: 'encrypt'表示加密，'decrypt'表示解密
    """

    if mode == 'decrypt':
        shift = -shift 
        
    result = ""
    
    for char in text:
        if char.isalpha():
            #只处理字母
            if char.isupper():
                # 处理大写字母
                shifted = (ord(char) - ord('A') + shift) % 26
                result += chr(shifted + ord('A'))
            else:
                shifted = (ord(char) - ord('a') + shift) % 26
                result += chr(shifted + ord('a'))
        else:
            #非字母不加密
            result += char
    
    return result

if __name__ == "__main__":
    original_text = input("输入文本")
    shift_amount = int(input("输入位移量"))
    
    mode = int(input('请输入模式:1-加密,2-解密'))
    if mode == 1:
        encrypted_text = caesar_cipher(original_text, shift_amount, 'encrypt')
        print(encrypted_text)
    elif mode == 2:
        decrypted_text = caesar_cipher(original_text, shift_amount, 'decrypt')
        print(decrypted_text)
    else:
        print('输入错误')
    