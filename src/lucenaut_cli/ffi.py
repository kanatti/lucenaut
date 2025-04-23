from ctypes import cdll, Structure, c_char_p, c_uint32, c_bool, c_size_t, POINTER, byref

## TODO: Maybe we can code-gen this entire thing?

class SegmentMetadata(Structure):
    _fields_ = [
        ("name", c_char_p),
        ("doc_count", c_uint32),
        ("is_compound", c_bool),
        ("codec", c_char_p),
    ]

lib = cdll.LoadLibrary("ffi_bridge/target/release/libffi_bridge.so")

lib.read_segment_metadata.argtypes = [c_char_p, POINTER(c_size_t)]
lib.read_segment_metadata.restype = POINTER(SegmentMetadata)

lib.free_segment_metadata.argtypes = [POINTER(SegmentMetadata), c_size_t]

def get_segment_metadata(index_path: str = ""):
    count = c_size_t()
    result_ptr = lib.read_segment_metadata(index_path.encode(), byref(count))
    results = [result_ptr[i] for i in range(count.value)]

    segments = [{
        "name": s.name.decode(),
        "doc_count": s.doc_count,
        "is_compound": bool(s.is_compound),
        "codec": s.codec.decode()
    } for s in results]

    lib.free_segment_metadata(result_ptr, count)
    return segments
