#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""
    Ce module propose les outils les plus courrant que j'utilise,
    et aussi pour retrouver des syntaxes peu utilisée que je n'ai pas en mémoire,
    mais qui nécessiterait des recherches.
    Les imports réalisé ici facilite les imports dans les scripts:
    Au lieu de:
        from pymultilame.httpdownload import HttpDownload
    faire:
        from pymultilame import HttpDownload
"""

name = "pymultilame"

from pymultilame.httpdownload import HttpDownload
from pymultilame.mytools import MyTools
from pymultilame.tcpclient import TcpClient
from pymultilame.myconfig import MyConfig
from pymultilame.getmyip import get_my_ip
from pymultilame.multicast import Multicast
from pymultilame.udpclient import UdpClient
from pymultilame.fifolist import PileFIFO
from pymultilame.multicast import Multicast

from pymultilame.blendertempo import Tempo
from pymultilame.blendersound import EasyAudio
from pymultilame.blendertexture import TextureChange
