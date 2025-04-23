use std::ffi::CString;
use std::os::raw::c_char;

// TODO: Maybe we can code-gen this entire thing?

#[repr(C)]
pub struct SegmentMetadata {
    name: *const c_char,
    doc_count: u32,
    is_compound: bool,
    codec: *const c_char,
}

#[no_mangle]
pub extern "C" fn read_segment_metadata(_path: *const c_char, count: *mut usize) -> *mut SegmentMetadata {
    let dummy_segments = vec![
        SegmentMetadata {
            name: CString::new("segment_A").unwrap().into_raw(),
            doc_count: 1000,
            is_compound: true,
            codec: CString::new("Lucene90").unwrap().into_raw(),
        },
        SegmentMetadata {
            name: CString::new("segment_B").unwrap().into_raw(),
            doc_count: 500,
            is_compound: false,
            codec: CString::new("Lucene87").unwrap().into_raw(),
        },
    ];

    let len = dummy_segments.len();
    unsafe { *count = len };
    let ptr = dummy_segments.as_ptr();
    std::mem::forget(dummy_segments); // pass ownership to Python
    ptr as *mut SegmentMetadata
}

#[no_mangle]
pub extern "C" fn free_segment_metadata(ptr: *mut SegmentMetadata, count: usize) {
    if ptr.is_null() {
        return;
    }
    unsafe {
        let slice = std::slice::from_raw_parts_mut(ptr, count);
        for s in slice {
            CString::from_raw(s.name as *mut _);
            CString::from_raw(s.codec as *mut _);
        }
        Vec::from_raw_parts(ptr, count, count); // dealloc
    }
}
