#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#######################################################################
# Copyright (C) La Labomedia August 2018
#
# This file is part of pymultilame.

# pymultilame is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pymultilame is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pymultilame.  If not, see <https://www.gnu.org/licenses/>.
#######################################################################

"""
Récupère la doc de tous les scripts pour le wiki
et enregistre dans tools/docstring.txt
"""

import re
import ast

import pydoc

from mytools import MyTools


class GetDoc:
    """
    Lit tous les scripts pour récupérer les docstrings.
    Enregistre dans un fichier docstring.txt
    classé par script
    Contrainte:
    - doc du script
    - doc de la classe avec Usage
    - doc des méthodes
    - Ne récupère pas les fonctions en dehors de la class,
      ni le if __name__ == '__main__':
    """

    def __init__(self, directory):
        """
        directory = dossier racine de recherche des scripts
        """
        self.directory = directory
        self.mt = MyTools()
        self.DOC = ""

    def get_doc_batch(self):
        """
        OSC3 twisted dénére une doc top longue
        """
        #all_scripts = self.mt.get_all_files_list(self.directory, "py")
        all_scripts = [
        './blendertools.py',
        './fifolist.py',
        './mytools.py',
        './http_download.py',
        './tcpclient.py',
        ]

        if all_scripts:
            for script in all_scripts:
                self.get_doc(script)

        # Enregister en écrasant dans "docstring.txt"
        self.DOC += '\n'
        print(self.DOC)
        self.save_doc(self.DOC)
        
    def get_doc(self, script):
        """
        Crée la doc du script avec pydoc3.5
        Installation de pydoc3.5
        sudo pip3 install pydoc
        et l'ajoute à self.DOC
        """
        
        command = ['pydoc3.5', script]
        resp = self.mt.run_command_system(command)
        
        # Suppression des 5 premières lignes
        lines = resp.splitlines()  # list
        lines = lines[5:]

        n = 0
        line_to_delete = []
        for line in lines:
            # Si DATA au début de la ligne, suppr de la ligne et la suivante
            if line[:4] == 'DATA':
                line_to_delete.extend([n, n+1])

            # Si FILE au début de la ligne, suppr de la ligne et la suivante
            if line[:4] == 'FILE':
                line_to_delete.extend([n, n+1, n+2])

            # Si CLASSES au début de la ligne, suppr de la ligne et la suivante
            if line[:7] == 'CLASSES':
                line_to_delete.extend([n+1, n+2, n+3])

            # au suivant
            n += 1
            
        # Suppression des lignes
        somelist = [i for j, i in enumerate(lines) if j not in line_to_delete]

        # Suppr des 2 dernières lignes
        somelist = somelist[:-2] 
        
        # Reconversion de la liste en str
        doc = ''
        for l in somelist:
            doc += l + '\n'
            
        # Ajout
        self.DOC += '====' + script[2:-3] + '====\n'
        self.DOC += '<code txt>\n' + doc + '</code>\n\n'

    def save_doc(self, doc):
        """
        Save in docstring.txt
        """
        fichier = "docstring.txt"
        self.mt.write_data_in_file(doc, fichier)


if __name__ == '__main__':
    d = "/media/data/3D/projets/pymultilame/pymultilame/"
    gd = GetDoc(d)
    gd.get_doc_batch() 
