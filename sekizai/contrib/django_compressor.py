# -*- coding: utf-8 -*-
from compressor import CssCompressor
from compressor import JsCompressor

def css(data):
    return CssCompressor(data).output()

def js(data):
    return JsCompressor(data).output()
