with open('/Users/benelster/Documents/Hackathon fall 2024/UOHackathon/cityData.csv', 'r') as f:
    content = f.read()
rows = list(content.strip())]

def chars_to_strings(char_list):
    result = []
    current_string = ""
    
    for char in char_list:
        
        if char == '\n':
            result.append(current_string)
            current_string = ""
        elif char == '|':
            result.append(current_string)
            current_string = ""
        else:
            current_string += char
    
    # Append the last string if not empty

    
    return result

def get_area(area_list):
    
    
#main
#full_list = chars_to_strings(rows)
#input = (Jakes_str)
#get_area(full_list, input) = city code