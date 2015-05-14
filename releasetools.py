import common
import edify_generator
import os

def WritePolicyConfig(info):
  try:
    file_contexts = info.input_zip.read("META/file_contexts")
    common.ZipWriteStr(info.output_zip, "file_contexts", file_contexts)
  except KeyError:
    print "warning: file_context missing from target;"
    
def FullOTA_InstallEnd(info):
    WritePolicyConfig(info)

