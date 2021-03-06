# Copyright (c) 2005 Nokia Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from location import *
from appuifw import *

mcc, mnc, lac, cellid = gsm_location()

L = [ u"MCC: %d"%mcc, u"MNC: %d"%mnc, u"LAC: %d"%lac, u"Cell Id: %d"%cellid ]
appuifw.popup_menu(L, u"Location info")
