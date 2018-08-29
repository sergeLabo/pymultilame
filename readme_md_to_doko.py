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
Convertit le README.md en README.dokuwiki pour la page du wiki.
"""

from pymultilame import MyTools

mt = MyTools()

command = [ 'pandoc', 'README.md', '-f', 'markdown', '-t', 'dokuwiki',
            '-s', '-o', 'README.dokuwiki']
            
mt.run_command_system(command)
