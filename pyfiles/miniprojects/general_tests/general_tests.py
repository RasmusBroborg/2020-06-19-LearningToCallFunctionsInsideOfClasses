b_list = [
    ["a", "a", "a"],
    ["b", "b", "b"],
    ["c", "c", "c"]
]

player_winstring = "aaa"

string_list = ["", "", "", "", "", "", "", ""]

for column in range(len(b_list)):
    char_string += b_list[0][column]

# Check row matches current players string:
if b_list[0][0] + b_list[0][1] + b_list[0][2] == player_winstring:
    return True
