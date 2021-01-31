import shutil

def clean():
  print("Performing clean...")
  print('Removing "doc" directory...')
  shutil.rmtree("./doc")
  print("Clean done.")