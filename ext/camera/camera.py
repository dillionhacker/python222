#
# camera.py
#
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
#

import _camera
import graphics

_my_camera=_camera.Camera()

modemap={'RGB':_camera.EColor16M,
         'RGB16':_camera.EColor64K,
         'RGB12':_camera.EColor4K}

flashmap={'none':_camera.EFlashNone,
          'auto':_camera.EFlashAuto,
          'forced':_camera.EFlashForced,
          'fill_in':_camera.EFlashFillIn,
          'red_eye_reduce':_camera.EFlashRedEyeReduce}

whitebalancemap={'auto':_camera.EWBAuto,
                 'daylight':_camera.EWBDaylight,
                 'cloudy':_camera.EWBCloudy,
                 'tungsten':_camera.EWBTungsten,
                 'fluorescent':_camera.EWBFluorescent,
                 'flash':_camera.EWBFlash}

exposuremap={'auto':_camera.EExposureAuto,
             'night':_camera.EExposureNight,
             'backlight':_camera.EExposureBacklight,
             'center':_camera.EExposureCenter}

def take_photo(mode='RGB16',size=(640, 480),zoom=0,flash='none',
               exposure='auto',white_balance='auto',position=0):
    s=-1
    for i in range(_my_camera.max_image_size()):
        if _my_camera.image_size(modemap[mode], i)==size:
            s=i
            break
    if s==-1:
        raise ValueError, "Size not supported"
    if _my_camera.taking_photo():
        raise RuntimeError, "Photo request ongoing"
    return graphics.Image.from_cfbsbitmap(_my_camera.take_photo(modemap[mode],s,
                                                                zoom,flashmap[flash],
                                                                exposuremap[exposure],
                                                                whitebalancemap[white_balance],
                                                                position))
def image_modes():
    ret=[]
    modes=_my_camera.image_modes()
    for key in modemap:
        if (modes&modemap[key]):
            ret.append(key)
    return ret
def image_sizes(mode='RGB16'):
    sizes=[]
    for i in range(_my_camera.max_image_size()):
        s=_my_camera.image_size(modemap[mode], i)
        if s!=(0,0):
            sizes.append(s)
    return sizes
def max_zoom():
    return _my_camera.max_zoom()
def flash_modes():
    ret = []
    modes = _my_camera.flash_modes()
    for key in flashmap:
        if (modes&flashmap[key]):
            ret.append(key)
        if (flashmap[key]==0):
            ret.append(key)
    return ret
def exposure_modes():
    ret = []
    modes = _my_camera.exposure_modes()
    for key in exposuremap:
        if (modes&exposuremap[key]):
            ret.append(key)
        if (exposuremap[key]==0):
            ret.append(key)
    return ret
def white_balance_modes():
    ret = []
    modes = _my_camera.white_balance_modes()
    for key in whitebalancemap:
        if (modes&whitebalancemap[key]):
            ret.append(key)
        if (whitebalancemap[key]==0):
            ret.append(key)
    return ret
def cameras_available():
    return _my_camera.cameras_available()
