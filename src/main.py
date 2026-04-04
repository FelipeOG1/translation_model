from tokenaizer import Tokenaizer
from pathlib import Path
import os
if __name__ == "__main__":
    parent_path: str = Path(os.getcwd()).parent
    data_path = os.path.join(parent_path, "data")
    
    eng_toke = Tokenaizer(os.path.join(data_path, "data-set.eng"))
    print(eng_toke())
