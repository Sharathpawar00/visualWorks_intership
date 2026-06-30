import string
password = "sharath@937"

# special = "!@#$%^&*()_-+=<>?/"
with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print(" Your password is veernable to attackes try different onces!")
    exit()


upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
char = [upper_case, lower_case, digits, special]
if (len(password) > 8):
    char.append(True)


print(
    f"your score is {str(sum(char))} password has different character type {str(sum(char)-1)}")
# for ch in password:
#     if ch.isupper():
#         score += 1
#     if ch.isdigit():
#         score += 1
#     if ch.lower():
#         score += 1
#     if ch in special:
#         score += 1
# here the score was giving me 16  the score should be 5 out of  so i opted to this solution
# so any function return boolen value so score does't get updated after each upper case or othe casees
# so the problem i am having is its cheaking for ever character and adding to score so i want to
# since i want to only check once if the any of thise conditions are satified only it should update the score
