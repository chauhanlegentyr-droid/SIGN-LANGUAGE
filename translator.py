import json
import os

def load_dictionary():
    # Looks for our word-to-animation mapping file
    dict_path = os.path.join(os.path.dirname(__file__), 'dictionary.json')
    with open(dict_path, 'r') as file:
        return json.load(file)

def text_to_sign_sequence(input_text):
    dictionary = load_dictionary()
    
    # 1. Clean the text (make it lowercase and remove punctuation)
    clean_text = input_text.lower().replace("?", "").replace(".", "").replace("!", "")
    words = clean_text.split()
    
    # 2. Extract only the core concept words that exist in our sign library
    # (Sign language skips words like "is", "the", "a", "to")
    matched_words = [word for word in words if word in dictionary]
    
    # 3. Simple Grammar Rule Example: 
    # If the sentence is a question containing a question word ("where"), move it to the end.
    # e.g., ["where", "bathroom"] becomes ["bathroom", "where"]
    if "where" in matched_words:
        matched_words.remove("where")
        matched_words.append("where")
        
    # 4. Convert the final word order into their corresponding animation file names
    animation_sequence = [dictionary[word] for word in matched_words]
    
    return matched_words, animation_sequence

# --- Test the Script ---
if __name__ == "__main__":
    test_message = "Where is the bathroom?"
    ordered_words, animations = text_to_sign_sequence(test_message)
    
    print(f"\n📝 Typed Message: '{test_message}'")
    print(f"🔄 Sign Language Word Order: {ordered_words}")
    print(f"🎬 Animation Queue to Play: {animations}\n")
