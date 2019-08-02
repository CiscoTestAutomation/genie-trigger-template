#******************************************************************************
#*                               Trigger Template
#* ----------------------------------------------------------------------------
#* ABOUT THIS TEMPLATE - Please read
#*
#* - Any comments with "#*" in front of them (like this entire comment box) are
#*   for template clarifications only and should be removed from the final
#*   product.
#*
#* - Anything enclosed in <> must be replaced by the appropriate text for your
#*   application
#*
#* Support:
#*    pyats-support@cisco.com
#*
#* Description:
#*   This template file describes how to write a standard trigger.
#*
#* Read More:
#*   For the complete and up-to-date user guide on triggers, visit:
#*   http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/userguide/harness/developer/triggers.html
#*
#*******************************************************************************

#*******************************************************************************
#* DOCSTRINGS
#*
#*   All parsers should use the built-in Python docstrings functionality
#*   to define parser/class/method headers.
#*
#* Format:
#*   Docstring format should follow:
#*   URL= https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
#*
#* Read More:
#*   Python Docstrings, PEP 257:
#*   URL= http://legacy.python.org/dev/peps/pep-0257/
#*******************************************************************************

#*******************************************************************************
#* General procedure that triggers follow
#*
#*   1. Check the device has the configuration for an action, say action_1.
#*   2. Perform action_1.
#*   3. Verify the expected result of action_1 on the device.
#*   4. Undo action_1 / perform action_2, where action_2 is the opposite of action_1
#*      (If the device state was changed).
#*   5. Verify the expected result of action_2 on the device.
#*   
#    in your case, action_1 = {{ cookiecutter.action }}, action_2 = {{ cookiecutter.undo_action }}
#*******************************************************************************

import time
import logging
from ats import aetest

from genie.harness.base import Trigger

log = logging.getLogger()

class {{ cookiecutter.trigger_name }}(Trigger):
    '''<trigger description>'''

    @aetest.setup
    def prerequisites(self, uut):
        '''<description of the prerequisites>'''

        '''<code>'''

    @aetest.test
    def {{ cookiecutter.action }}(self, uut):
        '''<description of the action>'''
        
        '''<code that performs the action>'''

    @aetest.test
    def verify_{{ cookiecutter.action }}(self, uut):
        '''verify if {{ cookiecutter.action }} worked'''

        '''<code that performs the verification>'''

    @aetest.test
    def {{ cookiecutter.undo_action }}(self, uut):
        '''<description of the action>'''
        
        '''<code that performs the action>'''

    @aetest.test
    def verify_{{ cookiecutter.undo_action }}(self, uut):
        '''verify if {{ cookiecutter.undo_action }} worked'''

        '''<code that performs the verification>'''
