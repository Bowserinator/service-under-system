# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2019  Diego Torres Milano
Created on 2022-01-10 by Culebra v20.4.4
                      __    __    __    __
                     /  \  /  \  /  \  /  \
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
"""

import sys
import os

try:
    sys.path.insert(0, os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

from com.dtmilano.android.viewclient import ViewClient, ViewNotFoundException

TAG = 'CULEBRA'

kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
vc = ViewClient(device, serialno, **kwargs2)

while True:
    vc.dump(window='-1')

    try:
        # Where logged in? CAS
        com_duosecurity_duomobile___id_logging_into_label = vc.findViewByIdOrRaise("com.duosecurity.duomobile:id/logging_into_label")

        # Desc, ie where logged in, etc..
        com_duosecurity_duomobile___id_pushinfo_content_description = vc.findViewByIdOrRaise("com.duosecurity.duomobile:id/pushinfo_content_description")
        com_duosecurity_duomobile___id_transaction_deny_button = vc.findViewByIdOrRaise("com.duosecurity.duomobile:id/transaction_deny_button")
        com_duosecurity_duomobile___id_transaction_approve_button = vc.findViewByIdOrRaise("com.duosecurity.duomobile:id/transaction_approve_button")

        # "Are you logging in to CAS (Central Authentication Service)?"
        # print(com_duosecurity_duomobile___id_logging_into_label.getText()) 

        # Location: [REDACTED]
        # Time: [REDACTED]
        # Username: [REDACTED]
        # print(com_duosecurity_duomobile___id_pushinfo_content_description.getContentDescription())

        com_duosecurity_duomobile___id_transaction_approve_button.touch()
    except ViewNotFoundException as e:
        continue
