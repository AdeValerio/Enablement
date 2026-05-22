# Lab — Python JSON helper
## Write `tools/jsonpick.py` that reads stdin JSON, prints one field (arg), exits non-zero on error. Add two sample invocations in README.

`tools/jsonpick.py` parse JSON from standsard input (`stdin`) and extract a specific field. It returns a non-zero exit code if the JSON is invalid or the field does not exist.

### Sample Invocations

#### Example 1: Extracting a top-level string field (Success)
Pass a JSON string via `echo` and extract the value of the `status` key.
```bash
$ echo '{"status": "success", "code": 200}' | python3 tools/jsonpick.py status
success
$ echo $?
0
$ echo '{"status": "success", "code": 200}' | python3 tools/jsonpick.py file
Error: Field 'file' not found.
$ echo $?
1