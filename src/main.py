import os
from tokenaizer import Tokenaizer
if __name__ == "__main__":
    current_dir: str = os.getcwd()
    spa_path: str = os.path.join(current_dir, "data-set.spa")
    eng_path: str = os.path.join(current_dir, "data-set.eng")
    
    toke_eng = Tokenaizer(eng_path)
    toke_spa = Tokenaizer(spa_path)

    toke_spa.build_words_matrix()

    toke_spa.build_dictionary()
    
    print(toke_spa.no_idea())
    
    
    



