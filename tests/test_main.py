### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
#
#    Main unit test interface for PyNIfTI
#
#    Copyright (C) 2007 by
#    Michael Hanke <michael.hanke@gmail.com>
#
#    This package is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    version 2 of the License, or (at your option) any later version.
#
#    This package is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

import unittest
import test_fileio
import test_utils

if __name__ == '__main__':
    
    ts = unittest.TestSuite( [ test_fileio.suite(), 
                               test_utils.suite() ] 
                           )

    unittest.TextTestRunner().run( ts )
    
