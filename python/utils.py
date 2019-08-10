import maya.cmds as cmds
import os

def isCamera(camera):
    cam = None
    if cmds.nodeType(camera) == "camera":
        cam = camera
        return cam
    else:
        cam = cmds.listRelatives(camera, s=True)[0]
        return cam
    return cam

def GetAllRenderLayers():
    renderlayers = [i for i in cmds.ls(type="renderLayer") if len(i.split(":")) == 1]
    return renderlayers

def GetActiveRenderLayers():
    activeRL = [i for i in GetAllRenderLayers() if cmds.getAttr("%s.renderable" % i)]
    return activeRL

def GetCurrentRenderLayer():
    current = cmds.editRenderLayerGlobals(q=True, crl=True)
    return current

def GetAllCameras():
    cameras = cmds.ls("camera")
    return cameras

def GetRenderableCameras():
    cameras = GetAllCameras()
    renderCam = [i for i in GetAllCameras() if cmds.getAttr("%s.renderable" % i)]
    return renderCam

def SetActiveRenderLayers(renderLayers):
    if isinstance(renderLayers, str):
        renderLayers = [renderLayers]
    for rl in renderLayers:
        cmds.setAttr("%s.renderable" % rl, 1)

def DisableRenderLayers(renderLayers):
    if isinstance(renderLayers, str):
        renderLayers = [renderLayers]
    for rl in renderLayers:
        cmds.setAttr("%s.renderable" % rl, 0)

def SetRenderableCameras(cameras):
    if isinstance(cameras, str):
        cameras = [cameras]
    for camera in cameras:
        cam = isCamera(camera)
        cmds.setAttr("%s.renderable" % cam, 1)

