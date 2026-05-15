Lab A
Lab A — Linux operator baseline (multi-topic)

On your sandbox/VM, document everything in `labs/week1-linux.md` with real command output.

(1) **Users & permissions:** show `id`, create a second user or use `sudo -u` if allowed; set `umask`; create `secret.txt`, chmod 600; explain your chmod choice in one sentence.

(2) **Processes & disk:** `ps aux --sort=-%mem | head`, `df -h`, `du -sh` on your repo dir.

(3) **systemd + logs:** pick any unit (`systemctl list-units --type=service | head`); `systemctl status <unit>`; `journalctl -u <unit> -n 30 --no-pager` (redact secrets).

(4) **Text pipeline:** use `grep` + one of `sed`/`awk` to extract one field from a file under `/etc` (read-only), save snippet to `labs/text-pipeline-sample.txt`.

(5) **Navigation:** `find` + `xargs` pattern OR `grep -R` over your practice folder only.
________________________________________________________________________________________________________________________
(1) Users & Permissions
# Display identity
id
# Set umask to ensure new files are private
umask 0077
# Create and secure the file
echo "This is a secret" > secret.txt
chmod 600 secret.txt
# Verify permissions
ls -l secret.txt


(2) Processes & Disk
# Top memory consumers
ps aux --sort=-%mem | head
# Filesystem usage (human-readable)
df -h
# Size of the current repository directory
du -sh .


(3) systemd + Logs
# Find an active service
systemctl list-units --type=service | head -n 10
# Check status (Replace <unit> with your choice, e.g., dbus.service)
systemctl status dbus.service
# View last 30 log entries
journalctl -u dbus.service -n 30 --no-pager


(4) Text Pipeline
# Grab the root line, then use awk to print the 7th field
grep "^root:" /etc/passwd | awk -F: '{print $7}' > labs/text-pipeline-sample.txt
# Verify the snippet
cat labs/text-pipeline-sample.txt


(5) Navigation
# Find all occurrences of "TODO" or "secret" within the current directory
grep -R "secret" . 
# OR use find + xargs to search files ending in .md
find . -name "*.md" | xargs grep "text*"


Lab B
Author `config/sample-app.yaml` with keys: `app.name`, `app.port`, `features` list. Run `python -c 'import yaml; yaml.safe_load(open("config/sample-app.yaml"))'` (or `yamllint` if installed). Fix errors until it parses.
_______________________________________________________________________________________________________________________
# Create directory for the lab
mkdir config
# Create Yaml file
vim config/sample-app.yaml
# Create the content of the file using VIM text editor
app:
  name: "Baseline-App"
  port: 8080
features:
  - "auth-v2"
  - "logging-stream"
  - "metrics-exporter"
# Test Command
python3 -c "import yaml; print(yaml.safe_load(open('config/sample-app.yaml')))"
# It should output this in the terminal
{'app': {'name': 'Baseline-App', 'port': 8080}, 'features': ['auth-v2', 'logging-stream', 'metrics-exporter']}

