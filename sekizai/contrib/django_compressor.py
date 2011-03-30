# -*- coding: utf-8 -*-
from compressor.css import CssCompressor
from compressor.js import JsCompressor

def css(data):
    return CssCompressor(data).output()

def js(data):
    return JsCompressor(data).output()

def css_inline(data):
    return CssCompressor(data).output_inline()

def js_inline(data):
    return JsCompressor(data).output_inline()