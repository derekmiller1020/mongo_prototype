from log import Logs

(a,b) = (5,0)

try:
    c = a/b

except Exception, e:
    error_log = Logs()
    err_logs = error_log.insert_error(str(e))


