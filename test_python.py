import sys

if len(sys.argv) >= 2:
    body = sys.argv[1].replace("### ", "").replace("_No response_", "").split("\n\n")
    i = 0
    while i < len(body) :
        if body[i+1]:
            print(f"{body[i]}: {body[i+1]}")
        i += 2
