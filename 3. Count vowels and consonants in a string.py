n =input()
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for i in n:
    if i.isalpha():        
        if i in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
