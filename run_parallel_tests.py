import json
import threading
from paver.easy import sh


def run_behave_test(feature, task_id=0):
    sh('SET TASK_ID=%s & behave features/%s.feature' % (task_id, feature), ignore_error=True)

with open("browsers.json", "r") as f:
    capabilities = json.loads(f.read())
f.close()
process = []
for counter in range(2):
    p = threading.Thread(target=run_behave_test, args=("login", counter))
    process.append(p)
    p.start()

for job in process:
    job.join(timeout=180)
