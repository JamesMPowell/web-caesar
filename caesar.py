def encrypt(text,rot):
    temp = list(text)
    new_text = ""
    new_char = ""
    if rot >= 26:
            rot = rot-26
    for i in temp: 
        new_char = rotate_character(i,rot)
        new_text = new_text +new_char
    return new_text

def alphabet_position(letter):
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz" 
    temp = cap.find(letter)
    if temp == -1:
            return lower.find(letter)
    else:
        return temp

def rotate_character(char,rot):
    if char.isalpha():
        cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"         
        temp_pos = alphabet_position(char)
        
        temp = cap.find(char)
  
        if temp == -1:
            new_pos = lower[temp_pos+rot-26] 
        else:
            new_pos = cap[temp_pos+rot-26]
        return new_pos
    else:
        return char