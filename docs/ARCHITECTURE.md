# Lucenaut Architecture

Lucenaut is a tool for exploring the contents of Lucene index files. It lets you visualize the memory layout and structure of the index.

## Components

### Frontend

A TUI application built using the Python Textual library, providing an interactive way to explore Lucene index files.

### Backend Options

Lucenaut supports multiple backend options for reading Lucene index files:


1. **Ferrocene IPC Server** (in-progress):
   - A standalone Rust server process (`ferrocene-ipc`) that reads Lucene index files
   - Communicates with the Python client via TCP sockets using a simple JSON-based protocol

2. **Lucene IPC Server** (planned):
   - A standalone Java server process that reads lucene index files.
   - Some JSON-based ICP protocol as ferrocene-ipc.

2. **Ferrocene FFI Bridge** (abandoned):
   - Uses a Rust library (`ffi_bridge`) compiled to a shared object (.so)
   - Provides a C API that the Python code calls via ctypes
   - This has been abandoned.

## Communication Protocol

The IPC protocol is based on JSON messages over TCP sockets:

- Client sends commands as single-line JSON objects
- Server responds with single-line JSON objects
- Supported commands:
  - Opening an index
  - Listing segments
  - Getting segment details
  - And more...

## Data Flow

1. User selects a Lucene index directory
2. Frontend starts the appropriate backend server (or connects to an existing one)
3. Frontend sends commands to query the index structure
4. Backend reads the index files and sends responses
5. Frontend visualizes the data in an interactive UI

## Future Extensions

- Support for more Lucene index features (doc values, norms, points)
- Memory layout visualization
- Support for different Lucene versions
- GUI frontend using Tauri
