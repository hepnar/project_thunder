'''OpenGL extension ARB.texture_query_levels

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_query_levels to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a new set of texture functions
	(textureQueryLevels) in the OpenGL Shading Language that exposes the
	number of accessible mipmap levels in the texture associated with a GLSL
	sampler variable.  The set of accessible levels includes all the levels of
	the texture defined either through TexImage*, TexStorage*, or TextureView*
	(ARB_texture_view) APIs that are not below the TEXTURE_BASE_LEVEL or above
	the TEXTURE_MAX_LEVEL parameters.  For textures defined with TexImage*,
	the set of resident levels is somewhat implementation-dependent.  For
	fully defined results, applications should use TexStorage*/TextureView
	unless the texture has a full mipmap chain and is used with a mipmapped
	minification filter.
	
	These functions means that shaders are not required to manually recompute,
	approximate, or maintain a uniform holding a pre-computed level count,
	since the true level count is already available to the
	implementation. This value can be used to avoid black or leaking pixel
	artifacts for rendering methods which are using texture images as memory
	pages (eg: virtual textures); methods that can't only rely on the fixed
	pipeline texture functions which take advantage of TEXTURE_MAX_LEVEL for
	their sampling.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_query_levels.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.texture_query_levels import *
from OpenGL.raw.GL.ARB.texture_query_levels import _EXTENSION_NAME

def glInitTextureQueryLevelsARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION