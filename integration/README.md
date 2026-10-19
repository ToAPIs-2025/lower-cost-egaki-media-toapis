# Egaki reuse recipe

The reusable part is an original local-media MDX composition. Run `python integration/copy-assets.py`, install the official Egaki CLI separately, then run `egaki dev video.mdx` to preview its images/video on your machine. Use the CLI's documented render/export controls after preview.

The three PNGs and the Seedance 2.5 clip were generated live by the independent ToAPIs client. The MDX follows the upstream's documented local image/Video syntax; Egaki preview/export has not been run in this delivery. This is not a native Egaki ToAPIs Provider, not a successful Egaki CLI API call, and not a repackaged Egaki build. No explicit root source license was identified at the pinned revision, so this repository publishes only our client, original assets and original MDX example. Before a code Provider PR, ask the maintainer for the extension point and applicable contribution license.

Video generation uses first-frame Seedance 2.5 on ToAPIs, then imports the completed local MP4. Egaki's own speech/transcription routes are outside this example.

