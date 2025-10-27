#![no_main]

use libfuzzer_sys::fuzz_target;
use centaur_example::text_utils::{reverse_string, count_words, to_title_case};

fuzz_target!(|data: &[u8]| {
    // Try to convert bytes to valid UTF-8
    if let Ok(text) = std::str::from_utf8(data) {
        // Test all text operations
        let reversed = reverse_string(text);
        let word_count = count_words(text);
        let titled = to_title_case(text);

        // Verify some properties
        assert_eq!(reversed.len(), text.len(), "reverse should preserve byte length");
        assert!(word_count <= text.len(), "word count can't exceed text length");

        // Double reverse should give original
        let double_reversed = reverse_string(&reversed);
        assert_eq!(text, double_reversed, "double reverse should be identity");

        // Title case should preserve word count
        assert_eq!(count_words(&titled), word_count, "title case preserves word count");
    }
});
