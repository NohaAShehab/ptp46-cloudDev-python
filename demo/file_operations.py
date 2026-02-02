
import json
def read_all_data(filename):
    data =[]
    try:
        with open(filename) as f:
            data = json.load(f)
    except Exception as e:
        return data

    return data


def save_new_data(filename, data: [dict]):
    old_data = read_all_data(filename)
    old_data.extend(data)
    try:
        with open(filename, 'w') as f:
            json.dump(old_data, f)
            return True

    except Exception as e:
        return False


def save_data(filename, data: [dict]):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
            return True

    except Exception as e:
        return False


"""
    [apple, kiwi, banana]
    
    ----
    l
    ----
    :
    -i-i
    ---
    
    

"""
