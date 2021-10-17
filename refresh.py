import json
import os
import sys

import amazon_auth
    
if __name__ == "__main__":
    script_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    tokens_path = os.path.join(script_path, "tokens")

    if sys.argv.count != 2:
        print("usage: refresh.py <domain>")
        print("domains: com, co.uk, co.jp, de")
        exit()
    domain = sys.argv[1]

    if os.path.isfile(tokens_path):
        with open(tokens_path, "r") as f:
            tokens = json.loads(f.read())
        tokens = amazon_auth.refresh(tokens)

        if domain in tokens:

            with open(tokens_path, "w") as f:
                f.write(json.dumps(tokens))
        else:
            print("No token found for given domain")

    else:
        print("Could not find token file")
