#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
    Ce module propose les outils les plus courrant que j'utilise,
    et aussi pour retrouver des syntaxes peu utilisée,
    mais qui nécessiterait des recherches.
"""
 
__version__ = "0.03"
 
from tools import mytools

from network.http_download import HttpDownload
from network.tcpclient import TcpClient
from network import tcptwisted
from network import OSC3
