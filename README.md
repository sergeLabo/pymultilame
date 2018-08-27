## pymultilame

### Des scripts python pour les tâches répétitives.

    Ce module propose les outils les plus courrant que j'utilise,
    à utiliser en import ou en recopiant des bouts de code.

    Ce module est une amélioration de
    [mylabotools](https://github.com/sergeLabo/mylabotools)
    qui n'est plus maintenu.

#### Comprend les rubriques

* Blender: Des scripts spécifiques pour le Blender Game Engine 2.7x et qui ne peuvent tourner que dans Blender
* Twisted: des exemples de twisted en python3
* Network: des sockets simples en python3
* Tools: des outils utilisés fréquement

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
from pymultilame.blendertools import scene_change
from pymultilame import HttpDownload
~~~

### Licence

Touls les scripts sont sous

GNU GENERAL PUBLIC LICENSE Version 3

voir le fichier LICENSE

### Documentation

* [Créer son propre package python](https://ressources.labomedia.org/creer_son_propre_package_python)
* [pymultilame](https://ressources.labomedia.org/pymultilame)

### Conversion de README.md en dokuwiki

~~~text
pandoc README.md -f markdown -t dokuwiki -s -o README.dokuwiki
~~~

### Merci à

* [La Labomedia](https://labomedia.org)
