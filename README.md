# Lucenaut

Visualize and explore memory layout and contents of lucene index files.

## Roadmap

These a very initial thoughts I have about the project.

- A textual based terminal app for viewing memory-layout and contents. I prefer textual so that I can some nice layouts that helps with interactive inspection.
- Ferrocene as a backend for reading lucene files.
- IPC with a ferrocene-server -> I started with the plan of doing rust ffi and even added some demo code under `ffi_bridge`. But now I am thinking IPC could be a better choice. It will keep things simpler and we can also support multiple backends, one with ferrocene and one with lucene.
- Support for viewing segments_N, segment-info, stored fields, inverted index, terms-dict, doc-values, point trees etc.
- Lucene based backend (with IPC). This will require java on users system. So the packaged binary will by default use ferrocene, with an optional choise of using lucene.
- Lucenaut app (Tauri based). Could still re-use the IPC servers.
