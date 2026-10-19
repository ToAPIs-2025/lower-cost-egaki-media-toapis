from pathlib import Path
import shutil
base=Path(__file__).resolve().parents[1]
for source,target in [('examples/gpt-image-2-vip.png','public/images/gpt-image-2-vip.png'),('examples/seedance-2-5.mp4','public/videos/seedance-2-5.mp4')]:
 p=base/target;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(base/source,p)
shutil.copyfile(base/'integration/video.mdx',base/'video.mdx')
