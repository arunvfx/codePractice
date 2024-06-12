#!/bin/bash

export BLENDER_USER_SCRIPTS=/mnt/work/MyWorks/pyscripts/blender/pipeline/scripts
export PYTHONPATH=/mnt/work/MyWorks/pyscripts/blender/pipeline/.venv/lib/python3.11/site-packages:/mnt/work/MyWorks/pyscripts/blender/pipeline/scripts:$PYTHONPATH
#export BLENDER_USER_CONFIG=/mnt/work/MyWorks/Pyscript/blender/scripts/config

/opt/blender/blender-4.1.1/blender
