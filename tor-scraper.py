import socks
import socket

import stem.process

SOCKS_PORT=7000# You can change the port number

tor_process = stem.process.launch_tor_with_config(
    config = {
        'SocksPort': str(SOCKS_PORT),
    },
)


socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5,
                      addr="127.0.0,1", #theres a ',' change it to '.' -- linkedin was being glitchy
                      port=SOCKS_PORT)
socket.socket = socks.socksocket




tor_process.kill()
﻿