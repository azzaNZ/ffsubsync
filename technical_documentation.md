# Technical Documentation for ffsubsync

This document provides a detailed breakdown of the subtitle synchronization process used in ffsubsync.

## Overview

ffsubsync synchronizes subtitles with a reference (typically a video file) by aligning speech segments detected in both the reference and the subtitles. It uses voice activity detection (VAD) for videos and subtitle timings for subtitle files. The alignment is performed using correlation techniques to find the optimal offset and potentially a framerate scale factor.

## Key Components

- **Speech Extraction**: Converts the reference and subtitles into speech activity arrays.
- **Alignment**: Finds the best offset and scale using aligners.
- **Transformation**: Applies the computed offset and scale to the subtitles.

## Detailed Process

1. **Argument Parsing and Validation**
   - Parse command-line arguments including reference, input subtitles, output file, and various options like VAD type, framerate, etc.
   - Validate inputs, permissions, and compatibility.

2. **Reference Pipeline Creation**
   - If the reference is a video: Use `VideoSpeechTransformer` with a chosen VAD (e.g., webrtc, auditok, silero) to extract speech activity.
   - If the reference is subtitles: Use `SubtitleSpeechTransformer` to convert subtitle timings to speech activity.
   - If the reference is a numpy array: Deserialize it directly.

3. **Subtitle Pipeline Creation**
   - For each input subtitle file, create a pipeline to parse and transform into speech activity.
   - Optionally, try different framerate ratios to account for mismatches.

4. **Alignment**
   - Use `MaxScoreAligner` with `FFTAligner` to compute the best offset and score for each potential framerate ratio.
   - Select the best matching pipeline based on the highest score.

5. **Transformation and Output**
   - Apply the computed offset using `SubtitleShifter`.
   - Optionally merge with reference subtitles if specified.
   - Write the transformed subtitles to the output file.

## Key Algorithms

- **VAD for Speech Detection**: Detects speech in audio streams.
- **FFT-based Alignment**: Uses fast Fourier transform for efficient correlation to find offsets.
- **Golden Section Search (optional)**: For optimizing framerate ratio.

This process ensures accurate synchronization by aligning speech patterns between the reference and subtitles.
