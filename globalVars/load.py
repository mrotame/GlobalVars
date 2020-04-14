import os, json
class Load(object):
    # ---------------- Public Methods ----------------
    def now(self):
        if os.getenv('GlobalVars')!=None:
            return json.loads(os.getenv('GlobalVars'))
        else:
            return None


# ---------------- Test ----------------
if __name__ == "__main__":
    os.environ['GlobalVars'] = json.dumps({"hi":"hi"})
    print(Load().now())