import sys
import argparse
import ffsubsync.ffsubsync as ffs

def main():
    # Manually create namespace with default options
    args = argparse.Namespace(
        reference='test-data/test.mp4',
        srtin=['test-data/test.srt'],
        srtout='synced.srt',
        # Default options
        overwrite_input=False,
        encoding='utf-8',
        max_subtitle_seconds=10.0,
        start_seconds=0,
        max_offset_seconds=60,
        apply_offset_seconds=0,
        frame_rate=23.976,
        skip_infer_framerate_ratio=False,
        non_speech_label=0.0,
        output_encoding='utf-8',
        reference_encoding=None,
        vad=None,
        no_fix_framerate=False,
        serialize_speech=False,
        extract_subs_from_stream=None,
        suppress_output_if_offset_less_than=None,
        ffmpeg_path=None,
        log_dir_path=None,
        gss=False,
        strict=False,
        vlc_mode=False,
        gui_mode=False,
        skip_sync=False,
        merge_with_reference=False,
        make_test_case=False,
        reference_stream=None,
    )
    
    result = ffs.run(args)
    if result["retval"] != 0:
        sys.exit(result["retval"])

if __name__ == "__main__":
    main()
