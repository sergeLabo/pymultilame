## pymultilame

### Des scripts python pour les tâches répétitives.

Ce module propose les outils les plus courrant que j'utilise,
à utiliser en import ou en recopiant des bouts de code.

Ce module est une amélioration de

* [mylabotools](https://github.com/sergeLabo/mylabotools)

qui n'est plus maintenu.

#### Rubriques proposées

* Blender: Des scripts spécifiques pour le Blender Game Engine 2.7x et qui ne peuvent tourner que dans Blender
* Twisted: des exemples de twisted en python3
* Network: des sockets simples en python3
* Tools: des outils utilisés fréquement

### Modifications majeurs

#### Version 1.1

* Les tempo pour Blender comptent bien de 0 à n-1, soit n fois
* TcpClient différent pour python 2 et 3

### Installation

#### Installation de Twisted pour python 3.x

* [Installation de Twisted pour python 3.x](https://ressources.labomedia.org/installation_de_twisted)

~~~text
sudo pip3 install twisted
~~~

#### Installation de pymultilame

* [Créer son propre package python](https://ressources.labomedia.org/creer_son_propre_package_python)

~~~text
sudo pip3 install -e git+https://github.com/sergeLabo/pymultilame.git#egg=pymultilame
~~~

Mise à jour:

~~~text
sudo pip3 install --upgrade git+https://github.com/sergeLabo/pymultilame.git#egg=pymultilame
~~~


### Utilisation

~~~python
# Imports en python3
from pymultilame import HttpDownload
from pymultilame import MyTools
from pymultilame import TcpClient3
from pymultilame import MyConfig
from pymultilame import get_my_ip
from pymultilame import Multicast
from pymultilame import UdpClient
from pymultilame import PileFIFO
from pymultilame import Multicast

from pymultilame import Tempo
from pymultilame import EasyAudio
from pymultilame import TextureChange

from pymultilame import scene_change, droiteAffine, scene_change, print_str_args
from pymultilame import get_all_objects, get_all_scenes, get_scene_with_name


# Imports en python2

from pymultilame.myconfig2 import MyConfig2
from pymultilame.tcpclient2 import TcpClient2
~~~

### Licence

Touls les scripts sont sous

GNU GENERAL PUBLIC LICENSE Version 3

voir le fichier LICENSE

### Documentation

* [Créer son propre package python](https://ressources.labomedia.org/creer_son_propre_package_python)
* [pymultilame](https://ressources.labomedia.org/pymultilame)

### Merci à

* [La Labomedia](https://labomedia.org)
