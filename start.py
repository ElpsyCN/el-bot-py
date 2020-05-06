import os
import glob
console_path = glob.glob('./mirai-console-wrapper-*.jar')
os.system('java -jar ' + console_path[0])
