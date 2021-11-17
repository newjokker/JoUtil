# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import sys
import atexit
import signal


def daemonize(pidfile, *, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):

    if os.path.exists(pidfile):
        raise RuntimeError('Already running')

    # first fork (detaches from parent)
    try:
        if os.fork() > 0:
            raise SystemExit(0)     # parent exit (因为父进程和子进程都会执行下面的代码，父进程的 pid 大于 0 所以会被退出)
    except OSError as e:
        raise RuntimeError('fork # 1 failed .')

    os.chdir('/')
    os.umask(0)
    os.setsid()

    # second fork (relinquish session leadership)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork # 2 filed.')

    # Flush I/O buffers
    sys.stdout.flush()      # 显式地让缓冲区的内容输出 refer : https://blog.csdn.net/Just_youHG/article/details/102591313
    sys.stderr.flush()

    # Replace file descriptors for stdin, stdout, and stderr
    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())

    # write the PID file
    with open(pidfile, 'w') as f:
        print(os.getpid(), file=f)

    # Arrange to have the PID file remove on exit/signal
    atexit.register(lambda: os.remove(pidfile))

    # Signal handler for termination (required)
    def sigterm_handler(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)


def main():
    import time
    sys.stdout.write('Daemon started with pid {0} \n'.format(os.getpid()))
    while True:
        sys.stdout.write('Daemo Alive! {0}\n'.format(time.ctime()))
        time.sleep(10)



if __name__ == "__main__":

    PIDFILE = '/tmp/daemon.pid'

    if len(sys.argv) !=2:
        print('Usage {0} [start|stop]'.format(sys.argv[0], file=sys.stderr))
        raise SystemExit(1)

    if sys.argv[1] == 'start':
        try:
            daemonize(PIDFILE, stdout='/tmp/daemon.log', stderr='/tmp/daemon.log')
        except RuntimeError as e:
            print(e, file=sys.stderr)       # 把报错写到标准输出中，下次一并放到文件中去？
            raise SystemExit(1)

        main()

    elif sys.argv[1] == 'stop':
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print('Not Running', file=sys.stderr)
            raise SystemExit(1)

    else:
        print('Unknow command {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)
